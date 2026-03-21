---
title: "Placement of parts on mounting surface"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecpropanel_k_placement_devices.htm"
file: "eecpropanel_k_placement_devices"
category: "eecpropanel"
---

# Placement of parts on mounting surface

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Placement of parts on mounting surface

Devices can be placed on every mounting surface.

The specification of coordinates generally refers to the mounting point V1 of the mounting surface. The values for the coordinates can also be specified as offsets to another base point.

The following specifications can be used for the placement.

Parameter | Parameter type | Usage | Syntax | Example  
---|---|---|---|---  
Part number | PartNumber |  Part number of a device in the Eplan parts database (<22001> Part number) |  ='<part number>' |  Base for Siemens signaling column: ='SIE.8WD4308-0CA'  
Coordinate | Coordinate | Position on the mounting surface |  =List{  
<x-coordinate>,  
<y-coordinate>  
} |  =List{  
150.6,  
70.2  
}  
Mate | Mate | Position on the mounting surface |  Specification of source and target mounting point: =List{  
'<handle>',  
'<plane>:<mate of plane>'  
} |  Specification of source and target mounting point: =List{  
'C',  
'FrontPlane:V1'  
}  
Specification of source and target mounting point and offset in the X direction: =List{  
'<handle>',  
'<plane>:<mate of plane>',  
<x-offset>  
} |  Specification of source and target mounting point and offset in the X direction: =List{  
'C',  
'FrontPlane:V1',  
150.6  
}  
Specification of source and target mounting point and offset in the X and Y direction: =List{  
'<handle>',  
'<plane>:<mate of plane>',  
<x-offset>,  
<y-offset>  
} |  Specification of source and target mounting point and offset in the X and Y direction: =List{  
'C',  
'FrontPlane:V1',  
150.6,  
70.2  
}  
Specification of source and target mounting point and offset in the X, Y and Z direction: =List{  
'<handle>',  
'<plane>:<mate of plane>',  
<x-offset>,  
<y-offset>,  
<z-offset>  
} |  Specification of source and target mounting point and offset in the X, Y and Z direction: =List{  
'C',  
'FrontPlane:V1',  
150.6,  
70.2,  
20.0  
}  
Specification of source and target mounting point and angle and offset in the X, Y and Z direction: =List{  
'<handle>',  
'<plane>:<mate of plane>',  
<angle>,  
<x-offset>,  
<y-offset>,  
<z-offset>  
} |  Specification of source and target mounting point and angle and offset in the X, Y and Z direction: =List{  
'C',  
'FrontPlane:V1',  
0,  
150.6,  
70.2,  
20.0  
}  
Specification of source and target mounting point and angle in the X, Y and Z direction and offset in the X, Y and Z direction: =List{  
'<handle>',  
'<plane>:<mate of plane>',  
<angle-X>,  
<angle-Y>,  
<angle-Z>,  
<x-offset>,  
<y-offset>,  
<z-offset>  
} |  Specification of source and target mounting point and angle in the X, Y and Z direction and offset in the X, Y and Z direction: =List{  
'C',  
'FrontPlane:V1',  
0,  
0,  
0,  
150.6,  
70.2,  
20.0  
}  
MateMap | MateMap | Position on the mounting surface |  Placement with reference to a mounting point of a mounting panel: =Map{   
Pair{'src','<source mate'},  
Pair{'dest','<destination mate>'},  
Pair{'dx',<value>},  
Pair{'dy',<value>},  
Pair{'angle',<value>}  
} |  Placement with reference to a mounting point of a mounting panel: =Map{  
Pair{'src','V1'},  
Pair{'dest','MP1'},  
Pair{'dx',200.0},  
Pair{'dy',500.0},  
Pair{'angle',0}  
}  
Placement with reference to a MateMarker: =Map{  
Pair{'src','<source mate'},  
Pair{'dest','<MateMarker definition>'},  
Pair{'dx',<value>},  
Pair{'dy',<value>},  
Pair{'angle',<value>}  
} |  Placement with reference to a MateMarker: =Map{  
Pair{'src','C'},  
Pair{'dest','MateMarker:V1'},  
Pair{'dx',100.0},  
Pair{'dy',150.5},  
Pair{'angle','0'}  
}  
Placement with reference to an already placed device: =Map{   
Pair{'src','<source mate'},  
Pair{'dest','<destination mate>'},  
Pair{'dx',<value>},  
Pair{'dy',<value>},  
Pair{'angle',<value>}  
} |  Placement with reference to an already placed device: =Map{  
Pair{'src','V4'},  
Pair{'dest','V3'},  
Pair{'dx',5.0},  
Pair{'dy',5.0},  
Pair{'angle','90'}  
}  
Placement with reference to an already placed device and application of the target coordinate system: =Map{  
Pair{'src','<source mate'},  
Pair{'dest','<destination mate>'},  
Pair{'dx',<value>},  
Pair{'dy',<value>},  
Pair{'angle',<value>},  
Pair{'useDestCS',<value>}  
} |  Placement with reference to an already placed device and application of the target coordinate system: =Map{  
Pair{'src','V4'},  
Pair{'dest','V3'},  
Pair{'dx',5.0},  
Pair{'dy',5.0},  
Pair{'angle',90},  
Pair{'useDestCS','true'}  
}  
Plug | Plug | Hierarchy within the project |  ='<plug name>' |  ='S1_Enclosure_Door'  
Position | String or integer | Position within the sequence in a hierarchy level of the project |  Position as string: ='<position>' Position as integer: =<position> |  Position as string:='2' Position as integer:=2  
  
### Note

The unit that is set in Pro Panel is always used for the specifications of length, height, width, etc.

The specification of an angle can be effected either in degrees or in radians (see [Unit for Angles](admin_r_modelvar_propanel_angle.htm)).

### [Example with reference to mounting point V1 of the door](javascript:void\(0\);)

Example for the placement of a part (base for Siemens signaling column) on the outer mounting surface of an enclosure door with reference to mounting point V1 of the door:

Result:

### [Example with reference to MateMarker FD1](javascript:void\(0\);)

Example for the placement of a part (base for Siemens signaling column) on the outer mounting surface of an enclosure door with reference to MateMarker FD1:

Result:

### [Example with reference to the component of the mounting surface Plane_Outside](javascript:void\(0\);)

Example for the placement of a part (base for Siemens signaling column) on the outer mounting surface of an enclosure door with reference to the mounting surface Plane_Outside:

Result:

### [Example with reference to the ID of the mounting surface 16000.1.2;10004;0](javascript:void\(0\);)

Example for the placement of a part (base for Siemens signaling column) on the outer mounting surface of an enclosure door with reference to MateMarker FD1:

Result:

### [Example with reference to a previously placed part](javascript:void\(0\);)

Example for the placement of a part (base for Siemens signaling column) on the outer mounting surface of an enclosure door with reference to a previously placed part (HMI device from Phoenix Contact):

Result:

### Tip

If the placement is to be carried out in relation to a previously placed object, it is recommended to use the Position parameter to specify the sequence of the objects to be placed.

### Note

The specification of an angle is always counter-clockwise in relation to the mounting surface.

### Read more

     * [Handle and mounting points](eecpropanel_k_mates_for_devices.htm)
