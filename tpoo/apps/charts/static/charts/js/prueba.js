/*globals
    d3,
*/



var tuto = function () {

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
                if (attr.slice(-2) === '()') {
                    data = data[attr.slice(0, -2)]();
                } else {
                    data = data[attr];
                }

            }
            return scale(data);
        };
    }

    function randomFloat(min, max) {
        return Math.random() * (max - min) + min;
    }

    function generateDataSet(min_amount, max_amount) {
        var i, amount, obj = {
            participantName: 'Juan Carlos Batman',
            timesPerTask: [],
        };

        amount = randomFloat(min_amount, max_amount);

        for (i = 1; i <= amount; i += 1) {
            obj.timesPerTask.push({
                taskName: "Tarea #" + i,
                time: randomFloat(10, 100),
            });
        }

        return obj;
    }


    function drawSvgBarChart(user) {

        var svg,
            width = 600,
            height = 400,
            max_time,
            padding = 2,
            g,
            barWidth,
            heightScale,
            colorScale,
            yScale;

        barWidth = (width + 2 * padding) / user.timesPerTask.length;

        max_time = d3.max(user.timesPerTask, function (obj) {
            return obj.time;
        }) + 10;

        colorScale = d3.scale.linear()
                   .domain([0, max_time])
                   .range([10, 255]);

        yScale = d3.scale.linear()
                   .domain([0, max_time])
                   .range([height, 0]);


        heightScale = d3.scale.linear()
                        .domain([0, max_time])
                        .range([0, height]);

        svg = d3.select('body').append('svg')
            .attr('width', width)
            .attr('height', height)
            .style('border', 'solid black')
            .style('margin', '10px');

        g = svg.selectAll('g')
            .data(user.timesPerTask)
            .enter()
            .append('g');

        svg.append('text')
            .attr('x', 5).attr('y', 20)
            .attr('text-anchor', 'start')
            .text('Tareas realizadas por el participante ' + user.participantName);

        g.append('rect')
            .attr('x', function (obj, i) {
                return i * barWidth;
            })
            .attr('y', getAndScale(yScale, 'time'))
            .attr('height', getAndScale(heightScale, 'time'))
            .attr('width', barWidth - padding)
            .attr('fill', function (obj, i) {
                return 'rgb(' + Math.round(colorScale(obj.time)) + ', 75, 60)';
            })
            .append('title').text(function (obj) {
                return obj.taskName;
            });

        g.append('text')
            .attr('x', function (obj, i) {
                return i * barWidth + barWidth / 2;
            })
            .attr('y', function (obj) {
                return yScale(obj.time) + 20;
            })
            .attr('height', getAndScale(heightScale, 'time'))
            .attr('width', barWidth - padding)
            .text(function (obj) {
                return obj.time.toFixed(2);
            });

        g.append('text')
            .attr('x', function (obj, i) {
                return i * barWidth + barWidth / 2;
            })
            .attr('y', function (obj) {
                return yScale(obj.time) + 35;
            })
            .attr('height', getAndScale(heightScale, 'time'))
            .attr('width', barWidth - padding)
            .text(function (obj) {
                return 'seg';
            });
    }

    drawSvgBarChart(generateDataSet(10, 15));

};

tuto();

