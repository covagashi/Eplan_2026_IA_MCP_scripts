---
title: "Checking the representation of the connections"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutgraph2d_h_test6_check_representation_of_connections.htm"
file: "tutgraph2d_h_test6_check_representation_of_connections"
category: "tutgraph2d"
---

# Checking the representation of the connections

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Checking the representation of the connections A check should be carried out whether the connections between persons and devices, as well as between devices among one another, are all depicted correctly. At the same time, the correct display of the tooltips can be determined.
    1. In the Project Catalog, open the diagram IT_SolutionMap with a double-click.
All the connections are shown in the correct colors and along the shortest distance between the nodes of the diagram.
    1. Position the mouse pointer over the connection of Telephone 101 to 2wayLANJack 10404001.
The tooltip displays the following text: 1 of 101 | 1 of 10404001. The number 1 is the name of the in-built component of type LAN_Jack. The number 101 is the direct dial extension of the telephone and the number 10404001 is the number of the 2-X LAN-socket. According to the configuration, the connections between persons and devices are polylines and the following test will show that the straight connections can be changed into inflected connections (see the following figure, point 1).
    1. Select a connection, for example, the one between the person Jack Johnson and the telephone 101.
A bend point (2) is shown in the middle of the selected connection. If the mouse pointer is positioned over the bend point, the appearance of the mouse pointer (3) changes. This symbolizes that this bend point can now be moved. Every new straight line that is created gets a bend point in the middle, so that polylines that can be bent as many times as desired are obtained. Tip To simplify the alignment of the nodes and edges (connections), a grid can be displayed with the menu option View > Merge into grid.
    1. Close the diagram without saving the changes.
