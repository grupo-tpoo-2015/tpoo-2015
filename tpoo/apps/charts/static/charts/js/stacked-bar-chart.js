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
            paddingTop = 10,
            gapBetweenStacks = 2,
            g,
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
                return bar.value;
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

        g = svg.selectAll('g')
            .data(data.stacks)
            .enter()
            .append('g');

        svg.append('text')
            .attr('x', 5).attr('y', 20)
            .attr('text-anchor', 'start')
            .text(data.title);

        /*jslint unparam: true */
        g.selectAll('rect').data(function (d) {return d; }).enter()
            .append('rect')
            .attr('x', function (bar, i, j) {
                return xScale(j);
            })
            .attr('y', function (bar, i, j) {
                var k, accum = 0;
                for (k = 0; k <= i; k += 1) {
                    accum += data.stacks[j][k].value;
                }
                return yScale(accum);
            })
            .attr('height', function (bar) {return heightScale(bar.value); })
            .attr('width', barWidth)
            .attr('fill', function (obj, i) {
                return colors[i % colors.length];
            })
            .append('title').text(function (obj) {
                return obj.name;
            });

        g.selectAll('text').data(function (d) {return d; }).enter()
            .append('text')
            .attr('x', function (obj, i, j) {
                return xScale(j) + barWidth / 2;
            })
            .attr('y', function (obj, i, j) {
                var k, accum = 0;
                for (k = 0; k <= i; k += 1) {
                    accum += data.stacks[j][k].value;
                }
                return yScale(accum) + 20;
            })
            .attr('width', barWidth)
            .text(function (obj) {
                return obj.value.toFixed(2);
            });

        // g.append('text')
        //     .attr('x', function (obj, i, j) {
        //         return xScale(j) + barWidth / 2;
        //     })
        //     .attr('y', function (obj) {
        //         return yScale(obj.value) + 35;
        //     })
        //     .attr('width', barWidth)
        //     .text('seg');
        /*jslint unparam: false */
    }

    return {
        init: function (params) {
            drawBarChart(params.dataset);
        }
    };

}());