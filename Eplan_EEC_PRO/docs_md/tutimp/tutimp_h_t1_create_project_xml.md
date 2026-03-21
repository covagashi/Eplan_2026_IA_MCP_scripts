---
title: "Creating a configuration by importing an XML file"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutimp_h_t1_create_project_xml.htm"
file: "tutimp_h_t1_create_project_xml"
category: "tutimp"
---

# Creating a configuration by importing an XML file

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Creating a configuration by importing an XML file Requirements:
     * The preparatory steps on the file level have been carried out.
     * EEC is started.
     * In addition to the system libraries, the Library catalog contains the architecture T_Mechatronic_Architecture and the modular system T_Mechatronic_ModularSystem.
     * The **Feeder** project contains the Project catalog.
A new configuration with the name Feeder is to be generated which already exists, however. Therefore the existing configuration has to be removed first:
    1. In the Project catalog select the Feeder project.
    2. Click [Del].
The Delete dialog opens. The Feeder project is listed in it.
    1. Click [Finish].
The XML file T1_Project.xml is imported to create a new configuration on the basis of the modular system. To this purpose the scheme file XML_without_template.xsl is additionally required. [Contents of the T1_Project.xml](javascript:void\(0\);)
    
        <?xml version="1.0" encoding="utf-8"?>
    <mo name="Feeder" typeClass="T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder" >
    </mo>

Description of the XML file: After the obligatory header data in Row 1 a component of the Feeder type is added to the configuration in Row 2 with the tag <mo name="Feeder">. These specifications are converted internally to the IMX format that has the following contents:
    
        <?xml version="1.0" encoding="utf-8"?>  
    <imx xmlns:xi="http://www.w3.org/2001/XInclude" version="1.0">  
    	<project name="Feeder" save="true" >
    		<libraries>
    			<add type="String" value="T_Mechatronic_ModularSystem"/>
    		</libraries>
    		<mo name="Feeder" typeClass="T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder" />
    	</project>
    </imx>

This creates a new configuration.
    1. Select the menu item File > Import....
The import wizard opens with the Select page.
    1. Navigate to Project > Import.
    2. Confirm via [Next >].
The import wizard opens the page Import file.
    1. Specify the file T1_Project.xml in the Source file name field.
The file is located in the following directory:
    
        <EEC installation path>\resources\Import\XML

Use [Browse...] to navigate to the file. If applicable, select the file filter XML files (*.xml).
    1. Specify the file XML_without_template.xsl in the Scheme file name field.
The file is located in the following directory:
    
        <EEC installation path>\resources\Import\XSL

Use [Browse...] to navigate to the file.
    1. Leave the Template file name field empty.
    2. If applicable, mark the Create new project option and enter the name Feeder in field to the right of it.
    3. Confirm with [Finish].
Result: The new configuration called Feeder is displayed in the project catalog: The Feeder configuration contains the Feeder with the built-in components Insert, Move and Store. The Placeholder_Inspect placeholder remains empty.
