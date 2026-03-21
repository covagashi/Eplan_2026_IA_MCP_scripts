---
title: "Representation of the connections"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutgraph2d_h_connections_configuration_representation.htm"
file: "tutgraph2d_h_connections_configuration_representation"
category: "tutgraph2d"
---

# Representation of the connections

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Representation of the connections The representation of a connection comprises the attributes line thickness, line style, line color, decorator of start of line and end of line and which text is to be displayed as a tooltip.
    1. Below the node with id=âLAN_Referenceâ, insert the following lines.
        
                <!-- Connection of Worker to Device -->
        <connection
         id="Worker_Path" reference="Worker_Reference" router="Bendpoint"
        width="2" style="1" color="0,255,0" sourceDeco="empty" targetDeco="empty"
        tooltip="=if not src.$Name.isNull 
        		then src.$Name
        		else 
        			if not src.$Number.isNull 
        				then src.$Number 
        				else 'Enter data' 
        			endif 
        	endif 
        	+ ' | ' + 
        			if not (target.$Name.isNull) 
        				then target.$Name 
        				else 
        					if not (target.$Number.isNull) 
        						then target.$Number 
        						else 'Enter data' 
        					endif 
        			endif" />
        <!-- Connection of Slave to Slave -->
        <connection
        	id="LAN_Path" reference="LAN_Reference"
        	width="2"
        	style="1"
        	color="255,0,0"
        	sourceDeco="empty"
        	targetDeco="empty"
        	tooltip="=src.getName() + ' of ' + 
        			if not src.mc.$Name.isNull 
        				then src.mc.$Name
        				else 
        					if not src.mc.$Number.isNull 
        						then src.mc.$Number
        						else 'Enter data'
        					endif
        			endif
        			 + ' | ' + target.getName() + ' of ' + 
        			if not target.mc.$Name.isNull 
        				then target.mc.$Name
        				else 
        					if not target.mc.$Number.isNull 
        						then target.mc.$Number
        						else 'Enter data'
        					endif
        			endif" />

    2. Save the diagram configuration ([Ctrl] \+ [S]).
[Explanation](javascript:void\(0\);) The ID of the first connection is Worker_Path. The ID of the second connection is LAN_Path. The first connection references the configuration of the reference between persons and devices with the attribute reference="Worker_Referenceâ. The second connection references the configuration of the reference between devices among themselves with the attribute reference="LAN_Reference". The attributes width="2", style="1", color="0,255,0", sourceDeco="empty" and targetDeco="empty" represent the connections with a thickness of 2 points as a solid line in green color without any special end-of-line symbols. The formula in the attribute tooltip="=if not src.$Name.isNull then src.$Name else if not src.$Number.isNull then src.$Nummer else 'Enter data' endif endif + ' | ' + if not (target.$Name.isNull) then target.$Name else if not (target.$Number.isNull) then target.$Number else 'Enter data' endif endif" determines the value of the parameter Name or Number of the source and target component of a connection, to display this data as a tooltip. If both the parameters are <null> then as a replacement, the text Enter data is displayed as a tooltip. The second connection distinguishes itself, in principle, from the first only because of the router, the line color and the formula for determining the parameter values for the tooltip, because here, it is necessary to first navigate from the in-built component to the parent component, to evaluate the parameter Name or Number there.
