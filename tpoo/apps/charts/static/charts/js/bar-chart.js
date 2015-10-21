/*globals
    d3,
*/

var barChart = (function () {

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

    function colorScale(domain, range) {
        // TODO: find out if d3 has a mechanism for defining custom scales
        var rScale = d3.scale.linear()
                       .domain(domain)
                       .range([range[0][0], range[1][0]]),
            gScale = d3.scale.linear()
                       .domain(domain)
                       .range([range[0][1], range[1][2]]),
            bScale = d3.scale.linear()
                       .domain(domain)
                       .range([range[0][2], range[1][2]]);
        return function (domainValue) {
            return 'rgb(' + [
                Math.round(rScale(domainValue)),
                Math.round(gScale(domainValue)),
                Math.round(bScale(domainValue)),
            ].join(', ') + ')';
        };
    }


    function drawBarChart(options) {

        var svg,
            width,
            height,
            max_value,
            paddingTop = 10,
            gapBetweenBars = 2,
            g,
            barWidth,
            heightScale,
            colorGradientScale,
            xScale,
            yScale;

        svg = d3.select('svg')
            .style('border', 'solid black')
            .style('margin', '10px');

        width = svg.node().getBoundingClientRect().width;
        height = svg.node().getBoundingClientRect().height;
        width = 600;


        barWidth = ((width + gapBetweenBars) / options.bars.length) - gapBetweenBars;


        max_value = d3.max(options.bars, function (obj) {
            return obj.value;
        }) + paddingTop;

        // TODO: if would be so much better if instead of using 3 elemen lists, colors could be
        // defined using different color notations like rgb, hex, color names, etc
        colorGradientScale = colorScale([0, max_value], [[10, 75, 60], [255, 75, 60]]);

        xScale = d3.scale.linear()
                   .domain([0, options.bars.length])
                   .range([0, width + gapBetweenBars]);

        yScale = d3.scale.linear()
                   .domain([0, max_value])
                   .range([height - 25, 25]);

        heightScale = d3.scale.linear()
                        .domain([0, max_value])
                        .range([25, height - 25]);


        g = svg.selectAll('g')
            .data(options.bars)
            .enter()
            .append('g');

        svg.append('text')
            .attr('x', 5).attr('y', 20)
            .attr('text-anchor', 'start')
            .text(options.title);

        /*jslint unparam: true */
        g.append('rect')
            .attr('x', function (obj, i) {
                return xScale(i);
            })
            .attr('y', getAndScale(yScale, 'value'))
            .attr('height', getAndScale(heightScale, 'value'))
            .attr('width', barWidth)
            .attr('fill', function (obj, i) {
                return colorGradientScale(obj.value);
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