---
title: "Extending an IMX file in order to place components on placeholders and extension points"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutjobs_h_jobdef3.htm"
file: "tutjobs_h_jobdef3"
category: "tutjobs"
---

# Extending an IMX file in order to place components on placeholders and extension points

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Extending an IMX file in order to place components on placeholders and extension points Requirements:
     * EEC as a Job Server with Worker installation Version 2.5.1 or higher.
A configuration could be created successfully with the second Job definition. In it the Placeholder_Inspect was still empty. A component of the Inspect type is to be placed on this placeholder. The Inspect component contains an extension point for a component of the Orientationinspector type which in turn contains an extension point for a component of the Positionsensor_optical type. These extension points are to be updated in order to place the suitable components on it. Not the Job definition, but rather the IMX file to be imported is extended in order to place the Inspect component on the placeholder and the suitable components on the extension points. This means that the Job definition jobdef2.jmx can be used again. Proceed as follows to extend the existing IMX file:
    1. Create a copy of the existing IMX file T1_Project.imx called T3_Project.imx.
    2. Open the IMX file T3_Project.imx with any editor, for example Notepad++.
    3. Insert the following block instead of the line <mo name="Feeder" typeClass="T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder" />:
    
        <mo name="Feeder" typeClass="T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder" >
    	<mo name="Inspect" typeClass="T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Inspect" calcExtensions="AllLevels" />
    </mo>

    1. Save the IMX file.
The complete IMX file should have the following appearance: [Content of the T3_Project.imx:](javascript:void\(0\);)
    
        <?xml version="1.0" encoding="utf-8"?>
    <imx xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xi="http://www.w3.org/2001/XInclude" version="1.0">
    	<project name="Feeder" save="true" >
    		<libraries>
    			<add type="String" value="T_Mechatronic_ModularSystem"/>
    		</libraries>
    		<mo name="Feeder" typeClass="T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder" >
    			<mo name="Inspect" typeClass="T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Inspect" calcExtensions="AllLevels"/>
    		</mo>
    	</project>
    </imx>

    1. Continue with section [Test 3 - Creating a configuration with updated extension points](tutjobs_h_test3.htm).
