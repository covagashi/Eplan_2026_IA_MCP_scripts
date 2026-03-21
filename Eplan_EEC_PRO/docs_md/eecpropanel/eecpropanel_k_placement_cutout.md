---
title: "Placement of cutouts on mounting surfaces"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecpropanel_k_placement_cutout.htm"
file: "eecpropanel_k_placement_cutout"
category: "eecpropanel"
---

# Placement of cutouts on mounting surfaces

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Placement of cutouts on mounting surfaces

Cutouts can be placed on every mounting surface.

The following specifications can be used for the placement.

Parameter | Parameter type | Usage | Syntax | Example  
---|---|---|---|---  
Drilling pattern | DrillingPatternVariant | Name of the drilling pattern variant |  ='<drilling pattern name>' |  ='Fan_105'  
Coordinate | Coordinate | Position on the mounting surface |  =List{<x-coordinate>,<y-coordinate>} |  =List{150.6,70.2}  
Mate | Mate | Position on the mounting surface |  =List{'<handle>','<plane>:<mate of plane>',<angle>,<x-offset>,<y-offset>} |  =List{'C','FrontPlane:V1',0,150.6,70.2  
}  
MateMap | MateMap | Position on the mounting surface |  =Map{   
Pair{'dest','<MateMarker definition>'},  
Pair{'src','<source mate'},  
Pair{'dx',<value>},  
Pair{'dy',<value>},  
Pair{'angle',<value>}  
} |  =Map{   
Pair{'dest','MateMarker:V1'},  
Pair{'src','C'},  
Pair{'dx',100.0},  
Pair{'dy',150.5},  
Pair{'angle',0}  
}  
Plug | Plug | Plug-Socket principle |  ='<plug name>' |  ='S1_Enclosure_Door'  
Position | String or integer | Position within the sequence in a hierarchy level of the project |  Position as string: ='<position>' Position as integer: =<position> |  Position as string:='2' Position as integer:=2  
Additional specifications | SupplementaryMap |  Form and size of the cutout: 1 = Drill hole 2 = Threaded hole 3 = Rectangle 4 = Slotted hole 5 = Hexagon 6 = Octagon 7 = User-defined 8 = Drilling pattern |  Drill hole: =Map{  
Pair{'type',1},  
Pair{'diameter',<diameter in mm>}  
} |  Drill hole: =Map{   
Pair{'type',1},  
Pair{'width',22.6}  
}  
Threaded hole: =Map{   
Pair{'type',2},  
Pair{'diameter',<diameter of regular metric tap>}  
} |  Threaded hole: =Map{   
Pair{'type',2},  
Pair{'diameter',4}  
}  
Rectangle: =Map{   
Pair{'type',3},  
Pair{'width',<value>},  
Pair{'height',<value>}  
} |  Rectangle: =Map{  
Pair{'type',3},  
Pair{'width',50.2},  
Pair{'height',20.5}  
}  
Rectangle with rounded corners: =Map{  
Pair{'type',3},  
Pair{'width',<value>},  
Pair{'height',<value>},  
Pair{'radius',<value>}  
} |  Rectangle with rounded corners: =Map{  
Pair{'type',3},  
Pair{'width',50.2},  
Pair{'height',20.5},  
Pair{'radius',1.5}  
}  
Rectangle with chamfer: =Map{  
Pair{'type',3},  
Pair{'width',<value>},  
Pair{'height',<value>},  
Pair{'chamfer distance',<value>}  
} |  Rectangle with chamfer: =Map{  
Pair{'type',3},  
Pair{'width',50.2},  
Pair{'height',20.5},  
Pair{'chamfer distance',0.5}  
}  
Slotted hole: =Map{  
Pair{'type',4},  
Pair{'length',<value>},  
Pair{'height',<value>}  
} |  Slotted hole: =Map{  
Pair{'type',4},  
Pair{'length',30.0},  
Pair{'height',4.5}  
}  
Hexagon: =Map{  
Pair{'type',5},  
Pair{'edge length',<value>}  
} |  Hexagon: =Map{  
Pair{'type',5},  
Pair{'edge length',20.0}  
}  
Octagon: =Map{  
Pair{'type',6},  
Pair{'edge length',<value>}  
} |  Octagon: =Map{  
Pair{'type',6},  
Pair{'edge length',20.0}  
}  
User-defined: =Map{  
Pair{'type',7},  
Pair{'pattern','<path to file>'}  
} |  User-defined: =Map{  
Pair{'type',7},  
Pair{'pattern','MyCutout.fc1'}  
}  
Drilling pattern: =Map{  
Pair{'type',8},  
Pair{'pattern','<pattern name>'}  
} |  Drilling pattern: =Map{  
Pair{'type',8},  
Pair{'pattern','MyDrillingPattern'}  
}  
  
### Note

EEC supports parts with variants of drilling patterns To this purpose a parameter of the type DrillingPatternVariant is to be created. The parameter must be contained in the discipline component. The value of the parameter is the name of the drilling pattern variant.

### Tip

If the placement is to be carried out in relation to a previously placed object, it is recommended to use the Position parameter to specify the sequence of the objects to be placed.

### Note

The unit that is set in Pro Panel is always used for the specifications of length, height, width, etc.

The specification of an angle can be effected either in degrees or in radians (see [Unit for Angles](admin_r_modelvar_propanel_angle.htm)).

### Note

The specification of an angle is always counter-clockwise in relation to the mounting surface.

### [Example for cutouts in the enclosure door](javascript:void\(0\);)

Example for the placement of cutouts for an HMI device, as well as switches and indicator lights on the outer mounting surface of an enclosure door. All parts and their assigned cutouts are placed with their mounting point C in relation to mounting point V1 of the mounting surface of the door.

Result:

### Read more

     * [Handle and mounting points](eecpropanel_k_mates_for_devices.htm)
