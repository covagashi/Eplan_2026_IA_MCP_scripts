---
title: "Parameter"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecpropanel_k_parameter.htm"
file: "eecpropanel_k_parameter"
category: "eecpropanel"
---

# Parameter

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Parameter

The Pro Panel discipline requires parameters with own parameter types in order satisfy specific requirements.

Parameter | Parameter type | Description  
---|---|---  
Dimensions |  Dimension DimensionMap |  Dimensions: Height, Width, Depth  
Components: Enclosure, Enclosure_Part, MountingPanel, FreeMountingPanel, Plane  
Examples:  
Dimension: =List{'10','20','30'} DimensionMap: =Map{  
Pair{'height',10},  
Pair{'width',20},  
Pair{'depth',30}  
} Dimensions: Height, width, angle  
Components: Area Examples:  
Dimension: =List{'10','20','90'} DimensionMap: =Map{  
Pair{'height',10},  
Pair{'width',20},  
Pair{'angle',90}  
} Dimensions: Length, angle  
Components: Busbar, MountingRail, WireDuct Examples:  
Dimension: =List{'100','90'} DimensionMap: =Map{  
Pair{'length',100},  
Pair{'angle',90}  
} Dimensions: Angle  
Components: CutOut, Device Examples:  
Dimension: =List{'90'} DimensionMap: =Map{  
Pair{'angle',90}  
}  
Part number | PartNumber | Part number of a component in the parts database  
Part variant | ArticleVariant | The variant of the part of a Pro Panel component. The part variant must correspond to the name of the variant in the parts database. This can be any string.  
Layout space description | Map |  Map for the specification of the input field Description in the dialog Properties (components): Layout space: =Map{  
Pair{'36018','LayoutSpace description'}  
}  
Component property | PropertyMap |  Map for specifying component characteristics. The key corresponds to the property number, the value corresponds to the property text. Example for the specification Remark: Remark <20045>: =Map{  
Pair{'20045','Stack of workpieces'}  
}  
Device tag | DeviceTag | Device tag (DT). The DT has to be specified fully for Pro Panel components. It is not compiled during the creation of Pro Panel from individual structure identifiers.  
Drilling pattern variant | DrillingPatternVariant | The variant of a drilling pattern of a Pro Panel article. The variant of the drilling pattern must conform to the name of the drilling pattern in the part definition. This can be any string.  
Identification number | Id | Identification number that clearly identifies a mounting surface  
Coordinate | Coordinate | Coordinates for the placement of objects with the syntax =List{x,y}  
Coordinates map | CoordinateMap |  Coordinates for the placement of objects with the syntax =Map{  
Pair{'x',<value>},  
Pair{'y',<value>}  
}  
Macro3D | Macro3D |  Places the specified 3D macro directly instead of a part. Specification of the macro file with the absolute path: ="<absolute path><3D macro name>" Specification of the macro file via system parameters:
    
        =type('Engineering.System').globalResourcePath()+'<trailing path><3D macro name>'  
  
Macro variant | String | The variant of the macro for a part.  
The name of this parameter is to be entered in the model variables under Disciplines > ECAD > Eplan Electric P8 > Parameter Name For The Window Macro Variant so that macro variants can be used (see [Parameter Name For The Window Macro Variant](admin_r_modelvar_p8variant.htm)).  
Placement mate on mate with coordinate specification and angle specifications | MateMap |  For the placement of enclosures: =Map{  
Pair{'src','<source mate>'},  
Pair{'dest','<destination mate>'},  
Pair{'dx',<value>},  
Pair{'dy',<value>},  
Pair{'dz',<value>},  
Pair{'angle',<value>}  
} For the placement of parts: =Map{  
Pair{'src','<source mate>'},  
Pair{'dest','<destination mate>'},  
Pair{'dx',<value>},  
Pair{'dy',<value>},  
Pair{'dz',<value>},  
Pair{'x-angle',<value>},  
Pair{'y-angle',<value>},  
Pair{'z-angle',<value>}  
} For the placement of parts it is sufficient to specify the value of null for the <source mate> and <destination mate>: =Map{  
Pair{'src',null},  
Pair{'dest',null}  
}  
Placement mate on mate, optionally with distance | Mate |  For the placement of a part in relation to the predecessor part. =List{'<source mate>','<destination mate>',<distance>} To use the default value it is sufficient to specify null for <source mate> and <destination mate> as well as a value for <distance>, for example =List{null, null, 20.6}.  
Placement marker | MateMarker | Designates a distinct object, on which placement should take place or which is referred to.  
BusBarId | BusBarId | ID of the busbar system  
Enclosure description | Map |  Map for the specification of the input field Description in the dialog Properties (components): Layout space: =Map{  
Pair{'36018','Enclosure description'}  
}  
Supplementary field / Supplementary field [x] Indexed properties <property>[x] | PropertyMap |  Map for the specification of the property Supplementary field or Supplementary field [1] to Supplementary field [1000] or another indexed property. A map with a list or a map with the key value pairs can be specified for the values. For a map with list the specifications have to take place in sequence starting with 1. Empty fields must be specified as such.  
Example map with list: =Map{  
Pair{'20901', List{'Text1','Text2','','Text4'}}  
} Example map with key value pairs: =Map{  
Pair{'20901', Map{  
Pair{'0','Text1'},  
Pair{'1','Text2'},  
Pair{'5','Text6'}}}  
} Indexed properties can currently only be applied with the following ProPanel components:
     * BusBarSystem
     * CutOut,
     * Device,
     * Enclosure,
     * EnclosurePart,
     * LayoutSpace,
     * MountingRail,
     * WireDuct,  
Additional specifications | SupplementaryMap | Transfer of supplemental information, e.g. placement of the hold with busbars.  
Syntax for number of holders for busbars:  
=Map{  
Pair{'holder',<number of holders>},  
Pair{'startoffset',<value>},  
Pair{'endoffset',<value>}  
}  
Syntax for restricted placement areas:  
=Map{  
Pair{'type',1}  
}  
Syntax for restricted drilling areas:  
=Map{  
Pair{'type',2}  
}  
  
### Note

The unit that is set in Pro Panel is always used for the specifications of length, height, width, etc.

The specification of an angle can be effected either in degrees or in radians (see [Unit for Angles](admin_r_modelvar_propanel_angle.htm)).
