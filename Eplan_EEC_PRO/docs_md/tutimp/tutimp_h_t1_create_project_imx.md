---
title: "Creating a configuration by importing an IMX file"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutimp_h_t1_create_project_imx.htm"
file: "tutimp_h_t1_create_project_imx"
category: "tutimp"
---

# Creating a configuration by importing an IMX file

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Creating a configuration by importing an IMX file Requirements:
     * The preparatory steps on the file level have been carried out.
     * EEC is started.
     * In addition to the system libraries, the Library catalog contains the architecture T_Mechatronic_Architecture and the modular system T_Mechatronic_ModularSystem.
     * The **Feeder** project contains the Project catalog.
A new configuration with the name Feeder is to be generated which already exists, however. Therefore the existing configuration has to be removed first:
    1. In the Project catalog select the Feeder project.
    2. Click [Del].
The Delete dialog opens. The Feeder project is listed in it.
    1. Click [Finish].
The IMX file T1_Project.imx is imported to create a new configuration on the basis of the modular system. [Contents of the T1_Project.imx](javascript:void\(0\);)
    
        <?xml version="1.0" encoding="utf-8"?>
    <imx xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xi="http://www.w3.org/2001/XInclude" version="1.0">
    	<project name="Feeder" save="true" >
    		<libraries>
    			<add type="String" value="T_Mechatronic_ModularSystem"/>
    		</libraries>
    		<mo name="Feeder" typeClass="T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder" />
    	</project>
    </imx>

Description of the IMX file: After the obligatory header data in Rows 1 and 2, the name of the new configuration is specified in Row 3 with the attribute name of the <project> tag on Feeder. Since the import wizard requires the specification of a project name, this specification is overridden by the import wizard. The save attribute with the value true determines that this configuration is saved immediately after creation. This tag is only effective if importing is carried out via action / command. The <libraries> tag encompasses the specification on which mechatronical modular system the configuration is based. With the <mo name="Feeder"> tag a component of the Feeder type is added to the configuration. This creates a new configuration.
    1. Select the menu item File > Import....
The import wizard opens with the Select page.
    1. Navigate to Project > Import.
    2. Confirm via [Next >].
The import wizard opens the page Import file.
    1. Specify the file T1_Project.imx in the Source file name field.
The file is located in the following directory:
    
        <EEC installation path>\resources\Import\IMX

Use [Browse...] to navigate to the file. If applicable, select the file filter IMX files (*.imx).
    1. Leave the Template file name field empty.
    2. If applicable, mark the Create new project option and enter the name Feeder in field to the right of it.
    3. Confirm with [Finish].
Result: The new configuration called Feeder is displayed in the project catalog: The Feeder configuration contains the Feeder with the built-in components Insert, Move and Store. The new aspect of this configuration is that a placeholder for components of the type Inspect is installed in Feeder. The Discard component is disabled and does not become active until a component of the type Inspect is installed on the placeholder.
