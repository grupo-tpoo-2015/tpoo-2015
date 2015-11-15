/*globals
    d3,
    tinycolor,
*/

var utils = (function () {

    'use strict';

    return {
        identityFunction: function (value) {
            return value;
        },
        buildColorScale: function (domain, range) {
            // TODO: find out if d3 has a mechanism for defining custom scales
            var fromColor = tinycolor(range[0]),
                toColor = tinycolor(range[1]),
                fromColorRGB = fromColor.toRgb(),
                toColorRGB = toColor.toRgb(),
                rScale = d3.scale.linear()
                           .domain(domain)
                           .range([fromColorRGB.r, toColorRGB.r]),
                gScale = d3.scale.linear()
                           .domain(domain)
                           .range([fromColorRGB.g, toColorRGB.g]),
                bScale = d3.scale.linear()
                           .domain(domain)
                           .range([fromColorRGB.b, toColorRGB.b]);

            return function (domainValue) {
                return "#" + tinycolor.fromRatio({
                    r: Math.round(rScale(domainValue)),
                    g: Math.round(gScale(domainValue)),
                    b: Math.round(bScale(domainValue))
                }).toHex();
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