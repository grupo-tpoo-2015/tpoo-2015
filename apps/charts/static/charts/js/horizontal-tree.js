/*globals
    window,
    d3,
    jQuery,
*/

// adapted from https://mohansun-canvas.herokuapp.com/content/training/

/*
    This module, given a set of data and a DOM selector, draws a tree inside the <svg> tag denoted
    by that selector. The set of data must follow the following structure:

        * A "name" field is mandatory. Determines the content of the label that will be displayed
        next to the node

    {
        name: "Hello, I'm a tree, bla bla bla bla...",
        full_name: ""Hello, I'm a tree, bla bla bla bla bla bla bla bla bla bla",

    }

*/

var tree = (function ($) {

    'use strict';

    var nextId = 1,
        margin = {
            left: 70,
            top: 20,
            right: 100,
            bottom: 20,
        },

        outerWidth,
        outerHeight = 800,
        width,
        height = outerHeight - margin.top - margin.bottom,

        duration = 750,
        root,

        tree = d3.layout.tree().size([height, width]),

        diagonal = d3.svg.diagonal().projection(function (d) { return [d.y, d.x]; }),

        svg;

    function update(source) {

        // Toggle children on click.
        function click(d) {
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
        var i,
            accum,
            nodes = tree.nodes(root).reverse(),
            links = tree.links(nodes),
            node,
            nodeEnter,
            nodeUpdate,
            nodeExit,
            link,
            distanceByDepth = [
                150,
                180,
                100,
                180,
                200,
                80,
                150,
            ];

        accum = 0;
        for (i = 0; i < distanceByDepth.length; i += 1) {
            accum += distanceByDepth[i];
            distanceByDepth[i] = accum - distanceByDepth[i];
        }

        // Normalize for fixed-depth.
        nodes.forEach(function (d) {
            d.y = distanceByDepth[d.depth];
        });

        // Update the nodesâ€¦
        node = svg.selectAll("g.node")
            .data(nodes, function (d) {
                if (d.id === undefined) {
                    d.id = nextId;
                    nextId += 1;
                }
                return d.id;
            });

        // Enter any new nodes at the parent's previous position.
        nodeEnter = node.enter().append("g")
            .attr("class", function (d) {
                return ["node"].concat(d.extra_classes || []).join(" ");
            })
            .attr("transform", function () { return "translate(" + source.y0 + "," + source.x0 + ")"; })
            .on("click", click);

        nodeEnter.append("circle")
            .attr("r", 1e-6)
            .style("fill", function (d) { return d._children ? "#ccff99" : "#fff"; });

        nodeEnter.append("text")
            .attr("x", function (d) { return d.children || d._children ? -13 : 13; })
            .attr("dy", ".35em")
            .attr("text-anchor", function (d) { return d.children || d._children ? "end" : "start"; })
            .text(function (d) { return d.name; })
            .style("fill-opacity", 1e-6)
            .attr("class", function (d) {
                if (d.url !== null) { return 'hyper'; }
            })
            .on("click", function (d) {
                var embed;
                $('.hyper').attr('style', 'font-weight:normal');
                d3.select(this).attr('style', 'font-weight:bold');
                if (d.url !== null) {
                    //  window.location=d.url;
                    $('#vid').remove();

                    embed = $('<embed>')
                        .attr('id', 'vid')
                        .attr('src', d.url + "?version=3&amp;hl=en_US&amp;rel=0&amp;autohide=1&amp;autoplay=1")
                        .attr('wmode', "transparent")
                        .attr('type', "application/x-shockwave-flash")
                        .attr('width', "100%")
                        .attr('height', "100%")
                        .attr('allowfullscreen', "true")
                        .attr('title', d.name);

                    $('#vid-container').append(embed);
                }
            })
            .append('title').text(function (d) {
                return d.full_name || d.name;
            });

        // Transition nodes to their new position.
        nodeUpdate = node.transition()
            .duration(duration)
            .attr("transform", function (d) { return "translate(" + d.y + "," + d.x + ")"; });

        nodeUpdate.select("circle")
            .attr("r", 10)
            .style("fill", function (d) { return d._children ? "#ccff99" : "#fff"; });

        nodeUpdate.select("text")
            .style("fill-opacity", 1);

        // Transition exiting nodes to the parent's new position.
        nodeExit = node.exit().transition()
            .duration(duration)
            .attr("transform", function () { return "translate(" + source.y + "," + source.x + ")"; })
            .remove();

        nodeExit.select("circle")
            .attr("r", 1e-6);

        nodeExit.select("text")
            .style("fill-opacity", 1e-6);

        // Update the linksâ€¦
        link = svg.selectAll("path.link")
            .data(links, function (d) { return d.target.id; });

        // Enter any new links at the parent's previous position.
        link.enter().insert("path", "g")
            .attr("class", "link")
            .attr("d", function () {
                var o = {x: source.x0, y: source.y0};
                return diagonal({source: o, target: o});
            });

        // Transition links to their new position.
        link.transition()
            .duration(duration)
            .attr("d", diagonal);

        // Transition exiting nodes to the parent's new position.
        link.exit().transition()
            .duration(duration)
            .attr("d", function () {
                var o = {x: source.x, y: source.y};
                return diagonal({source: o, target: o});
            })
            .remove();

        // Stash the old positions for transition.
        nodes.forEach(function (d) {
            d.x0 = d.x;
            d.y0 = d.y;
        });
    }

    function abbreviateNodeNames(node) {
        var i, children, maxLen = 30;
        if (node.name.length > maxLen) {
            node.full_name = node.name;
            node.name = node.name.substring(0, maxLen - 3) + "...";
        }
        children = node.children || node._children || [];
        for (i = 0; i < children.length; i += 1) {
            abbreviateNodeNames(children[i]);
        }
    }

    return {
        draw: function (params) {

            root = params.data;
            abbreviateNodeNames(root);
            root.x0 = height / 2;
            root.y0 = 0;

            svg = d3.select(params.svgSelector)
                .attr("height", outerHeight)
                .append("g")
                .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

            outerWidth = svg.node().getBoundingClientRect().width;
            width = outerWidth - margin.right - margin.left;

            update(root);
            d3.select(window.frameElement).style("height", outerHeight + "px");

        }
    };

}(jQuery));