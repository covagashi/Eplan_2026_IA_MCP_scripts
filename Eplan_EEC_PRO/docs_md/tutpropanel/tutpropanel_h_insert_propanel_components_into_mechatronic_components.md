---
title: "Installing Pro Panel components in mechatronic components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutpropanel_h_insert_propanel_components_into_mechatronic_components.htm"
file: "tutpropanel_h_insert_propanel_components_into_mechatronic_components"
category: "tutpropanel"
---

# Installing Pro Panel components in mechatronic components

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Installing Pro Panel components in mechatronic components In the following steps the discipline components are to be installed in the mechatronic components in the way they can be structurally assigned.
     * Discipline components for the mechanical basic structure as well as the power supply, PLC and end terminal blocks are installed in the Station Feeder.
     * Digital input cards are in installed in the Functionunits which also contain sensors.
     * Terminal clamps are installed in the sensors.
Install discipline components for the mechanical basic structure in the Feeder station:
    1. Open the Feeder component in the T_Mechatronic_ModularSystem library.
    1. Drag and drop each of the components into the component editor once: Schematic, LayoutSpace, AE1050_500, AE1050_500_MountingPanel and MP_Plane_Front.
    2. Drag the KK3060 component into the component area twice and rename the resulting components KK3060Left and KK3060Right.
    3. Drag the KK3040 component into the component area three times and rename the resulting components KK3040Top, KK3040Middle and KK3040Bottom.
    4. Drag the TS35_7_5 component into the component area twice and rename the resulting components TS35_7_5Top and TS35_7_5Bottom.
    5. Drag the PowerSupply_PXC_2938581 and PXC_IL_PB_DP components into the component editor.
    6. Drag the EndBracket_PxC_3022276 component four times into the component editor.
    7. Drag the Terminal_PXC_3031212 component into the component editor three times and rename the resulting components L1, N and PE.
The arrows  und  may be used to move the installed components to the correct position. Install digital inputs cards into the Functionunits Axis, Gripper, Orientationinspector, Separator and Stack:
    1. Open the Axis mechatronic component.
    2. Drag the PxC_IL_24_DI component twice into the component editor.
Result: If the Feeder station is installed without the components Inspect and Discard (Option_Inspect_available=false), two positions for the X-Axis are omitted. In this case only one digital input card is necessary. Specify a formula for the Disabler for the digital input card PxC_IL_24_DI2.
    1. Select the installed PxC_IL_24_DI2 discipline component.
    2. Enter the following formula in the Disabled field:
    
        =not(mc.mos('Sensor').size > 2)

With mc.mos('Sensor') this formula creates a collection of all sensors, which are installed in the parent components (Axis) and which are active. If the number of components of this collection is larger than 2 (.size > 2), the installed component should not be disabled (not()). Install the digital input card into other mechatronic components.
    1. Open the mechatronic Gripper component.
    2. Drag the PxC_IL_24_DI component once into the component editor.
    3. Result:
    4. Repeat steps 3 and 4 with the mechatronic components Orientationinspector, Separator and Stack.
Install terminal clamps into the sensors:
    1. Open the Positionsensor_inductive mechatronic component.
    2. Drag the Terminal_PxC_3031212 component three times into the component editor.
    3. Name the installed components as follows:
Old name | New name  
---|---  
Terminal_PxC_3031212 | X1L+  
Terminal_PxC_30312122 | X1M1  
Terminal_PxC_30312123 | Input  
  5. Result:
    1. Repeat the steps 1 to 3 for the Positionsensor_optical component.
    2. Open the Pressuresensor mechatronic component.
    3. Drag the Terminal_PxC_3031212 component twice into the component editor.
    4. Name the installed components as follows:
Old name | New name  
---|---  
Terminal_PxC_3031212 | X1L+  
Terminal_PxC_30312122 | Input  
Result:
    1. All discipline components are installed in mechatronic components.
