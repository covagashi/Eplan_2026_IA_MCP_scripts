---
title: "Placing a component on a placeholder by importing an XML file"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutimp_h_t2_placeholder_xml_inst.htm"
file: "tutimp_h_t2_placeholder_xml_inst"
category: "tutimp"
---

# Placing a component on a placeholder by importing an XML file

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Placing a component on a placeholder by importing an XML file Requirements:
     * The preparatory steps on the file level have been carried out.
     * EEC is started.
     * In addition to the system libraries, the Library catalog contains the architecture T_Mechatronic_Architecture and the modular system T_Mechatronic_ModularSystem.
     * The **Feeder** project contains the Project catalog.
     * Section [Creating a configuration by importing an XML file](tutimp_h_t1_create_project_xml.htm) is carried out.
The XML file T2_Component.imx is imported in order to install a component in the existing configuration. [Content of the T2_Component.xml](javascript:void\(0\);)
    
        <?xml version="1.0" encoding="utf-8"?>
    <mo name="Feeder" typeClass="T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder" >
    	<mo name="Inspect" typeClass="T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Inspect"/>
    </mo>

Description of the XML file: With the <mo name="Feeder"> tag a component of the Feeder type of the configuration is addressed. In the addressed component the <mo name="Inspect"> tag is used to place a component of the Inspect type on a suitable placeholder. These specifications are converted internally to the IMX format that has the following contents:
    
        <?xml version="1.0" encoding="utf-8"?>
    <imx xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xi="http://www.w3.org/2001/XInclude" version="1.0">
    	<project name="Feeder" save="true" >
    		<libraries>
    			<add type="String" value="T_Mechatronic_ModularSystem"/>
    		</libraries>
    		<mo name="Feeder" typeClass="T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder" >
    			<mo name="Inspect" typeClass="T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Inspect" />
    		</mo>
    	</project>
    </imx>

Proceed as follows to install a component on a placeholder:
    1. Select the menu item File > Import....
The import wizard opens with the Select page.
    1. Navigate to Project > Import.
    2. Confirm via [Next >].
The import wizard opens the page Import file.
    1. Specify the file T2_Component.xml in the Source file name field.
The file is located in the following directory:
    
        <EEC installation path>\resources\Import\XML

Use [Browse...] to navigate to the file. If applicable, select the file filter XML files (*.xml).
    1. Specify the file XML_without_template.xsl in the Scheme file name field.
The file is located in the following directory:
    
        <EEC installation path>\resources\Import\XSL

Use [Browse...] to navigate to the file.
    1. Leave the Template file name field empty.
    2. Remove the Create new project option and mark the Feeder project in the list below it.
    3. Confirm with [Finish].
Result: The new configuration called Feeder is displayed in the project catalog: The Feeder configuration contains the Feeder with the built-in components Insert, Move and Store. The new aspect of this configuration is that the Inspect component is placed on the placeholder Placeholder_Inspect in Feeder. In the Inspect component the previously fixed installed component Orientationinspector has been replaced by the ExtensionPoint_Orientationinspector extension point. The Discard component is thus active and is also displayed. Note The display of placeholders, extension points and of components that are deactivated is influenced by the filter setting of the project catalog (see [Filter](eecbase_k_filter.htm)).
