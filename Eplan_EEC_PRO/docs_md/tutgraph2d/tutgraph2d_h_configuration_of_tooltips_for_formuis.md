---
title: "Configuring tooltips for displaying Form-UIs"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutgraph2d_h_configuration_of_tooltips_for_formuis.htm"
file: "tutgraph2d_h_configuration_of_tooltips_for_formuis"
category: "tutgraph2d"
---

# Configuring tooltips for displaying Form-UIs

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Configuring tooltips for displaying Form-UIs The configuration of the nodes is to be extended in such a way that a Form-UI is displayed as a tooltip in a manner suitable for the node. In the Form-UIs, parameter values of the project component can be changed. The diagram editor must be enhanced with this functionality:  
    1. In the tag <diagramEditor> insert the attribute xmlns:formui="http://www.mind8.com/Diagram/Formui".
The configuration of the node for Floor is expanded as follows:
    1. Below the tag <figurePolygon>, insert the following lines.
    
        <configuration>
    	<editRequestHandler xsi:type="formui:formui-handler" />
    	<editRequestHandlerInfo xsi:type="formui:formui-handler-info" refId="GSD" showMenu="true" />
    </configuration>

[Explanation:](javascript:void\(0\);) The configuration of a node is expanded with <configuration>. Here, <editRequestHandler xsi:type="formui:formui-handler"> is used to expand the node by the function for executing a call for a Form-UI Handler.  
The tag <editRequestHandlerInfo xsi:type="formui:formui-handler-info" refId="GSD" /> is used to give the function the information for accessing the Form-UI with the ID GSD. Expanding the configuration of the node Room:
    1. Below the tag <figurePolygon>, insert the following lines.
    
        <configuration>
    	<editRequestHandler xsi:type="formui:formui-handler" />
    	<editRequestHandlerInfo xsi:type="formui:formui-handler-info" refId="RD" />
    </configuration>

The configuration of the node Component is expanded by these lines:
    1. Below the tag <figureImage>, insert the following lines.
    
        <configuration>
    	<editRequestHandler xsi:type="formui:formui-handler" />
    	<editRequestHandlerInfo xsi:type="formui:formui-handler-info" refId="Data" resizable="true" movable="true" showMenu="true" />
    </configuration>

    1. Save the diagram configuration ([Ctrl] \+ [S]).
[Explanation:](javascript:void\(0\);) The Form-UI for the devices is somewhat bigger than that for floor and room, owing to which it has to be possible to change the size of this overlay window, as well as to move it, by using the attributes resizable="true" and movable="true".  
The display of the window menu is activated with the attribute showMenu="true".
