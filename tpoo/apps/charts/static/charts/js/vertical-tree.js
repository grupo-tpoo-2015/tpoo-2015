/*globals
    d3,
*/

// adapted from http://www.codeproject.com/Tips/1021936/Creating-Vertical-Collapsible-Tree-With-d-js

var tree = (function () {

    'use strict';

    var svg, root,
        margin = { top: 40, right: 120, bottom: 20, left: 120 },
        width = 960 - margin.right - margin.left,
        height = 900 - margin.top - margin.bottom,

        i = 0,
        duration = 750,
        tree = d3.layout.tree().size([height, width]),
        diagonal = d3.svg.diagonal().projection(function (d) {
            return [d.x, d.y];
        });

    function update(source) {


        // Toggle children on click.
        function nodeclick(d) {
            if (d.children) {
                d._children = d.children;
                d.children = null;
            } else {
                d.children = d._children;
                d._children = null;
            }
            update(d);
        }


        // Compute the new tree layout.
        var nodes = tree.nodes(root).reverse(),
            links = tree.links(nodes),
            node,
            nodeEnter,
            nodeUpdate,
            nodeExit,
            link;
        // Normalize for fixed-depth.
        nodes.forEach(function (d) { d.y = d.depth * 100; });
        // Declare the nodes&hellip;
        node = svg.selectAll("g.node").data(nodes, function (d) {
            if (d.id === undefined) {
                i += 1;
                d.id = i;
            }
            return d.id;
        });
        // Enter the nodes.
        nodeEnter = node.enter().append("g")
            .attr("class", "node")
            .attr("transform", function () {
                return "translate(" + source.x + "," + source.y + ")";
            }).on("click", nodeclick);
        nodeEnter.append("circle").attr("r", 10)
            .attr("stroke", function (d) {
                return d.children || d._children ? "steelblue" : "#00c13f";
            })
            .style("fill", function (d) {
                return d.children || d._children ? "lightsteelblue" : "#fff";
            });
        //.attr("r", 10)
        //.style("fill", "#fff");
        nodeEnter.append("text")
            .attr("y", function (d) {
                return d.children || d._children ? -18 : 18;
            })
            .attr("dy", ".35em")
            .attr("text-anchor", "middle")
            .text(function (d) { return d.name; })
            .style("fill-opacity", 1e-6);
        // Transition nodes to their new position.
        //horizontal tree
        nodeUpdate = node.transition()
            .duration(duration)
            .attr("transform", function (d) {
                return "translate(" + d.x + "," + d.y + ")";
            });
        nodeUpdate.select("circle")
            .attr("r", 10)
            .style("fill", function (d) {
                return d._children ? "lightsteelblue" : "#fff";
            });
        nodeUpdate.select("text")
            .style("fill-opacity", 1);

        // Transition exiting nodes to the parent's new position.
        nodeExit = node.exit().transition()
            .duration(duration)
            .attr("transform", function () {
                return "translate(" + source.x + "," + source.y + ")";
            })
            .remove();
        nodeExit.select("circle").attr("r", 1e-6);
        nodeExit.select("text").style("fill-opacity", 1e-6);
        // Update the links&hellip;
        // Declare the links&hellip;
        link = svg.selectAll("path.link").data(links, function (d) { return d.target.id; });
        // Enter the links.
        link.enter().insert("path", "g").attr("class", "link")
            .attr("d", function () {
                var o = { x: source.x, y: source.y };
                return diagonal({ source: o, target: o });
            });
        // Transition links to their new position.
        link.transition()
            .duration(duration)
            .attr("d", diagonal);

        // Transition exiting nodes to the parent's new position.
        link.exit().transition()
            .duration(duration)
            .attr("d", function () {
                var o = { x: source.x, y: source.y };
                return diagonal({ source: o, target: o });
            })
            .remove();

        // Stash the old positions for transition.
        nodes.forEach(function (d) {
            d.x0 = d.x;
            d.y0 = d.y;
        });
    }

    return {
        draw: function (params) {

            svg = d3.select(params.svgSelector).append("svg")
                .attr("width", width + margin.right + margin.left)
                .attr("height", height + margin.top + margin.bottom)
                .append("g")
                .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

            root = params.data;

            update(params.data);
        }
    };

}());