var margin = {top: 20, right: 15, bottom: 60, left: 60},
    width = 600 - margin.left - margin.right,
    height = 450 - margin.top - margin.bottom;

d3.csv("../static/tdf.csv", function(csv){
          var x = d3.scale.linear().domain([2004, 2013]).range([60, width-20]),
              y = d3.scale.linear().domain([34, 60]).range([height-20, 20]);

          var svg = d3.select("body").append("svg")
                                     .attr("width", width)
                                     .attr("height", height);

          var xAxis = d3.svg.axis().scale(x).orient('bottom')
                        .ticks(7).tickFormat(function(d,i) {
                        if (d>2004 && d<2013) {return d ;}}),
              yAxis = d3.svg.axis().scale(y).orient('left');

          var med_2005 = d3.median(csv, function(d) {if (d.Year==2005) {return +d.Tt;} }),
              med_2006 = d3.median(csv, function(d) {if (d.Year==2006) {return +d.Tt;} }),
              med_2007 = d3.median(csv, function(d) {if (d.Year==2007) {return +d.Tt;} }),
              med_2008 = d3.median(csv, function(d) {if (d.Year==2008) {return +d.Tt;} }),
              med_2010 = d3.median(csv, function(d) {if (d.Year==2010) {return +d.Tt;} }),
              med_2011 = d3.median(csv, function(d) {if (d.Year==2011) {return +d.Tt;} }),
              med_2012 = d3.median(csv, function(d) {if (d.Year==2012) {return +d.Tt;} });

          svg.selectAll("circle").data(csv).enter()
             .append("circle")
             .attr("cx", function(d) {if (+d.Tt>0) {return x(+d.Year);}})
             .attr("cy", function(d) {if (+d.Tt>0) {return y(+d.Tt);}})
             .attr("r", function(d) {if (+d.Tt>0) {return 3;}})
             .style("opacity", 0.1);
          
          svg.append("g")
             .attr("class", "axis")
             .attr("transform", "translate(0, "+(height-20)+")")
             .call(xAxis);
 
          svg.append("g")
             .attr("class", "axis")
             .attr("transform", "translate(" + margin.left + "," + 0 + ")")
             .call(yAxis);
          
          svg.append("line")
             .attr("x1", x(2004.75))
             .attr("x2", x(2005.25))
             .attr("y1", y(med_2005))
             .attr("y2", y(med_2005))
             .style("stroke", "red")
             .style("stroke-width", 2);

          svg.append("line")
             .attr("x1", x(2005.75))
             .attr("x2", x(2006.25))
             .attr("y1", y(med_2006))
             .attr("y2", y(med_2006))
             .style("stroke", "red")
             .style("stroke-width", 2);

          svg.append("line")
             .attr("x1", x(2006.75))
             .attr("x2", x(2007.25))
             .attr("y1", y(med_2007))
             .attr("y2", y(med_2007))
             .style("stroke", "red")
             .style("stroke-width", 2);

          svg.append("line")
             .attr("x1", x(2007.75))
             .attr("x2", x(2008.25))
             .attr("y1", y(med_2008))
             .attr("y2", y(med_2008))
             .style("stroke", "red")
             .style("stroke-width", 2);

          svg.append("line")
             .attr("x1", x(2009.75))
             .attr("x2", x(2010.25))
             .attr("y1", y(med_2010))
             .attr("y2", y(med_2010))
             .style("stroke", "red")
             .style("stroke-width", 2);

          svg.append("line")
             .attr("x1", x(2010.75))
             .attr("x2", x(2011.25))
             .attr("y1", y(med_2011))
             .attr("y2", y(med_2011))
             .style("stroke", "red")
             .style("stroke-width", 2);

          svg.append("line")
             .attr("x1", x(2011.75))
             .attr("x2", x(2012.25))
             .attr("y1", y(med_2012))
             .attr("y2", y(med_2012))
             .style("stroke", "red")
             .style("stroke-width", 2);

       });