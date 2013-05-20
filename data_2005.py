## Import modules

import pickle, csv, pandas
import lxml.etree

## Getting the data from the text files.

temp = []

with open('TDF2005.txt', 'rU') as f:
    reader = csv.reader(f, delimiter= '\t')
    for row in reader:
        temp.append(row)

with open('temp_2005.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(temp)

def rename(element):
    if element == 'Year of Birth': return 'YOB'
    elif element == 'Type of Rider': return 'Type'
    elif len(element)>3: return element.split(' ')[0]
    else: return element

def diff(x,y):
    return y-x

def get_time_differences(df):
    for i in range(1,22):
        if i==1: df['t1'] = df.T1
        else:
            x = i - 1
            df['t%s' % i] = diff(df['T%s' % x], df['T%s' % i])

data = pandas.read_csv('temp_2005.csv')
columns = [rename(element) for element in list(data.columns)]
data.columns = columns

get_time_differences(data)

columns_to_drop = [col for col in data.columns if 'T' in col or 'R' in col]
columns_to_drop = [col for col in columns_to_drop if len(col)<4 and col!='R21' and col!='T21']

data = data.drop(columns_to_drop, axis =1)

## Getting the data from the wikipedia.

url = 'http://en.wikipedia.org/wiki/%s_Tour_de_France'

parser = lxml.etree.HTMLParser(encoding='utf-8')

def get_siblings(node):
    return node.getparent().getchildren()

def get_rows_for_wiki_table(tree, caption):
    """   Return the first element because there is only one element in the list.   """
    return [get_siblings(table_caption) for table_caption in tree.xpath('//table//caption') if table_caption.text == caption][0]

def get_info_from_table(column, wiki_table):
    """   Slice up for first two elements to get rid of titles and some HTML tags.   """
    return [a[column] for a in [[b for b in row.getchildren()] for row in wiki_table[2:]]]

def stage_style(list_of_dicts):
    """   This is actually a list of list of dicts, so we take this into account   """
    if len(list_of_dicts)==1:
        if 'Plainstage' in list_of_dicts[0]['src']: return 'P'
        elif 'Mediummountainstage' in list_of_dicts[0]['src']: return 'H'
        elif 'Mountainstage' in list_of_dicts[0]['src']: return 'M'
    else:
        if list_of_dicts[0]['title']=='Individual time trial': return 'TT'
        elif list_of_dicts[0]['title']=='Team time trial': return 'TT'

tree = lxml.etree.parse(url % 2005, parser)
wiki_table = get_rows_for_wiki_table(tree, 'Stage results')

raw_km = [element.text for element in get_info_from_table(4, wiki_table)]
km = [float(element.split('km')[0][:-1]) for element in raw_km]

raw_stage_type = [[child.attrib for child in element.getchildren()] for element in get_info_from_table(3, wiki_table)]
stage_type = [stage_style(element) for element in raw_stage_type]

## Combining the two datasets (for 2005)

def speed_calculator(distance, time):
    return distance/(time/3600)

# overall speed
tot_km = sum(km)
data['overall_speed'] = speed_calculator(tot_km, data['T21'])

mountain_km = zip(km, stage_type)
stage_info = zip(['t%s' % i for i in range(1,22)],['S%s' % i for i in range(1,22)],stage_type, km)

mountain_stage_columns = [x[1] for x in stage_info if x[2]=='M']
km_mtn = [x[3] for x in stage_info if x[2]=='M']

tt_stage_columns = [x[1] for x in stage_info if x[2]=='TT']
km_tt = [x[3] for x in stage_info if x[2]=='TT']

def distance_mtn(distance_list, stages_done):
    return sum(distance_list[:stages_done])

temp = data.filter(mountain_stage_columns)
data['mtn_time'] = temp.sum(1)
data['mtn_stages']=temp.count(axis=1)
data['mtn_distance'] = data.mtn_stages.apply(lambda x: sum(km_mtn[:x]))
data['mtn_speed'] = speed_calculator(data['mtn_distance'], data['mtn_time'])

temp = data.filter(tt_stage_columns)
data['Year'] = 2005
data['tt_time'] = temp.sum(1)
data['tt_stages']=temp.count(axis=1)
data['tt_distance'] = data.tt_stages.apply(lambda x: sum(km_tt[:x]))
data['tt_speed'] = speed_calculator(data['tt_distance'], data['tt_time'])

database = data.filter(['Year','Name', 'R21', 'overall_speed', 'mtn_speed', 'tt_speed'])
database.columns = ['Year','Name', 'Ranking', 'Total', 'Mtn', 'Tt']