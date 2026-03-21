---
title: "Placement of enclosures in the layout space"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecpropanel_k_placement_enclosures.htm"
file: "eecpropanel_k_placement_enclosures"
category: "eecpropanel"
---

# Placement of enclosures in the layout space

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Placement of enclosures in the layout space

The handles that are used for enclosures differ from those of the parts:

Enclosures that have not yet been positioned have the following handles:C1, C2, C3 and C4.

Enclosures that have been positioned have the following handles:CUB1, CUB2, CUB3 and CUB4.

The following specifications can be used for the placement.

Parameter | Parameter type | Usage | Syntax | Example  
---|---|---|---|---  
3D macro | Macro3D | Specify 3D macro instead of part number of enclosure. |  Specification of the macro file with the absolute path: ="<absolute path><3D macro name>" Specification of the macro file via system parameters: =type('Engineering.System').globalResourcePath()+'<trailing path><3D macro name>' |  Specification of the absolute path to the macro file: ='Rittal\\\SE\\\SE5833600_3D.ema' Specification of the macro file via system parameters: =type('Engineering.System').globalResourcePath()+'Rittal\\\SE\\\SE5833600_3D.ema'  
Part number | PartNumber | Placement of a part |  ='<part number>' |  ='RIT.5833600'  
Macro variant | String | The variant of the macro for an enclosure |  Alphabetical: ='<variant>' Numerical: <variant> Alphanumeric: ='variant' |  Alphabetical:='A' Numerical: =1 Alphanumeric: ='1'  
MateMap | MateMap | Placement mate on mate with coordinate and angle specifications |  Placement without distance and without angle: =Map{  
Pair{'src','<source mate>'},  
Pair{'dest','<destination mate>'}  
} Placement without distance and with angle: =Map{  
Pair{'src','<source mate>'},  
Pair{'dest','<destination mate>'},  
Pair{'angle',<value>}  
} Placement with distance and with angle: =Map{  
Pair{'src','<source mate>'},  
Pair{'dest','<destination mate>'},  
Pair{'dx',<value>},  
Pair{'dy',<value>},  
Pair{'dz',<value>},  
Pair{'angle',<value>}  
} |  Placement without distance and without angle: =Map{  
Pair{'src','C4'},  
Pair{'dest','CUB3'}  
} Placement without distance and with angle: =Map{  
Pair{'src','C4'},  
Pair{'dest','CUB3'},  
Pair{'angle',90}  
} Placement with distance and with angle: =Map{  
Pair{'src','C4'},  
Pair{'dest','CUB3'},  
Pair{'dx',0},  
Pair{'dy',0},  
Pair{'dz',0},  
Pair{'angle',90}  
}  
Plug | Plug | Plug-Socket principle |  ='<plug name>' |  ='Enclosure'  
Position | String or integer | Position within the sequence in a hierarchy level of the project |  Position as string: ='<position>' Position as integer: =<position> |  Position as string:='2' Position as integer:=2  
Socket | Socket | Plug-Socket principle |  ='<socket name>' |  ='S1_Enclosure'  
  
### Tip

The specification of an angle must not be defined in relation to the previous component (enclosure), but absolutely.

If, in the above example, a further enclosure is to be lined up on the right-hand side, wall-to-wall, the same angle (90) must be used.

### Note

The unit that is set in Pro Panel is always used for the specifications of length, height, width, etc.

The specification of an angle can be effected either in degrees or in radians (see [Unit for Angles](admin_r_modelvar_propanel_angle.htm)).

Not all combinations of target and start handles are permitted, because this could lead to collisions. For the same reason, not all coordinate values are valid.

In order to place several enclosures that are located in the same level of the discipline structure in the same layout space we recommend using a formula with the following form for MateMap:
    
        =if droot.dos('Enclosure').indexOf(this)= 0
    	then
    	null
    	else
    	Map { Pair {'src', 'C4'}, Pair {'dest', 'CUB3'} ,Pair {'dx', 0}, Pair {'dy', 0}, Pair{'angle', 0} }
    endif

### Note

Enclosures, preconfigured with placed parts, can be saved and reused as modified parts or 3D macros.

### [Example with 6 enclosures lined up in a rectangle](javascript:void\(0\);)

Example for the placement of several enclosures in the same layout space.

Result:

### Read more

     * [Handle and mounting points](eecpropanel_k_mates_for_devices.htm)
