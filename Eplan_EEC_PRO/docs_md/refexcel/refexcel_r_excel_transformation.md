---
title: "Excel-Transformation"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refexcel_r_excel_transformation.htm"
file: "refexcel_r_excel_transformation"
category: "refexcel"
---

# Excel-Transformation

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Excel-Transformation The purpose of the Excel import is to create projects based on a modular system. The Excel files are not imported directly and therefore must be converted during the import with the help of a schema file into the IMX format that can be interpreted by EEC. Excel files are typically imported through the import wizard or an equivalent command. Schema files in XML and XSLT format can be used for converting into thee IMX format. The following section describe how a schema file in XML format is structured for the import of Excel files. For importing an Excel file, one schema file and one mapping file are always required. The mapping file is always the same for the examples in the following sections and therefore is only listed once here. [Example code of the mapping file](javascript:void\(0\);)  
      
        <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <mapping>
    						
    	<!-- T_Mechatronic_ModularSystem.Mechatronic.Actuators -->
    	<moTypeClass alias="Cylinder" realName="T_Mechatronic_ModularSystem.Mechatronic.Actuators.Cylinder"/>
    	<moTypeClass alias="Valve" realName="T_Mechatronic_ModularSystem.Mechatronic.Actuators.Valve"/>
    						
    	<!-- T_Mechatronic_ModularSystem.Mechatronic.Functiongroups -->
    	<moTypeClass alias="Discard" realName="T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Discard"/>
    	<moTypeClass alias="Insert" realName="T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Insert"/>
    	<moTypeClass alias="Inspect" realName="T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Inspect"/>
    	<moTypeClass alias="Move" realName="T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Move"/>
    	<moTypeClass alias="Store" realName="T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Store"/>
    						
    	<!-- T_Mechatronic_ModularSystem.Mechatronic.Functionunits -->
    	<moTypeClass alias="Axis" realName="T_Mechatronic_ModularSystem.Mechatronic.Functionunits.Axis"/>
    	<moTypeClass alias="Gripper" realName="T_Mechatronic_ModularSystem.Mechatronic.Functionunits.Gripper"/>
    	<moTypeClass alias="Orientationinspector" realName="T_Mechatronic_ModularSystem.Mechatronic.Functionunits.Orientationinspector"/>
    	<moTypeClass alias="Separator" realName="T_Mechatronic_ModularSystem.Mechatronic.Functionunits.Separator"/>
    	<moTypeClass alias="Stack" realName="T_Mechatronic_ModularSystem.Mechatronic.Functionunits.Stack"/>
    						
    	<!-- T_Mechatronic_ModularSystem.Mechatronic.Sensors -->
    	<moTypeClass alias="Positionsensor_inductive" realName="T_Mechatronic_ModularSystem.Mechatronic.Sensors.Positionsensor_inductive"/>
    	<moTypeClass alias="Positionsensor_optical" realName="T_Mechatronic_ModularSystem.Mechatronic.Sensors.Positionsensor_optical"/>
    	<moTypeClass alias="Pressuresensor" realName="T_Mechatronic_ModularSystem.Mechatronic.Sensors.Pressuresensor"/>
    						
    	<!-- T_Mechatronic_ModularSystem.Mechatronic.Stations -->
    	<moTypeClass alias="Feeder" realName="T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder"/>
    </mapping>

Read more
     * [Importing project data via wizard](eecbase_k_import_projectdata.htm)
     * [Engineering.ImportExcelCommand](refcommands_r_engineering_importexcelcommand.htm)
