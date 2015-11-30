
// User priority scale (1 - 5) 
var pPrice = 4;
var pArea = 3;
var pBed = 4;
var pSafety = 5;

var lim = 10;   // The number of entries shown in the initial Bubble chart
var color = ['#DF4949', '#E27A3F', '#EFC94C', '#9B59B6'];  
var labels = ['Price', 'Area', 'Bedrooms', 'Safety'];
var oR = 5;
var x = 0;
var y = 0;
//var json = data['data'];
// Sample JSON data returned from the database
var json = {'12345': { 'address': '123 Peachtree St, Atlanta, GA', 'price': 75000, 'area': 15000, 'bedrooms': 3, 'pScore': 5, 'aScore': 2, 'bScore': 3, 'sScore': 2, 'totScore': 51},
            '15234': { 'address': '213 Peachtree St, Atlanta, GA', 'price': 65000, 'area': 16000, 'bedrooms': 2, 'pScore': 5, 'aScore': 3, 'bScore': 4, 'sScore': 3, 'totScore': 62},
            '13524': { 'address': '312 Peachtree St, Atlanta, GA', 'price': 85000, 'area': 17000, 'bedrooms': 4, 'pScore': 4, 'aScore': 4, 'bScore': 1, 'sScore': 4, 'totScore': 52},
            '21345': { 'address': '456 Northside Dr, Atlanta, GA', 'price': 98000, 'area': 17000, 'bedrooms': 4, 'pScore': 3, 'aScore': 5, 'bScore': 2, 'sScore': 1, 'totScore': 46},
            '25341': { 'address': '546 Northside Dr, Atlanta, GA', 'price': 78000, 'area': 15000, 'bedrooms': 3, 'pScore': 5, 'aScore': 1, 'bScore': 5, 'sScore': 5, 'totScore': 68},
            '23145': { 'address': '645 Northside Dr, Atlanta, GA', 'price': 88000, 'area': 15000, 'bedrooms': 2, 'pScore': 3, 'aScore': 5, 'bScore': 4, 'sScore': 2, 'totScore': 57},
            '31245': { 'address': '789 Marietta St, Atlanta, GA', 'price': 77000, 'area': 15000, 'bedrooms': 1, 'pScore': 2, 'aScore': 4, 'bScore': 2, 'sScore': 3, 'totScore': 43},
            '35241': { 'address': '879 Marietta St, Atlanta, GA', 'price': 87000, 'area': 16000, 'bedrooms': 4, 'pScore': 3, 'aScore': 2, 'bScore': 5, 'sScore': 2, 'totScore': 49},
            '34215': { 'address': '987 Marietta St, Atlanta, GA', 'price': 97000, 'area': 16000, 'bedrooms': 2, 'pScore': 4, 'aScore': 3, 'bScore': 3, 'sScore': 4, 'totScore': 56},
            '41235': { 'address': '159 Atlantic Dr, Atlanta, GA', 'price': 76000, 'area': 18000, 'bedrooms': 3, 'pScore': 4, 'aScore': 5, 'bScore': 3, 'sScore': 2, 'totScore': 58},
            '43125': { 'address': '519 Atlantic Dr, Atlanta, GA', 'price': 86000, 'area': 19000, 'bedrooms': 2, 'pScore': 3, 'aScore': 1, 'bScore': 1, 'sScore': 1, 'totScore': 26},
            '45123': { 'address': '951 Atlantic Dr, Atlanta, GA', 'price': 96000, 'area': 16000, 'bedrooms': 2, 'pScore': 3, 'aScore': 2, 'bScore': 2, 'sScore': 1, 'totScore': 34},
            '51234': { 'address': '269 Cherry St, Atlanta, GA', 'price': 74000, 'area': 15000, 'bedrooms': 4, 'pScore': 2, 'aScore': 1, 'bScore': 1, 'sScore': 2, 'totScore': 24},
            '53124': { 'address': '692 Cherry St, Atlanta, GA', 'price': 84000, 'area': 15000, 'bedrooms': 2, 'pScore': 2, 'aScore': 1, 'bScore': 2, 'sScore': 1, 'totScore': 25},
            '52134': { 'address': '962 Cherry St, Atlanta, GA', 'price': 94000, 'area': 17000, 'bedrooms': 3, 'pScore': 2, 'aScore': 2, 'bScore': 1, 'sScore': 2, 'totScore': 28}};


