
    // User priority scale (1 - 5) 
var pPrice = 4;
var pArea = 3;
var pBed = 4;
var pSafety = 5;

/*
var json2 = {"countries_msg_vol": {
    "CA": 170, "US": 393, "BB": 12, "CU": 9, "BR": 89, "MX": 192, "PY": 32, "UY": 9, "VE": 25, "BG": 42, "CZ": 12, "HU": 7, "RU": 184, "FI": 42, "GB": 162, "IT": 87, "ES": 65, "FR": 42, "DE": 102, "NL": 12, "CN": 92, "JP": 65, "KR": 87, "TW": 9, "IN": 98, "SG": 32, "ID": 4, "MY": 7, "VN": 8, "AU": 129, "NZ": 65, "GU": 11, "EG": 18, "LY": 4, "ZA": 76, "A1": 2, "Other": 254 
  }};
*/

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
var h = 600;
var svg = d3.select("#chart")
            .append("svg")
            .attr("width", w)
            .attr("height", h);

var bubble = d3.layout.pack()
               .size([h, h])
               .value(function(d) {return d.size;})
               .padding(3);

var nodes = bubble.nodes(processData(json))
                  .filter(function(d) { return !d.children; }); // filter out the outer bubble

console.log(nodes); 

var circles = svg.selectAll('circle')
                 .data(nodes)
                 .enter()
                 .append('circle')
                 .attr('transform', function(d) { console.log(d.x); return 'translate(' + d.x + ',' + d.y + ')'; })
                 .attr('r', function(d) { return d.r; })
                 .attr('class', function(d) { console.log(d.className); return d.className; })
                 .on("mouseover", tooltip(d))
                 .on("mouseout", function() {
                        //Hide the tooltip
                        d3.select("#tooltip").classed("hidden", true);
                    });

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

function processData(data) 
{
    //var obj = data.countries_msg_vol;

    var newDataSet = [];

    for(var prop in data) 
    {
        //console.log(prop);
        arr = [pPrice*data[prop].pScore, pArea*data[prop].aScore, pBed*data[prop].bScore, pSafety*data[prop].sScore];
        maxVal = Math.max.apply(Math, arr);
        idx = arr.indexOf(Math.max.apply(Math, arr));
        switch (idx)
        {
            case 0:
                newDataSet.push({name: prop, className: "price", size: data[prop].totScore});
                // col.push("red");
                //opa.push(maxVal/maxPrice);
                break;
            case 1:
                newDataSet.push({name: prop, className: "area", size: data[prop].totScore});
                //col.push("blue");
                //opa.push(maxVal/maxArea);
                break;
            case 2:
                newDataSet.push({name: prop, className: "beds", size: data[prop].totScore});
                //col.push("yellow");
                //opa.push(maxVal/maxBed);
                break;
            case 3:
                newDataSet.push({name: prop, className: "safety", size: data[prop].totScore});
                //col.push("green");
                //opa.push(maxVal/maxSafety);
                break;
        }
        

    }
    //console.log(newDataSet);
    return {children: newDataSet};
}
function tooltip(data)
{
    var xPosition = parseFloat(d3.select(this).attr("x")) + xScale.rangeBand() / 2;
    var yPosition = parseFloat(d3.select(this).attr("y")) / 2 + h / 2;

    //Update the tooltip position and value
    d3.select("#tooltip")
      .style("left", xPosition + "px")
      .style("top", yPosition + "px")
      .select("#value")
      .text(d);

    //Show the tooltip
    d3.select("#tooltip").classed("hidden", false);
} 

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


