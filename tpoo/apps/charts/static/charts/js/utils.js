/*globals
    d3,
*/

var utils = (function () {

    'use strict';

    return {
        identityFunction: function (value) {
            return value;
        },
        buildColorScale: function (domain, range) {
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
        },
        getAndScale: function () {
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
    };
}());