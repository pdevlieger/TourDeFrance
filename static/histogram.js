var quitters = [[2005, 0.17989417989417988], [2006, 0.21022727272727271],
            [2007, 0.25396825396825395], [2008, 0.18994413407821231],
            [2010, 0.13705583756345174], [2011, 0.15656565656565657],
            [2012, 0.22727272727272729]];
            
var margin = {top: 20, right: 15, bottom: 60, left: 60};
var w = 960 - margin.left - margin.right;
var h = 220 - margin.top - margin.bottom;

var svg = d3.select("body")
            .append("svg")
            .attr("width", w)
            .attr("height", h);

svg.selectAll("rect")
   .data(quitters)
   .enter()
   .append("rect")
   .attr("x", function(d, i) { return i*60 + 20 ;})
   .attr("y", function(d, i) { return h - 25 - d[1]*400 ;})
   .attr("width", 40)
   .attr("height", function(d, i) { return d[1]*400 ;})
   .attr("fill", "gold");
       
function precise_round(num,decimals){
         return Math.round(num*Math.pow(10,decimals))/Math.pow(10,decimals);};

svg.selectAll("text")
   .data(quitters)
   .enter()
   .append("text")
   .text(function(d) { return precise_round(d[1]*100,2)+"%";})
   .attr("x", function(d, i) { return i*60 + 40;})
   .attr("y", function(d, i) { return h - 15 - d[1]*400})
   .attr("text-anchor", "middle")
   .attr("fill", "red");

svg.selectAll("text_axis")
   .data(quitters)
   .enter()
   .append("text")
   .text(function(d) { return d[0] ;})
   .attr("x", function(d, i) { return i*60 + 40;})
   .attr("y", 130)
   .attr("text-anchor", "middle")
   .attr("fill", "black")
   .attr("stroke-width", "3px");