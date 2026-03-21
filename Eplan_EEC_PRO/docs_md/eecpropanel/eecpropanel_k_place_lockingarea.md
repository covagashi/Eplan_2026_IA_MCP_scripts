---
title: "Placement of locked areas on mounting surfaces"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecpropanel_k_place_lockingarea.htm"
file: "eecpropanel_k_place_lockingarea"
category: "eecpropanel"
---

# Placement of locked areas on mounting surfaces

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Placement of locked areas on mounting surfaces

There are two types of locked areas:

     * Locked areas for placement
     * Locked areas for cutouts

Locked areas are always rectangular.

The following specifications can be used for the placement.

Parameters | Parameter type | Usage | Syntax | Example  
---|---|---|---|---  
Dimension | Dimension | Size of locked area |  =List{width, height} |  =List{60.0, 120.0}  
Coordinate | Coordinate | Position on the mounting surface |  =List{  
<x-coordinate>,  
<y-coordinate>  
} |  =List{  
150.6,  
70.2  
}  
Plug | Plug | Plug-Socket principle |  ='PlugName' |  =PlaneFront_MountingPanel_S1  
Position | String or integer | Position within the sequence in a hierarchy level of the project |  Position as string: ='<position>' Position as integer: =<position> |  Position as string:='2' Position as integer:=2  
Additional specifications | SupplementaryMap |  Type of locked area. 1 = Locked area for the placement 2 = Locked area for a cutout |  Locked area: =Map{  
Pair{'type', 1}  
} Cutout: =Map{  
Pair{'type', 2}  
} |  Locked area: =Map{  
Pair{'type', 1}  
} Cutout: =Map{  
Pair{'type', 2}  
}  
  
### Note

The unit that is set in Pro Panel is always used for the specifications of length, height, width, etc.

The specification of an angle can be effected either in degrees or in radians (see [Unit for Angles](admin_r_modelvar_propanel_angle.htm)).

### Tip

If the placement is to be carried out in relation to a previously placed object, it is recommended to use the Position parameter to specify the sequence of the objects to be placed.

### [Example with reference to a previously placed part](javascript:void\(0\);)

Example for the placement of a locked area on the outer mounting surface of an enclosure door with reference to a previously placed part (Siemens signaling column):

Result:

### Read more

     * [Handle and mounting points](eecpropanel_k_mates_for_devices.htm)
