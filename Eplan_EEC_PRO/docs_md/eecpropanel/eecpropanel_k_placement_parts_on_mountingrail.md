---
title: "Placement of parts on mounting rails"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecpropanel_k_placement_parts_on_mountingrail.htm"
file: "eecpropanel_k_placement_parts_on_mountingrail"
category: "eecpropanel"
---

# Placement of parts on mounting rails

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Placement of parts on mounting rails

By default, the first part is placed on a mounting rail with the mounting point M4 centered at the left-hand edge.

Further parts are lined up without gaps with the mounting point M4 to the mounting point M2 of the predecessor. You do not have to make specifications in this regard.

To place parts at a distance from mounting point M4 of the mounting rail, use the Coordinate or CoordinateMap parameter.

If parts are to be placed on the mounting rail at a distance from an already placed part, use the Mate parameter.

Parts whose holding clip is not aligned centered have the handle G1 or have to be extended by the handle G1. The handle G1 should be positioned at the left-hand edge in the center of the holding clip for these parts.

The following specifications can be used for the placement.

Parameter | Parameter type | Usage | Syntax | Example  
---|---|---|---|---  
Part number | PartNumber |  Part number of a device in the Eplan parts database (<22001> Part number) |  ='<part number>' |  Phoenix Contact feed-through terminal PT 2.5 gray: ='PXC.3209510'  
Coordinate | Coordinate | Distance in X direction from M4 of the mounting rail |  =List{<x-coordinate>} |  =List{20.0}  
Coordinate Map | CoordinateMap | Distance in X direction from M4 of the mounting rail (Y coordinate is ignored) |  =Map{  
Pair{'x',<x-coordinate>},  
Pair{'y',<y-coordinate>}  
} |  =Map{  
Pair{'x',20.0},  
Pair{'y',0.0}  
}  
Mate | Mate | Position on the mounting rail |  Line up without gaps: =List{  
'<source mate',  
'<destination mate>'  
} Line up at a distance to the predecessor: =List{  
'<source mate',  
'<destination mate>',  
<x-offset>  
} Line up parts with add-ons (<x-offset> corresponds to the width of the add-on): =List{  
'<source mate',  
'<destination mate>',  
<x-offset>  
} |  Line up of symmetrical parts to symmetrical predecessors without gaps:=List{  
'M4',  
'M2'  
} Line up of asymmetrical parts to symmetrical predecessors without gaps:=List{  
'G1',  
'M2'  
} Line up of asymmetrical parts to asymmetrical predecessors without gaps:=List{  
'M4',  
'M2'  
} Line up of symmetrical parts to symmetrical predecessors at a distance:=List{  
'M4',  
'M2',  
20.0  
} Line up of asymmetrical parts to symmetrical predecessors at a distance:=List{  
'G1',  
'M2',  
20.0  
} Line up of asymmetrical parts to asymmetrical predecessors at a distance:=List{  
'M4',  
'M2',  
20.0  
} Line up of parts with add-ons:=List{  
'M4',  
'M2',  
7.5  
}  
Plug | Plug | Plug-Socket concept |  ='<plug name>' |  ='PF_MP_S1'  
Position | String or integer | Position within the sequence in a hierarchy level of the project |  As string: ='<position>' As integer: =<position> |  Position as string:='2' Position as integer:=2  
Socket | Socket |  Plug-Socket concept |  ='<socket name>' |  ='MR1_PF_MP_S1'  
  
### Note

The unit that is set in Pro Panel is always used for the specifications of length, height, width, etc.

The specification of an angle can be effected either in degrees or in radians (see [Unit for Angles](admin_r_modelvar_propanel_angle.htm)).

### [Example with parts at a distance from mounting point M4 of the mounting rail](javascript:void\(0\);)

Example for the placement of a terminal block consisting of several parts on a mounting rail.

The first part (EndBracket_1) is placed by means of the Coordinate = List{20.0,0} parameter at a distance of 20.0 mm to the left-hand edge of the mounting rail.

All further parts are lined up without gaps to their respective predecessors.

In the line up, the sequence is defined by a consecutive value for the Position parameter:

Result:

### [Example with parts with spacing on the same mounting rail](javascript:void\(0\);)

Example for the placement of two terminal blocks consisting of several parts on a mounting rail. The terminal blocks are placed at a distance of 40.0 mm from each other.

The first part (EndBracket_3) is placed on the same mounting rail by means of the Mate=List{'M4', 'M2', 40.0} parameter at a distance of 40.0 mm to the predecessor part (EndBracket_2).

All further parts are lined up without gaps to their respective predecessors.

In the line up, the sequence is defined by a consecutive value for the Position parameter:

Result:

### [Example with add-on on the same mounting rail](javascript:void\(0\);)

Example for the placement of two contactors that are each extended with an auxiliary contact on the left-hand side.

The first contactor (Contactor_1) is placed by means of the Coordinate=List{20.0, 0} parameter at a distance of 20.0 mm to the mounting point M4 of the mounting rail. The first contactor is given the MateMarker Contactor1 so that the second contactor can be placed relative to the first contactor without calculating it.

The first auxiliary contact (AuxiliaryContact_1) is placed with the handle G1 at the mounting point M4 of the first contactor on the same mounting rail.

The second contactor (Contactor_2) is placed by means of the Mate = List{'M4', 'Contactor1:M2', 8.7} parameter at a distance of 8.7 mm (corresponds to the width of an auxiliary contact) from the mounting point M2 of the first contactor.

The second auxiliary contact (AuxiliaryContact_2) is placed with the handle G1 at the mounting point M4 of the second contactor on the same mounting rail.

Result:

### Note

For this example the 3D macro of the auxiliary contact ABB.1SAE901901R1011 has been modified.

    1. The placement area was exchanged from the right-hand side to the lower side.
    2. The handle G1 has been added on the right-hand side so that the auxiliary contact can be placed in the center of the contactor.

### Tip

If the placement is to be carried out in relation to a previously placed object, it is recommended to use the Position parameter to specify the sequence of the objects to be placed.

### Read more

     * [Handle and mounting points](eecpropanel_k_mates_for_devices.htm)
