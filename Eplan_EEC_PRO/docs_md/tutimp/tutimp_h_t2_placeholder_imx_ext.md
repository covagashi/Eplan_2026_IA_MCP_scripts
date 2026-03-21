---
title: "Placing components on an extension point by importing an IMX file"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutimp_h_t2_placeholder_imx_ext.htm"
file: "tutimp_h_t2_placeholder_imx_ext"
category: "tutimp"
---

# Placing components on an extension point by importing an IMX file

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Placing components on an extension point by importing an IMX file Requirements:
     * The preparatory steps on the file level have been carried out.
     * EEC is started.
     * In addition to the system libraries, the Library catalog contains the architecture T_Mechatronic_Architecture and the modular system T_Mechatronic_ModularSystem.
     * The **Feeder** project contains the Project catalog.
     * Section [Creating a configuration by importing an IMX file](tutimp_h_t1_create_project_imx.htm) is carried out.
In order to place one or more components on an extension point in the existing configuration the IMX files T2_Extension_OneLevel.imx and T2_Extension_AllLevels.imx are imported. [Contents of the T2_Extension_OneLevel.imx](javascript:void\(0\);)
    
        <?xml version="1.0" encoding="utf-8"?>
    <imx xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xi="http://www.w3.org/2001/XInclude" version="1.0">
    	<project name="Feeder" save="true" >
    		<libraries>
    			<add type="String" value="T_Mechatronic_ModularSystem"/>
    		</libraries>
    		<mo name="Feeder" typeClass="T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder" >
    			<mo name="Inspect" typeClass="T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Inspect" calcExtensions="OneLevel"/>
    		</mo>
    	</project>
    </imx>

Description of the IMX file: After the obligatory header data in Rows 1 and 2, the name of the new configuration is specified in Row 3 with the attribute name of the <project> tag on Feeder. Since the import wizard requires the specification of a project name, this specification is overridden by the import wizard. The save attribute with the value true determines that this configuration is saved immediately after creation. This tag is only effective if importing is carried out via action / command. The <libraries> tag encompasses the specification on which mechatronical modular system the configuration is based. With the <mo name="Feeder"> tag a component of the Feeder type of the configuration is addressed. In the addressed component the <mo name="Inspect"> tag is used to place a component of the Inspect type on a suitable placeholder. The calcExtensions="OneLevel" attribute has the effect that the extension point that is installed in the Inspect component is updated. This means that a suitable component is placed on this extension point. [Contents of the T2_Extension_AllLevel.imx](javascript:void\(0\);)
    
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

Description of the IMX file: After the obligatory header data in Rows 1 and 2, the name of the new configuration is specified in Row 3 with the attribute name of the <project> tag on Feeder. Since the import wizard requires the specification of a project name, this specification is overridden by the import wizard. The save attribute with the value true determines that this configuration is saved immediately after creation. This tag is only effective if importing is carried out via action / command. The <libraries> tag encompasses the specification on which mechatronical modular system the configuration is based. With the <mo name="Feeder"> tag a component of the Feeder type of the configuration is addressed. In the addressed component the <mo name="Inspect"> tag is used to place a component of the Inspect type on a suitable placeholder. The calcExtensions="AllLevel" attribute has the effect that the extension point that is installed in the Inspect component is updated and all those located under it. This means that a suitable component is placed on this extension point and all suitable components located under it. Proceed as follows to place a component on an extension point of the subordinate level:
    1. Select the menu item File > Import....
The import wizard opens with the Select page.
    1. Navigate to Project > Import.
    2. Confirm via [Next >].
The import wizard opens the page Import file.
    1. Specify the file T2_Extension_OneLevel.imx in the Source file name field.
The file is located in the following directory:
    
        <EEC installation path>\resources\Import\IMX

Use [Browse...] to navigate to the file. If applicable, select the file filter IMX files (*.imx).
    1. Leave the Template file name field empty.
    2. Remove the Create new project option and mark the Feeder project in the list below it.
    3. Confirm with [Finish].
Result: The new configuration called Feeder is displayed in the project catalog: The Feeder configuration contains the Feeder with the built-in components Insert, Move and Store. The new aspect of this configuration is that the Inspect component is placed on the placeholder Placeholder_Inspect in Feeder. In the Inspect component the previously fixed installed component Orientationinspector is now placed on the ExtensionPoint_Orientationinspector extension point. The Orientationinspector component also has an extension point installed. However, no component has been placed on it. The Discard component is thus active and is also displayed. Note The display of placeholders, extension points and of components that are deactivated is influenced by the filter setting of the project catalog (see [Filter](eecbase_k_filter.htm)). Proceed as follows to install components on extension points of all the subordinate levels: In order to use the existing Feeder project the installed Inspect component has to be initially removed first:
    1. Mark the Inspect component in the Project catalog.
    2. Delete the component using the [Del] key.
    3. Confirm the selection with [Finish] in the Delete dialog.
After the Inspect component has been removed from the project the import can be started:
    1. Select the menu item File > Import....
The import wizard opens with the Select page.
    2. Navigate to Project > Import.
    3. Confirm via [Next >].
The import wizard opens the page Import file.
    4. Specify the file T2_Extension_AllLevel.imx in the Source file name field.
The file is located in the following directory:
        
                C:\Users\Public\EPLAN\EngineeringConfiguration\<Build-ID>\resources\Import\IMX

Use [Browse...] to navigate to the file. If applicable, select the file filter IMX files (*.imx).
    5. Leave the Template file name field empty.
    6. Remove the Create new project option and mark the Feeder project in the list below it.
    7. Confirm with [Finish].
Result: The new configuration called Feeder is displayed in the project catalog: The Feeder configuration contains the Feeder with the built-in components Insert, Move and Store. The new aspect of this configuration is that the Inspect component is installed on the placeholder Placeholder_Inspect in Feeder. In the Inspect component the previously fixed installed component Orientationinspector is now placed on the ExtensionPoint_Orientationinspector extension point. The component Positionsensor_optical is placed on the extension point ExtentionPoint_Positionsensor_optical of the Orientationinspector component. The Discard component is thus active and is also displayed.
