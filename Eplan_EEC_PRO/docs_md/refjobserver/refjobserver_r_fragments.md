---
title: "Fragments"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refjobserver_r_fragments.htm"
file: "refjobserver_r_fragments"
category: "refjobserver"
---

# Fragments

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Fragments A Job definition must not have a monolithic structure. Actions can be distributed onto multiple files, so-called Fragments that must each be integrated into the main Job definition by a corresponding [<xi:include>](refjobserver_r_xi_include.htm). [Example](javascript:void\(0\);)
    
        <?xml version="1.0" encoding="UTF-8"?>
    <jobdefinition name="testJob" model="\\localhost\JobServer\models\base.eox" xmlns:xi="http://www.w3.org/2001/XInclude">
    	<fileTrigger>
    		<failedFolder value="\\localhost\JobServer\failed" />
    		<incomingFolder value="\\localhost\JobServer\incoming" />
    		<outputFolder value="\\localhost\JobServer\success" />
    		<filter value="*.imx" />
    	</fileTrigger>
    	<actions>
    		<action name="Engineering.ImportIMXCommand" arguments="List{trigger.filePath}" />
    		<xi:include xmlns:xi="http://www.w3.org/2001/XInclude" href="includedJobDef.xml"/>
    	</actions>
    </jobdefinition>

[Example of a fragment](javascript:void\(0\);)
    
        <actions>
    	<action name="T_Ecad_Ui.UpdateExtensions" arguments="List{absRef('Feeder.Mechatronik')}"/>
    	<action name="Engineering.ExportPXCommand" arguments="List{'Feeder','\\\\localhost\\JobServer\\results\\Feeder.px',true}" />
    </actions>
