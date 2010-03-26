#!/bin/zsh
dot -Tsvg -o doorsensors_nodes.svg doorsensors_nodes.dot
circo -Tsvg -o doorsensors_nodes_legend.svg doorsensors_nodes_legend.dot
dot -Tsvg -o doorsensors_nodes_legend2.svg doorsensors_nodes_legend2.dot
circo -LC22 -Tsvg -o doorsensors_nodes_circo.svg doorsensors_nodes.dot