/*
var priceScore = [ 5, 5, 4, 3, 5, 3, 2, 3, 4, 4 ];
var areaScore = [ 2, 3, 4, 5, 1, 5, 4, 2, 3, 5 ];
var bedScore = [ 3, 4, 1, 2, 5, 4, 2, 5, 3, 3 ];
var safetyScore = [ 2, 3, 4, 1, 5, 2, 3, 2, 4, 2 ];
var totScore = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ];

var numHouses = priceScore.length;
numFeats = 4;
//var totScore = pPrice*priceScore + pArea*areaScore + pBed*bedScore + pSafety*safetyScore;
for (var i = 0; i < numHouses; i++)
{
    totScore[i] = pPrice*priceScore[i] + pArea*areaScore[i] + pBed*bedScore[i] + pSafety*safetyScore[i];
}
//var totScore = [ 5, 10, 15, 20, 25 ];
*/

var w = 1000;
var h = 500;
var legendRectSize = 18;                                  
var legendSpacing = 4;                                

var svg = d3.select("#chart")
            .append("svg")
            .attr("width", w)
            .attr("height", h);

var legendContainer = svg.selectAll(".legend")
                         .style('left', '900px')
                         .style('top', '0px');
//legendContainer.append('rect');

var legend = legendContainer.data(color)  
                            .enter()
                            .append('g')                                             
                            .attr('transform', function(d, i) {                    
                                var height = legendRectSize + legendSpacing;     
                                var horz = w - legendRectSize - 200;                       
                                var vert = i * height;                    
                                return 'translate(' + horz + ',' + vert + ')';        
                            });                                                     

legend.append('rect')                                     
      .attr('width', legendRectSize)                      
      .attr('height', legendRectSize)                        
      .style('fill', function(d) {
            return d;
        })                                   
      .style('stroke', function(d) {
            return d;
        });                                
          
legend.append('text')                                     
      .attr('x', legendRectSize + legendSpacing)              
      .attr('y', legendRectSize - legendSpacing)             
      .text(function(d, i) { return labels[i]; }); 

/*
var bubble = d3.layout.pack()
               .size([h, h])
               .value(function(d) {return d.size;})
               .padding(5);

var nodesTop = bubble.nodes(processData(json, "top", lim))
                     .filter(function(d) { return !d.children; }); // filter out the outer bubble
var nodesRem = bubble.nodes(processData(json, "rem", lim))
                     .filter(function(d) { return !d.children; }); // filter out the outer bubble
*/
var nodes = processData(json, "top", lim);
var nodesTop = nodes.children; // filter out the outer bubble
nodes = processData(json, "rem", lim);
var nodesRem = nodes.children; // filter out the outer bubble
console.log(nodesTop);
console.log(nodesRem);
var radScale = d3.scale.linear()
               .domain([0, d3.max(nodesTop, function(d) { return d.size; })])
               .range([0, (w-10)/lim]);
var circles = svg.selectAll('circle')
                 .data(nodesTop)
                 .enter()
                 .append('circle')
                 .attr('cx', function(d, i)
                    {
                        d.x = i * w/lim + w/(2*lim);
                        return d.x;
                    })
                 .attr("cy", function(d)
                    {
                        d.y = h/3;
                        return d.y;
                    })
                 .attr("r", function(d) 
                    {
                        d.r = radScale(d.size/2)
                        return d.r;
                    })
                 .attr('class', function(d) { return d.className; })
                 /*
                 .attr("data-legend",function(d) 
                    { 
                        return d.className;
                    })
                 */
                 .on("mouseover", function(d)
                    {
                        //Update the tooltip position and value
                        d3.select("#tooltip")
                          .style("left", d.x + "px")
                          .style("top", d.y + "px")
                          .select("#value")
                          .html('<strong>Address:</strong> ' + json[d.name].address + '<br><strong>Price:</strong> $' + json[d.name].price + '<br><strong>Area:</strong> ' + json[d.name].price + 'sq.ft.<br><strong>Number of bedrooms:</strong> ' + json[d.name].bedrooms);

                        //Show the tooltip
                        d3.select("#tooltip").classed("hidden", false);
                    })
                 .on("mouseout", function() {
                        //Hide the tooltip
                        d3.select("#tooltip").classed("hidden", true);
                    })
                 .on("click", function(d, i) 
                    {
                        d3.select(this).transition()
                          .attr('transform', 'translate(' + 0 + ',' + 100 + ')') //.attr("x",320)
                          .duration(1000) // this is 1s 
                        d.y = d.y + 100;
                        x = d.x;
                        y = d.y;
                        showNewEntries(d.className); 
                    });


