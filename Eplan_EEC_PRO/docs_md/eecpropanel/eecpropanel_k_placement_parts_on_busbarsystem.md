---
title: "Placement of parts on busbar systems"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecpropanel_k_placement_parts_on_busbarsystem.htm"
file: "eecpropanel_k_placement_parts_on_busbarsystem"
category: "eecpropanel"
---

# Placement of parts on busbar systems

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Placement of parts on busbar systems

In the case of a busbar system you place the parts on the mounting surface of a rail and to this purpose specify the ID of the rail with the parameter BusbarID (for example 15500.1.3;0;2).

The first and all further parts are lined up without gaps to the first support (Holder_0).

No further specifications are required in addition to the part number, plug and BusBarId.

If not all parts fit between two supports, the parts no longer fitting are lined up without gaps to the next support.

If the supports between the first and last supports and all parts are to be lined up on the same busbar without gaps, these supports are to be modeled as components.

In order to line up a modeled support to a placed part without gaps, use the BusbarID parameter to specify the ID of the rail with a preceding plus sign (for example +15500.1.3;0;2).

The following specifications can be used for the placement.

Parameter | Parameter type | Usage | Syntax | Example  
---|---|---|---|---  
Plug | Plug | Plug-Socket concept |  ='plug name' |  ='TS1_PF_MP_S1'  
Socket | Socket |  Plug-Socket concept |  ='socket name' |  ='S1_BusBar'  
Position | String or integer | Position within the sequence in a hierarchy level of the project |  As string: ='<position>' As integer: =<position> |  Position as string:='2' Position as integer:=2  
BusBarId | BusBarId | Identification number of the mounting surface of a busbar |  ='<BusBarId>' |  Upper busbar: ='15500.1.3;0;3' Middle busbar: ='15500.1.3;0;2' Lower busbar: ='15500.1.3;0;0'   
  
Coordinate | Coordinate | Distance in X direction from M4 of the busbar |  As list: =List{<x-coordinate>} |  =List{20.0}  
Coordinate map | CoordinateMap | Distance in X direction from M4 of the mounting rail (Y coordinate is ignored) |  As map: =Map{  
Pair{'x',<x-coordinate>},  
Pair{'y',<y-coordinate>}  
} |  =Map{  
Pair{'x',20.0},  
Pair{'y',0.0}  
}  
Dimension | Dimension | Length of the busbar system |  As list: =List{<length>} |  =List{700.0}   
  
Mate | Mate | Position on the busbar |  Line up without gaps: =List{  
'<source mate',  
'<destination mate>'  
} Line up at a distance to the predecessor: =List{  
'<source mate',  
'<destination mate>',  
<x-offset>  
} |  Line up without gaps: =List{  
'M4',  
'M2'  
} Line up with distance: =List{  
'M4',  
'M2',  
20.0  
}  
MateMarker | MateMarker | Unique reference to an already placed object | Any string |  MateMarker of an already placed object:='X104' Reference to the already placed object with the MateMap parameter: =Map{  
Pair{'src','G1'},  
Pair{'dest','X104:M4'}  
}  
MateMap | MateMap | Position on an already placed object |  Syntax without distances and without angle specifications: =Map{  
Pair{'src','<handle>'},  
Pair{'dest','<plane>:<mate of plane>'}  
} Syntax with distances in all directions and angle specifications for rotations around all axes (all combinations are permitted): =Map{  
Pair{'src','<handle>'},  
Pair{'dest','<plane>:<mate of plane>'},  
Pair{'dx',<value>},  
Pair{'dy',<value>},  
Pair{'dz',<value>},  
Pair{'angleX',<value>},  
Pair{'angleY',<value>},  
Pair{'angleZ',<value>}  
} |  Placement without distances and without angle specifications: =Map{  
Pair{'src','G1'},  
Pair{'dest','X104:M4'}  
} Placement with distances in the X and Y direction as well as rotation around the X axis: =Map{  
Pair{'src','C'},  
Pair{'dest','X104:V1'},  
Pair{'dx','120'},  
Pair{'dy','90'},  
Pair{'angleX','45'}  
}  
Part number | PartNumber |  Part number of a device in the Eplan parts database (<22001> Part number) |  ='Part number' |  Rittal busbar system: ='RIT.BBS.RiLine60_060_3_ECu12x05_2400_internal'  
Additional specifications | SupplementaryMap |  Map with specification about the number of supports and the positions of the first and last supports |  =Map{  
Pair{'holder',<number of holders>},  
Pair{'startoffset',<value>},  
Pair{'endoffset',<value>}  
} |  Busbar system with 3 supports which are placed 20 mm from the ends: =Map{  
Pair{'holder',3},  
Pair{'startoffset',20.0},  
Pair{'endoffset',-20.0}  
}  
  
### Note

The unit that is set in Pro Panel is always used for the specifications of length, height, width, etc.

The specification of an angle can be effected either in degrees or in radians (see [Unit for Angles](admin_r_modelvar_propanel_angle.htm)).

### Tip

If the placement is to be carried out in relation to a previously placed object, it is recommended to use the Position parameter to specify the sequence of the objects to be placed.

### [Example with 5 adapters on a busbar system with 3 supports](javascript:void\(0\);)

Example for placement without gaps of several adapters on a busbar system.

The fifth adapter no longer fits into the gap between the fourth adapter and the middle support. The fifth adapter is therefore lined up without gaps to the middle support.

Result:

### [Example with a modeled support that is lined up without gaps to the last adapter](javascript:void\(0\);)

Example for the placement without gaps of several adapters and a modeled support on a busbar system.

3 supports are specified for the busbar system via the SupplementaryMap parameter. These supports are placed by means of the startoffset and endoffset specifications as well as the center of the busbar system.

The completely placed support is modeled as a discipline component. By means of the BusBarId the support is lined up without gaps to the second adapter.

Result:

### [Example with parts on 2 adapters on a busbar system](javascript:void\(0\);)

Example for the placement of parts on the mounting rails of the adapters that are placed on a busbar system.

To this purpose the mounting rails of the adapters are to be modeled as components that are placed on a mounting surface on the adapter that is also to be modeled.

The parts are placed without specifications with their handle on the mounting point M4 of the mounting rail.

Result:

### Read more

     * [Handle and mounting points](eecpropanel_k_mates_for_devices.htm)
