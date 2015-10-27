/*globals
    d3,
*/

var stackedBarChart = (function () {

    'use strict';

    function getAndScale() {
        var args = arguments,
            scale = args[0];
        return function (obj) {
            var i,
                attr,
                data = obj;
            for (i = 1; i < args.length; i += 1) {
                attr = args[i];
                if (typeof attr === "string" && attr.slice(-2) === '()') {
                    data = data[attr.slice(0, -2)]();
                } else {
                    data = data[attr];
                }

            }
            return scale(data);
        };
    }

    function drawBarChart(data) {

        var svg,
            width,
            height,
            max_value,
            paddingTop = 50,
            gapBetweenStacks = 2,
            stacks,
            bars,
            legend,
            legendItems,
            identityFunction = function (x) {return x; },
            barWidth,
            heightScale,
            colors,
            xScale,
            yScale;

        svg = d3.select('svg')
            .style('border', 'solid black')
            .style('margin', '10px');

        width = svg.node().getBoundingClientRect().width;
        height = svg.node().getBoundingClientRect().height;


        barWidth = ((width + gapBetweenStacks) / data.stacks.length) - gapBetweenStacks;


        max_value = d3.max(data.stacks, function (stack) {
            return d3.sum(stack, function (bar) {
                return bar;
            });
        }) + paddingTop;

        colors = [
            "#174C79",
            "#2C7286",
            "#92CE82",
        ];
        xScale = d3.scale.linear()
                   .domain([0, data.stacks.length])
                   .range([0, width + gapBetweenStacks]);

        yScale = d3.scale.linear()
                   .domain([0, max_value])
                   .range([height, paddingTop]);

        heightScale = d3.scale.linear()
                        .domain([0, max_value])
                        .range([0, height - paddingTop]);

        svg.append('text')
            .attr('x', 5).attr('y', 20)
            .attr('text-anchor', 'start')
            .text(data.title);

        /*jslint unparam: true */
        legend = svg.append('g').classed('legend', true);

        legendItems = legend.selectAll('.legend-item').data(data.legends).enter()
            .append('g')
            .classed('legend-item', true);

        legendItems.append('text').text(identityFunction)
            .attr('y', function (text, i) {return 70 - 20 * i; })
            .attr('x', width - 100);

        legendItems.append('rect').text(identityFunction)
            .attr('y', function (text, i) {return 70 - 10 - 20 * i; })
            .attr('x', width - 120)
            .attr('fill', function (text, i) {return colors[i % colors.length]; })
            .attr('width', 10)
            .attr('height', 10);

        stacks = svg.selectAll('.stack').data(data.stacks).enter()
                    .append('g')
                    .classed('stack', true);


        bars = stacks.selectAll('.bar').data(identityFunction).enter()
            .append('g')
            .classed('bar', true);

        bars.append('rect')
            .attr('x', function (bar, barIndex, stackIndex) {
                return xScale(stackIndex);
            })
            .attr('y', function (bar, barIndex, stackIndex) {
                var k, accum = 0;
                for (k = 0; k <= barIndex; k += 1) {
                    accum += data.stacks[stackIndex][k];
                }
                return yScale(accum);
            })
            .attr('height', heightScale)
            .attr('width', barWidth)
            .attr('fill', function (bar, barIndex) {
                return colors[barIndex % colors.length];
            })
            .append('title').text(function (bar) {
                return bar + ' seg';
            });
        /*jslint unparam: false */

    }

    return {
        init: function (params) {
            drawBarChart(params.dataset);
        }
    };

}());