/*
var circles = svg.selectAll('circle')
                 .data(nodesTop)
                 .enter()
                 .append('circle')
                 .attr('transform', function(d) { return 'translate(' + d.x + ',' + d.y + ')'; })
                 .attr('r', function(d) { return d.r; })
                 .attr('class', function(d) { return d.className; })
                 .attr("data-legend",function(d) { return d.className})
                 .on("mouseover", function(d) {
                        //Update the tooltip position and value
                        d3.select("#tooltip")
                          .style("left", d.x + "px")
                          .style("top", d.y + "px")
                          .select("#value")
                          .html('<strong>Address:</strong> ' + json[d.name].address + '<br><strong>Price:</strong> $' + json[d.name].price + '<br><strong>Area:</strong> ' + json[d.name].price + 'sq.ft.<br><strong>Number of bedrooms:</strong> ' + json[d.name].bedrooms);

                        //Show the tooltip
                        d3.select("#tooltip").classed("hidden", false);
                    })
                 .on("mouseout", function() {
                        //Hide the tooltip
                        d3.select("#tooltip").classed("hidden", true);
                    })
                 .on("click", function(d, i) {
                        d3.select(this).transition()
                          .attr('transform', function() { return 'translate(500,500)'; }) //.attr("x",320)
                          .duration(1000) // this is 1s
                          .delay(100)     // this is 0.1s
                          
                 });

 
*/

/*
var opacityScale = d3.scale.linear()
                     .domain([0, d3.max(totScore, function(d) { return d; })])
                     .range([0, (w-10)/numHouses]);
*/

/*
var radScale = d3.scale.linear()
               .domain([0, d3.max(totScore, function(d) { return d; })])
               .range([0, (w-10)/numHouses]);

circlesTot.attr("cx", function(d, i)
        {
            return (i * w/numHouses + w/(2*numHouses));
        })
       .attr("cy", h/4)
       .attr("r", function(d) 
       {
            return radScale(d/2);
       });
var maxPrice = pPrice * Math.max.apply(Math, priceScore);
var maxArea = pArea * Math.max.apply(Math, areaScore);
var maxBed = pBed * Math.max.apply(Math, bedScore);
var maxSafety = pSafety * Math.max.apply(Math, safetyScore);
var arr;
var idx;
var maxVal;
var maxcheck = [];
var col = [];
var opa = [];
var colOpa = [];
for (var i = 0; i < numHouses; i++)
{
    arr = [pPrice*priceScore[i], pArea*areaScore[i], pBed*bedScore[i], pSafety*safetyScore[i]];
    maxVal = Math.max.apply(Math, arr);
    idx = arr.indexOf(Math.max.apply(Math, arr));
    switch (idx)
    {
        case 0:
            col.push("red");
            opa.push(maxVal/maxPrice);
            break;
        case 1:
            col.push("blue");
            opa.push(maxVal/maxArea);
            break;
        case 2:
            col.push("yellow");
            opa.push(maxVal/maxBed);
            break;
        case 3:
            col.push("green");
            opa.push(maxVal/maxSafety);
            break;
    }
}
var circlesCol = svg.selectAll("circle")
                 .data(col)
                 .attr("fill", function(d) { return d;});
var circlesOpa = svg.selectAll("circle")
                 .data(opa)
                 .attr("opacity", function(d) { return d;})
                 .on("click", function(d) {console.log(d);});
*/

