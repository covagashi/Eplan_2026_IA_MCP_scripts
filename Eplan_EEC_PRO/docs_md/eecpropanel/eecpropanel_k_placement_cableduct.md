---
title: "Placement of wire ducts on mounting surfaces"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecpropanel_k_placement_cableduct.htm"
file: "eecpropanel_k_placement_cableduct"
category: "eecpropanel"
---

# Placement of wire ducts on mounting surfaces

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Placement of wire ducts on mounting surfaces

To place mounting rails that are sold by the meter and are cut to size prior to assembly, it is necessary to specify not only the position, but also the length and alignment (angle).

To apply the target coordinate system of a point on which a device is to be placed instead of the global coordinate system, the specification of <useDestCS> is set to true or 'true'.

The following specifications can be used for the placement.

Parameter | Parameter type | Usage | Syntax | Example  
---|---|---|---|---  
Part number | PartNumber |  Part number of a device in the Eplan parts database (<22001> Part number) |  ='<part number>' |  Wire duct Rittal TS 8800.750: ='RIT.8800750'  
Dimension | Dimension | Length of the wire duct |  =List{<length>} |  =List{440.0}  
Coordinate | Coordinate | Position on the mounting surface |  =List{  
<x-coordinate>,  
<y-coordinate>  
} |  =List{  
150.6,  
70.2  
}  
Mate | Mate | Position on the mounting surface |  Specification of 2 values: =List{  
'<handle>',  
'<plane>:<mate of plane>'  
} |  =List{  
'C',  
'FrontPlane:V1'  
}  
Specification of 3 values: =List{  
'<handle>',  
'<plane>:<mate of plane>',  
<x-offset>  
} |  =List{  
'C',  
'FrontPlane:V1',  
150.6  
}  
Specification of 4 values: =List{  
'<handle>',  
'<plane>:<mate of plane>',  
<x-offset>,  
<y-offset>  
} |  =List{  
'C',  
'FrontPlane:V1',  
150.6,  
70.2  
}  
Specification of 5 values: =List{  
'<handle>',  
'<plane>:<mate of plane>',  
<x-offset>,  
<y-offset>,  
<z-offset>  
} |  =List{  
'C',  
'FrontPlane:V1',  
150.6,  
70.2,  
20.0  
}  
Specification of 6 values: =List{  
'<handle>',  
'<plane>:<mate of plane>',  
<angle>,  
<x-offset>,  
<y-offset>,  
<z-offset>  
} |  =List{  
'C',  
'FrontPlane:V1',  
0,  
150.6,  
70.2,  
20.0  
}  
Specification of 7 values: =List{  
'<handle>',  
'<plane>:<mate of plane>',  
<angle>,  
<x-offset>,  
<y-offset>,  
<z-offset>,  
<useDestCS>  
} |  =List{  
'C',  
'FrontPlane:V1',  
0,  
150.6,  
70.2,  
20.0,  
'false'  
}  
Specification of 8 values: =List{  
'<handle>',  
'<plane>:<mate of plane>',  
<angle-X>,  
<angle-Y>,  
<angle-Z>,  
<x-offset>,  
<y-offset>,  
<z-offset>  
} |  =List{  
'C',  
'FrontPlane:V1',  
0,  
0,  
0,  
150.6,  
70.2,  
20.0  
}  
Specification of 9 values: =List{  
'<handle>',  
'<plane>:<mate of plane>',  
<angle-X>,  
<angle-Y>,  
<angle-Z>,  
<x-offset>,  
<y-offset>,  
<z-offset>,  
'<useDestCS>'  
} |  =List{  
'C',  
'FrontPlane:V1',  
0,  
0,  
0,  
150.6,  
70.2,  
20.0,  
'false'  
}  
MateMap | MateMap | Position on the mounting surface |  Placement with reference to a mounting point of a mounting panel: =Map{   
Pair{'dest','<destination mate>'},  
Pair{'src','<source mate'},  
Pair{'dx',<value>},  
Pair{'dy',<value>},  
Pair{'dz',<value>}  
Pair{'angle',<value>}  
} |  Placement with reference to a mounting point of a mounting panel: =Map{   
Pair{'dest','MP1'},  
Pair{'src','V1'},  
Pair{'dx',10.0},  
Pair{'dy',500.0},  
Pair{'dz',0},  
Pair{'angle',0}  
}  
Placement with reference to a MateMarker: =Map{   
Pair{'dest','<MateMarker definition>'},  
Pair{'src','<source mate'},  
Pair{'dx',<value>},  
Pair{'dy',<value>},  
Pair{'dz',<value>},  
Pair{'angle',<value>}  
} |  Placement with reference to a MateMarker: =Map{   
Pair{'dest','MateMarker:V1'},  
Pair{'src','C'},  
Pair{'dx',10.0},  
Pair{'dy',500.5},  
Pair{'dz',0},  
Pair{'angle',0}  
}  
Placement with reference to an already placed wire duct: =Map{   
Pair{'dest','<destination mate>'},  
Pair{'src','<source mate'},  
Pair{'dx',<value>},  
Pair{'dy',<value>},  
Pair{'dz',<value>}  
Pair{'angle',<value>}  
} |  Placement with reference to an already placed wire duct: =Map{   
Pair{'dest','V1'},  
Pair{'src','V3'},  
Pair{'dx',0},  
Pair{'dy',0},  
Pair{'dz',0},  
Pair{'angle',270}  
}  
Plug | Plug | Plug-Socket principle |  ='<plug name>' |  ='S1_Mountingpanel'  
Position | String or integer | Position within the sequence in a hierarchy level of the project |  As string: ='<position>' As integer: =<position> |  Position as string:='2' Position as integer:=2  
  
### Note

The unit that is set in Pro Panel is always used for the specifications of length, height, width, etc.

The specification of an angle can be effected either in degrees or in radians (see [Unit for Angles](admin_r_modelvar_propanel_angle.htm)).

### [Example with reference to a previously placed wire duct](javascript:void\(0\);)

Example for the placement of wire ducts (Rittal RIT.8800750) on the front mounting surface of a mounting panel. The placement of the first wire duct (position=10) is described in the previous example. No coordinate is specified for the placement of the second wire duct (position=11). Instead, the second wire duct is placed with its handle V1 on the handle V3 of the first wire duct. The third wire duct (position=12) is placed with its handle V4 on the handle V2 of the second wire duct:

Result:

### Tip

If the placement is to be carried out in relation to a previously placed object, it is recommended to use the Position parameter to specify the sequence of the objects to be placed.

### Note

The specification of an angle is always counter-clockwise in relation to the mounting surface.

### Read more

     * [Handle and mounting points](eecpropanel_k_mates_for_devices.htm)
