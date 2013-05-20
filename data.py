# This has changed because I changed dataset!

import pandas as pd

# check hierarchical indexing to maybe improve this stuff. A bit messy for now. => check this tonight
years = [2005, 2006, 2007, 2008, 2010, 2011, 2012]
df = pd.read_csv('dataset.csv')

# get quits
quits = [(2005, df.Name_2005.count(), df.ranking_2005.count()),
         (2006, df.Name_2006.count(), df.ranking_2006.count()),
         (2007, df.Name_2007.count(), df.ranking_2007.count()),
         (2008, df.Name_2008.count(), df.ranking_2008.count()),
         (2010, df.Name_2010.count(), df.ranking_2010.count()),
         (2011, df.Name_2011.count(), df.ranking_2011.count()),
         (2012, df.Name_2012.count(), df.ranking_2012.count())]

def get_quitters(list):
    quitters = []
    for i in list:
        quitters.append((i[0],1-float(i[2])/i[1]))
    return quitters

quitters = get_quitters(quits)

# get overall averages, calculate mean and median in javascript.
speed_points = [(2005, df.total_2005.dropna().tolist(),
                 df.mtn_2005.dropna().tolist(), df.tt_2005.dropna().tolist()),
                (2006, df.total_2006.dropna().tolist(),
                 df.mtn_2006.dropna().tolist(), df.tt_2006.dropna().tolist()),
                (2007, df.total_2007.dropna().tolist(),
                 df.mtn_2007.dropna().tolist(), df.tt_2007.dropna().tolist()),
                (2008, df.total_2008.dropna().tolist(),
                 df.mtn_2008.dropna().tolist(), df.tt_2008.dropna().tolist()),
                (2010, df.total_2010.dropna().tolist(),
                 df.mtn_2010.dropna().tolist(), df.tt_2010.dropna().tolist()),
                (2011, df.total_2011.dropna().tolist(),
                 df.mtn_2011.dropna().tolist(), df.tt_2011.dropna().tolist()),
                (2012, df.total_2012.dropna().tolist(),
                 df.mtn_2012.dropna().tolist(), df.tt_2012.dropna().tolist()),
                ]