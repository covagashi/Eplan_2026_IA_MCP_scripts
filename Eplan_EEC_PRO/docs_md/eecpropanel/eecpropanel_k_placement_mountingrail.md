---
title: "Placement of mounting rails on mounting surfaces"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecpropanel_k_placement_mountingrail.htm"
file: "eecpropanel_k_placement_mountingrail"
category: "eecpropanel"
---

# Placement of mounting rails on mounting surfaces

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Placement of mounting rails on mounting surfaces

To place mounting rails that are sold by the meter and are cut to size prior to assembly, it is necessary to specify not only the position, but also the length and alignment (angle).

To apply the target coordinate system of a point on which a device is to be placed instead of the global coordinate system, the specification of <useDestCS> is set to true or 'true'.

The following specifications can be used for the placement.

Parameter | Parameter type | Usage | Syntax | Example  
---|---|---|---|---  
Part number | PartNumber |  Part number of a device in the Eplan parts database (<22001> Part number) |  ='<part number>' |  Mounting rail Rittal TS 35: ='RIT.4934000'  
Dimension | Dimension | Length of the mounting rail |  =List{<length>} |  =List{440.0}  
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
} |  Specification of 2 values: =List{  
'C',  
'FrontPlane:V1'  
}  
Specification of 3 values: =List{  
'<handle>',  
'<plane>:<mate of plane>',  
<x-offset>  
} |  Specification of 3 values: =List{  
'C',  
'FrontPlane:V1',  
150.6  
}  
Specification of 4 values: =List{  
'<handle>',  
'<plane>:<mate of plane>',  
<x-offset>,  
<y-offset>  
} |  Specification of 4 values: =List{  
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
} |  Specification of 5 values: =List{  
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
} |  Specification of 6 values: =List{  
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
} |  Specification of 7 values: =List{  
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
} |  Specification of 8 values: =List{  
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
<useDestCS>  
} |  Specification of 9 values: =List{  
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
Pair{'dy',<value>}  
Pair{'angle',<value>}  
} |  Placement with reference to a mounting point of a mounting panel: =Map{   
Pair{'dest','MP1'},  
Pair{'src','V1'},  
Pair{'dx',10.0},  
Pair{'dy',500.0},  
Pair{'angle',0}  
}  
Placement with reference to a MateMarker: =Map{   
Pair{'dest','<MateMarker definition>'},  
Pair{'src','<source mate'},  
Pair{'dx',<value>},  
Pair{'dy',<value>},  
Pair{'angle',<value>}  
} |  Placement with reference to a MateMarker: =Map{   
Pair{'dest','MateMarker:V1'},  
Pair{'src','C'},  
Pair{'dx',10.0},  
Pair{'dy',500.5},  
Pair{'angle',0}  
}  
Placement with reference to an already placed mounting rail: =Map{   
Pair{'dest','<destination mate>'},  
Pair{'src','<source mate'},  
Pair{'dx',<value>},  
Pair{'dy',<value>}  
Pair{'angle',<value>}  
} |  Placement with reference to an already placed mounting rail: =Map{   
Pair{'dest','V1'},  
Pair{'src','V1'},  
Pair{'dx',0},  
Pair{'dy',200.0},  
Pair{'angle',0}  
}  
Plug | Plug | Plug-Socket principle |  ='<plug name>' |  ='S1_MP_PF'  
Position | String or integer | Position within the sequence in a hierarchy level of the project |  As string: ='<position>' As integer: =<position> |  Position as string:='2' Position as integer:=2  
Socket | Socket | Plug-Socket principle |  ='<socket name>' |  ='S1_MP_PF_MR1'  
  
### Tip

If the placement is to be carried out in relation to a previously placed object, it is recommended to use the Position parameter to specify the sequence of the objects to be placed.

### Note

The unit that is set in Pro Panel is always used for the specifications of length, height, width, etc.

The specification of an angle can be effected either in degrees or in radians (see [Unit for Angles](admin_r_modelvar_propanel_angle.htm)).

### Note

The specification of an angle is always counter-clockwise in relation to the mounting surface.

### [Example with two mounting rails](javascript:void\(0\);)

Example for the placement of mounting rails (Rittal RIT.4934000) on the front mounting surface of a mounting panel. The placement of the first mounting rail (Position=20) is specified with a coordinate. No coordinate is specified when placing the second mounting rail (Position=21). Instead, the second mounting rail is placed via MateMap with its handle V1 on the handle V1 of the first mounting rail at a distance of -200 mm in the Y direction.

Result:

### Read more

     * [Handle and mounting points](eecpropanel_k_mates_for_devices.htm)
