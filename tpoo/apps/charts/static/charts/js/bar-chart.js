/*globals
    d3,
    utils,
*/

var barChart = (function () {

    'use strict';


    function drawBarChart(dataset) {

        var svg,
            width,
            height,
            max_value,
            paddingTop = 10,
            gapBetweenBars = 2,
            g,
            barWidth,
            heightScale,
            colorScale,
            xScale,
            yScale;

        svg = d3.select('svg')
            .style('border', 'solid black')
            .style('margin', '10px');

        width = svg.node().getBoundingClientRect().width;
        height = svg.node().getBoundingClientRect().height;
        width = 600;


        barWidth = ((width + gapBetweenBars) / dataset.data.length) - gapBetweenBars;


        max_value = d3.max(dataset.data, function (obj) {
            return obj.value;
        }) + paddingTop;

        colorScale = utils.buildColorScale([0, max_value], ['rgb(10, 75, 60)', 'rgb(255, 75, 60)']);

        xScale = d3.scale.linear()
                   .domain([0, dataset.data.length])
                   .range([0, width + gapBetweenBars]);

        yScale = d3.scale.linear()
                   .domain([0, max_value])
                   .range([height - 25, 25]);

        heightScale = d3.scale.linear()
                        .domain([0, max_value])
                        .range([25, height - 25]);


        g = svg.selectAll('g')
            .data(dataset.data)
            .enter()
            .append('g')
            .classed('bar', true);

        svg.append('text')
            .attr('x', 5).attr('y', 20)
            .attr('text-anchor', 'start')
            .text(dataset.title);

        /*jslint unparam: true */
        g.append('rect')
            .attr('x', function (obj, i) {
                return xScale(i);
            })
            .attr('y', utils.getAndScale(yScale, 'value'))
            .attr('height', utils.getAndScale(heightScale, 'value'))
            .attr('width', barWidth)
            .attr('fill', function (obj, i) {
                return colorScale(obj.value);
            })
            .append('title').text(function (obj) {
                return obj.name;
            });

        g.append('text')
            .attr('x', function (obj, i) {
                return xScale(i) + barWidth / 2;
            })
            .attr('y', function (obj) {
                return yScale(obj.value) + 20;
            })
            .attr('width', barWidth)
            .text(function (obj) {
                return obj.value.toFixed(2);
            });

        g.append('text')
            .attr('x', function (obj, i) {
                return xScale(i) + barWidth / 2;
            })
            .attr('y', function (obj) {
                return yScale(obj.value) + 35;
            })
            .attr('width', barWidth)
            .text('seg');
        /*jslint unparam: false */
    }

    return {
        init: function (params) {
            drawBarChart(params.dataset);
        }
    };

}());