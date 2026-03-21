---
title: "Placement of parts on parts"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecpropanel_k_place_devices_on_device.htm"
file: "eecpropanel_k_place_devices_on_device"
category: "eecpropanel"
---

# Placement of parts on parts

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Placement of parts on parts

Parts that allow another part to be placed on it usually already have a corresponding mounting point.

Mounting points are displayed in a macro project.

If you drag the mouse pointer onto a mounting point, its designation is displayed as a tooltip.

In the following representation the tooltip shows the mounting point SIE.8WD4_AE:

The mounting point can be used for the part to be placed on it in the value for the MateMap parameter, for example =Map{Pair{'src','C'},Pair{'dest','SIE.8WD4_AE'},Pair{'angle',0},Pair{'dx',0},Pair{'dy',0}}.

The following representation shows the placement resulting from the example above:

If target and source parts are located at different locations within the model structure, you can assign a unique reference to the target part with the MateMarker parameter which the source part references with the MateMap parameter.

### Note

Objects that have to provide an unambiguous reference via the MateMarker parameter must be inserted into the model structure before the objects that refer to this reference.

### Note

An object with a MateMap connects to the superior object if no object with a suitable MateMarker is to be found.

The following specifications can be used for the placement.

Parameter | Parameter type | Usage | Syntax | Example  
---|---|---|---|---  
Part number | PartNumber |  Part number of a device in the Eplan parts database (<22001> Part number) |  ='part number' |  Siemens base for signaling column: ='SIE.8WD4308-0CA'  
Coordinate | Coordinate | Distance in X direction from M4 of the mounting rail |  As list: =List{<x-coordinate>, <y-coordinate>} |  =List{20.0}   
  
Coordinate Map | CoordinateMap | Distance in X direction from M4 of the mounting rail (Y coordinate is ignored) |  As map:  
=Map{  
Pair{'x',<x-coordinate>},  
Pair{'y',<y-coordinate>}  
} |    
=Map{  
Pair{'x',20.0},  
Pair{'y',0.0}  
}  
Mate | Mate | Position in relation to the predecessor |  Placement without gaps at the predecessor: =List{  
'<source mate',  
'<destination mate>'  
} Placement at a distance from the predecessor in the X direction: =List{  
'<source mate',  
'<destination mate>',  
<x-offset>  
} Placement at a distance from the predecessor in the X direction and rotation around the X axis: =List{  
'<source mate',  
'<destination mate>',  
<angle>,  
<dx>  
} Placement at a distance from the predecessor in the X and Y direction and rotation around the X axis: =List{  
'<source mate',  
'<destination mate>',  
<angle>,  
<dx>,  
<dy>  
} Placement at a distance from the predecessor in the X, Y and Z direction and rotation around the X axis: =List{  
'<source mate',  
'<destination mate>',  
<angle>,  
<dx>,  
<dy>,  
<dz>  
} Placement at a distance from the predecessor in all directions and rotation around all axes: =List{  
'<source mate',  
'<destination mate>',  
<angleX>,  
<angleY>,  
<angleZ>,  
<dx>,  
<dy>,  
<dz>  
} |  Placement without gaps at the predecessor: =List{  
'M4',  
'M2'  
} Placement at a distance from the predecessor in the X direction: =List{  
'M4',  
'M2',  
20.0  
} Placement at a distance from the predecessor in the X direction and rotation around the X axis: =List{  
'M4',  
'M2',  
90,  
20.0  
} Placement at a distance from the predecessor in the X and Y direction and rotation around the X axis: =List{  
'M4',  
'M2',  
90,  
20.0,  
40.0  
} Placement at a distance from the predecessor in the X, Y and Z direction and rotation around the X axis: =List{  
'M4',  
'M2',  
90,  
20.0,  
40.0,  
60.0  
} Placement at a distance from the predecessor in all directions and rotation around all axes: =List{  
'M4',  
'M2',  
90,  
180,  
270,  
20.0,  
40.0,  
60.0  
}  
MateMap | MateMap | Position on an already placed object |  Syntax without distances and without angle specifications: =Map{  
Pair{'src','<handle>'},  
Pair{'dest','<plane>:<mate of plane>'}  
}   
Syntax with distances in all directions and angle specifications for rotations around all axes (all combinations are permitted): =Map{  
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
Pair{'dest','MateMarker:V1'},  
Pair{'dx','120'},  
Pair{'dy','90'},  
Pair{'angleX',45}  
}  
MateMarker | MateMarker | Unique reference to an already placed object | Any string |  MateMarker of an already placed object:='X104' Reference to the already placed object with the MateMap parameter: =Map{  
Pair{'src','G1'},  
Pair{'dest','X104:M4'}  
}  
Plug | Plug | Plug-Socket concept |  ='plug name' |  ='Signal_Foot'  
Position | String or integer | Position within the sequence in a hierarchy level of the project |  As string: ='<position>' As integer: =<position> |  Position as string:='2' Position as integer:=2  
Socket | Socket | Plug-Socket concept |  ='socket name' |  ='Signal_Pipe'  
  
### [Example with parts of a signaling column](javascript:void\(0\);)

Example for the placement of several parts for a signaling column.

The first part (Foot_angled) is placed by means of the Coordinate = List{20.0,0} parameter at a distance of 20.0 mm to the left-hand edge of the mounting rail.

All further parts are lined up without gaps to their respective predecessors.

In the line up, the sequence is defined by a consecutive value for the Position parameter:

Result:

### [Example for the placement of multi-part parts on different mounting surfaces](javascript:void\(0\);)

The following example shows a main switch whose rotary knob is placed on a enclosure door and that acts via a shaft on the switch element which is placed on a mounting rail on the mounting panel.

Rotary knob:

Switch element:

For the placement of the rotary knob with shaft, the switching element has the mounting point 3KD_WELLE.

The items are located on different branches of the discipline structure. The switch element (MainSwitch) is located below the mounting panel, the rotary knob (RotaryHandle) below the enclosure door.

The parameter MateMarker is defined with the value Q1 in the switch element.

For the placement of the rotary knob the value of the MateMarker parameter is to be specified with Q1:3KD_WELLE for dest in the MateMap parameter.

Result:

### Note

The unit that is set in Pro Panel is always used for the specifications of length, height, width, etc.

The specification of an angle can be effected either in degrees or in radians (see [Unit for Angles](admin_r_modelvar_propanel_angle.htm)).

### Read more

     * [Handle and mounting points](eecpropanel_k_mates_for_devices.htm)
