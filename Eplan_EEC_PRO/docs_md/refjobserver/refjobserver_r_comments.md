---
title: "Comments"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refjobserver_r_comments.htm"
file: "refjobserver_r_comments"
category: "refjobserver"
---

# Comments

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Comments For very large job definitions, it is helpful to document parts of the file with comments. Comments always start with <!-- and end with \-->. In between may lie a few comments, but also entire program sections. [Example code for a comment line](javascript:void\(0\);)  
      
        <!--This is a comment line -->

[Example code for a commented-out program block](javascript:void\(0\);)
    
        <jobdefinition name="'testJob_' + trigger.fileName" model="C:Users\public\EPLAN\base.eox " xmlns:xi="http://www.w3.org/2001/XInclude">
    	<actions>
    		<action name="Engineering.ImportIMXCommand" arguments="List{'project.imx'}" />
    		<action name="T_Ecad_Ui.UpdateExtensions" arguments=" absRef('Feeder.Mechatronic')"/>
    		<!--The next action is disabled by comment
    		<action name="Engineering.ImportIMXCommand" arguments="List{'project2.imx'}" />
    		-->
    		<xi:include xmlns:xi="http://www.w3.org/2001/XInclude" href="includedJobDef.xml"/>
    	</actions>
    </jobdefinition>
