/*globals
    d3,
    utils,
*/

var stackedBarChart = (function () {

    'use strict';

    function drawBarChart(dataset) {

        var svg,
            width,
            height,
            max_value,
            paddingTop = dataset.legends.length * 35,
            gapBetweenStacks = 2,
            stacks,
            bars,
            legend,
            legendItems,
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


        barWidth = ((width + gapBetweenStacks) / dataset.items.length) - gapBetweenStacks;


        max_value = d3.max(dataset.items, function (stack) {
            return d3.sum(stack.values);
        }) + paddingTop;

        colors = [
            // "#174C79",
            "#2C7286",
            "#92CE82",
        ];
        xScale = d3.scale.linear()
                   .domain([0, dataset.items.length])
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
            .text(dataset.title);

        /*jslint unparam: true */
        legend = svg.append('g').classed('legend', true);

        legendItems = legend.selectAll('.legend-item').data(dataset.legends).enter()
            .append('g')
            .classed('legend-item', true);

        legendItems.append('text').text(utils.identityFunction)
            .attr('y', function (text, i) {return 15 + 20 * (dataset.legends.length - i); })
            .attr('x', width - 170);

        legendItems.append('rect').text(utils.identityFunction)
            .attr('y', function (text, i) {return 15 + 20 * (dataset.legends.length - i) - 10; })
            .attr('x', width - 170 - 15)
            .attr('fill', function (text, i) {return colors[i % colors.length]; })
            .attr('width', 10)
            .attr('height', 10);

        stacks = svg.selectAll('.stack')
            .data(dataset.items).enter()
            .append('g')
            .classed('stack', true);

        bars = stacks.selectAll('.bar')
            .data(function (d) {return d.values; }).enter()
            .append('g')
            .classed('bar', true);

        function calculateY(bar, barIndex, stackIndex) {
            var k, accum = 0;
            for (k = 0; k <= barIndex; k += 1) {
                accum += dataset.items[stackIndex].values[k];
            }
            return yScale(accum);
        }

        bars.append('rect')
            .attr('x', function (bar, barIndex, stackIndex) {
                return xScale(stackIndex);
            })
            .attr('y', calculateY)
            .attr('height', heightScale)
            .attr('width', barWidth)
            .attr('fill', function (bar, barIndex) {
                return colors[barIndex % colors.length];
            })
            .append('title').text(function (bar, barIndex, stackIndex) {
                return dataset.items[stackIndex].name;
            });

        function addTextToBars(marginTop, text) {
            bars.append('text')
                .attr('x', function (bar, barIndex, stackIndex) {
                    return xScale(stackIndex) + barWidth / 2;
                })
                .attr('height', heightScale)
                .attr('y', function (bar, barIndex, stackIndex) {
                    return calculateY(bar, barIndex, stackIndex) + marginTop;
                })
                .attr('width', barWidth)
                .text(text);
        }
        addTextToBars(20, function (value) {
            return value.toFixed(2);
        });
        addTextToBars(35, 'segs');
        /*jslint unparam: false */

    }

    return {
        init: function (params) {
            drawBarChart(params.dataset);
        }
    };

}());