function processData(data, choice, lim) 
{
    //var obj = data.countries_msg_vol;

    var newDataSet = [];
    var ct = 0;
    for(var prop in data) 
    {
        if (choice == 'top')
        {
            
            if (ct < lim)
                ct = ct + 1;
            else
                break;
            console.log(choice);
        }
        else if (choice == 'rem')
        {
            console.log(choice);
            ct = ct + 1;
            if (ct <= lim)
                continue;   
        }
        //console.log(prop);
        arr = [pPrice*data[prop].pScore, pArea*data[prop].aScore, pBed*data[prop].bScore, pSafety*data[prop].sScore];
        maxVal = Math.max.apply(Math, arr);
        idx = arr.indexOf(Math.max.apply(Math, arr));
        switch (idx)
        {
            case 0:
                newDataSet.push({name: prop, className: "price", size: data[prop].totScore, x: 0, y: 0, r: 0});
                //opa.push(maxVal/maxPrice);
                break;
            case 1:
                newDataSet.push({name: prop, className: "area", size: data[prop].totScore, x: 0, y: 0, r: 0});
                //opa.push(maxVal/maxArea);
                break;
            case 2:
                newDataSet.push({name: prop, className: "beds", size: data[prop].totScore, x: 0, y: 0, r: 0});
                //opa.push(maxVal/maxBed);
                break;
            case 3:
                newDataSet.push({name: prop, className: "safety", size: data[prop].totScore, x: 0, y: 0, r: 0});
                //opa.push(maxVal/maxSafety);
                break;
        }
        

    }
    //console.log(newDataSet);
    return {children: newDataSet};
}

function showNewEntries(tag)
{
    console.log(tag);
    var newEntries = [];
    console.log(nodesRem);
    var nw = w/3
    for (var node in nodesRem)
    {
        console.log(node);
        if (tag == nodesRem[node].className)
            newEntries.push(nodesRem[node]);
    }
    nlim = newEntries.length;
    var newCircles = svg.append('g')
                 .selectAll('circle')
                 .data(newEntries)
                 .enter()
                 .append('circle')
                 .attr('cx', function(d, i)
                    {
                        d.x = i * nw/nlim + nw/(2*nlim) + x - nw/2;
                        return d.x;
                    })
                 .attr("cy", function(d)
                    {
                        d.y = y + h/4;
                        return d.y;
                    })
                 .attr("r", function(d) 
                    {
                        d.r = radScale(d.size/2)
                        return d.r;
                    })
                 .attr('class', function(d) { return d.className; })
                 /*
                 .attr("data-legend",function(d) 
                    { 
                        return d.className;
                    })
                 */
                 .on("mouseover", function(d)
                    {
                        //Update the tooltip position and value
                        d3.select("#tooltip")
                          .style("left", d.x + "px")
                          .style("top", d.y + "px")
                          .select("#value")
                          .html('<strong>Address:</strong> ' + json[d.name].address + '<br><strong>Price:</strong> $' + json[d.name].price + '<br><strong>Area:</strong> ' + json[d.name].price + 'sq.ft.<br><strong>Number of bedrooms:</strong> ' + json[d.name].bedrooms);

                        //Show the tooltip
                        d3.select("#tooltip").classed("hidden", false);
                    })
                 .on("mouseout", function() {
                        //Hide the tooltip
                        d3.select("#tooltip").classed("hidden", true);
                    })
                 .on("click", function(d, i) 
                    {
                        d3.select(this).transition()
                          .attr('transform', 'translate(' + 0 + ',' + 100 + ')') //.attr("x",320)
                          .duration(1000) // this is 1s
                          .delay(100);     // this is 0.1s 
                        d.y = d.y + 100;
                        x = d.x;
                        y = d.y;
                    });
                 
} 
/* 
function activateBubble(d,i) 
{
    // increase this bubble and decrease others
    var t = d3.select(this).transition()
               .duration(350);
    t.attr('transform', 'translate(300,300)')
    
    t.attr("x", function(d,ii){
            if(i == ii) // Push Down
                return 300;//                
        })
     .attr("y", function(d,ii){
            if(i == ii) // Push Down
                return 300;//                
        })
    
     .attr("r", function(dd, ii) { 
            if(i == ii) // Make larger
                return dd.r+5;//
        });         
                  
}
*/ 

/*
var circlesPrice = svg.append("g").selectAll("circle")
                 .data(priceScore)
                 .enter()
                 .append("circle");
var radScale = d3.scale.linear()
               .domain([0, d3.max(priceScore, function(d) { return d; })])
               .range([0, (w-10)/numHouses]);

circlesPrice.attr("cx", function(d, i)
        {
            return (i * w/numHouses + w/(2*numHouses));
        })
       .attr("cy", 3*h/4)
       .attr("r", function(d) 
       {
            return radScale(d/2);
       });    
*/


