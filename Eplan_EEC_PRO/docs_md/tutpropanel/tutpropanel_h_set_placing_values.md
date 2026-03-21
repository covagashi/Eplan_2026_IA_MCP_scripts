---
title: "Entering values for placement"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutpropanel_h_set_placing_values.htm"
file: "tutpropanel_h_set_placing_values"
category: "tutpropanel"
---

# Entering values for placement

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Entering values for placement [Preliminary considerations regarding the placement of the discipline components](javascript:void\(0\);) The Mounting panel with zero points diagram shows both the null points and the handles for the parts that are positioned using a coordinate.
     * The zero point (x=0, y=0, z=0) of the mounting panel is located in the lower left corner.
     * The handles of the cable ducts and mounting rails are mainly located in the lower left corner. The coordinate specification for the position of these parts refers to the distance from the zero point on the mounting panel to the handle. A part is rotated around this handle (cable ducts KK3060Left and KK3060Right by 90 degrees).
     * The electrical items and terminal clamps are mounted on the mounting rails. The coordinate specification for the position of these parts no longer refers to the distance from the zero point on the mounting panel to the handle, but from the start of the center line on the mounting rail (line mate) to the handle.
Enter the coordinate specifications for the placement of the cable ducts and mounting rails:
    1. Open the Feeder station.
    2. For the following installed components enter the values for the Coordinate parameter:
Component | Parameter | Value  
---|---|---  
KK3060Left | Coordinate | =List{60.0,25.0}  
KK3060Right | Coordinate | =List{449.0,25.0}  
KK3040Top | Coordinate | =List{60.0,405.0}  
KK3040Middle | Coordinate | =List{60.0,195.0}  
KK3040Bottom | Coordinate | =List{60.0,25.0}  
TS35_7_5Top | Coordinate | =List{60.0,302.5}  
TS35_7_5Bottom | Coordinate | =List{60.0,112.5}  
The components that are positioned on the mounting rails should maintain a gap of 20.0 mm from the left edge. Furthermore, a gap the width of the PLC should be maintained between the terminal block with line voltage and the terminal block of the sensor connection points. The ordering of the endblocks and terminal clamps also has to be entered here.
    1. Open the Feeder library component.
    2. Open the installed PowerSupply_PxC_2938581 component.
    3. For the Coordinate parameter, enter the value =List{20,0}.
    4. Open the installed EndBracket_PxC_3022276 component.
    5. For the Coordinate parameter, enter the value =List{20,0}.
    6. For the Position parameter, enter the value 100.
    7. Repeat step 6 for the L1, N, PE and EndBracket_PxC_30222762components.
    8. Open the installed EndBracket_PxC_30222763 component.
    9. For the Position parameter, enter the value 200.
    10. Enter the following formula for the Mate parameter:
    
        =List{'M4','M2', mc.mos('T_Mechatronic_ModularSystem.ECAD.ProPanel.PxC_IL_PB_DP').select(x|x.parameter('EPN').value='PXC.2862246').first.parameter('Width').value}

    1. Open the installed EndBracket_PxC_30222764 component.
    2. For the Position parameter, enter the value 400.
Explanation of the formula: The parameter Mate describes a placement relative to the parent component. Here the distance from the left terminal group to the right terminal group is to be determined. This corresponds to the width of the PLC CPU. The arguments are supplied as a list via List{âSource handle','Destination mounting pointâ,Distance}. The M4 argument is the left handle of the component to be positioned and M2 is the right mounting point of the parent component. The formula uses mc to determine the superordinate mechatronic component and creates a collection of all components that correspond to the type in the bracket (PxC_IL_PB_DP) via mos('T_Mechatronic_ModularSystem.ECAD.ProPanel.PxC_IL_PB_DP'). This collection is searched via select(x|x.parameter('EPN').value='PXC.2862246').first for the first component whose EPN parameter has a value of PXC.2862246. The value for the width is then determined from this component using parameter('Width').value. This width is the third argument (distance) in the list.
