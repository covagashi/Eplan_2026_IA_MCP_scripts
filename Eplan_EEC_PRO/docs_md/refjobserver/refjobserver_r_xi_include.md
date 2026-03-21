---
title: "\u003cxi:include\u003e"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refjobserver_r_xi_include.htm"
file: "refjobserver_r_xi_include"
category: "refjobserver"
---

# \u003cxi:include\u003e

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  <xi:include> Job definition The <xi:include> tag inserts the specified job definition file into the job definition at this location. The definition file can be specified by different methods:  
     * A relative URI, for example href="JobDefinition.jmx" or href="test/JobDefinition.jmx " or href="../output/test/JobDefinition.jmx ".
A relative URI always references the path of the job definition file.
     * An absolute URI, for example href="file:///c:/Users/test/JobDefinition.jmx".
In this case the correct notation file:/// with three flashes must be observed. The inserted job definition file must be well-formed. The tag has no sub-elements. Attribute | Usage | Values | Default value | Description  
---|---|---|---|---  
href | required |  |  | Absolute name of the XML file to insert  
xmlns:xi | required if not specified in the <jobdefinition> tag | http://www.w3.org/2001/XInclude |  | Namespace extension to facilitate use of xi:include  
[Example of a job definition that uses xi:include](javascript:void\(0\);)
    
        <?xml version="1.0" encoding="UTF-8"?>
    <jobdefinition name="'testJob_' + trigger.fileName" model="C:Users\public\EPLAN\base.eox"
    successMailRecipients="Me@MyCompany.com,MyDepartmentManager@MyCompany.com"
    failedMailRecipients="Me@MyCompany.com,MyDepartmentManager@MyCompany.com">
    	<actions>
    		<action name="Engineering.ImportIMXCommand" arguments="List{'project.imx'}" />
    		<action name="Engineering.ImportIMXCommand" arguments="List{'project2.imx'}" />
    		<action name="Engineering.ImportIMXCommand" arguments="List{'project3.imx'}" />
    		<xi:include xmlns:xi="http://www.w3.org/2001/XInclude" href="includedJobDef.xml"/>
    	</actions>
    </jobdefinition>

[Example of a job definition to be inserted](javascript:void\(0\);)
    
        <actions>
    	<action name="T_Ecad_Ui.UpdateExtensions" arguments="List{absRef('Feeder.Mechatronic')}"/>
    	<action name="T_Ecad_Ui.UpdateExtensions" arguments="List{absRef('Feeder2.Mechatronic')}"/>
    	<action name="T_Ecad_Ui.UpdateExtensions" arguments="List{absRef('Feeder3.Mechatronic')}"/>
    <actions>
