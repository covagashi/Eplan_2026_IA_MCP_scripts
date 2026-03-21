---
title: "Placement of busbar systems on the mounting surface"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecpropanel_k_placement_busbarsystem.htm"
file: "eecpropanel_k_placement_busbarsystem"
category: "eecpropanel"
---

# Placement of busbar systems on the mounting surface

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Placement of busbar systems on the mounting surface

In order to position a busbar system that consists of at least two holders and two busbars, the length, start position, number of holders and the relative positions of the first and last holders are required.

You specify the length and start position with the Dimension and Coordinate parameters.

You specify the number of supports as well as the positions of the first and last supports with the SupplementaryMap parameter.

You enter the value of the endoffset parameter as a negative number, since the offset relative to the end of the busbar system has to be calculated.

Example:

=Map{  
Pair{'holder',3},  
Pair{'startoffset',20.0},  
Pair{'endoffset',-20.0}  
}

Further supports are placed evenly distributed over the length of the busbar system.

The following specifications can be used for the placement.

Parameter | Parameter type | Usage | Syntax | Example  
---|---|---|---|---  
Part number | PartNumber |  Part number of a device in the Eplan parts database (<22001> Part number) |  ='<part number>' |  Rittal busbar system: ='RIT.BBS.RiLine60_060_3_ECu12x05_2400_internal'  
Dimension | Dimension | Length and alignment |  =List{  
<lenght>,  
<angle>  
} |  =List{  
700.0,  
0  
}  
Coordinate | Coordinate | Position on the mounting surface |  =List{  
<x-coordinate>,  
<y-coordinate>  
} |  =List{  
150.6,  
70.2  
}  
Plug | Plug | Plug-Socket concept |  ='<plug name>' |  ='S1_MP'  
Position | String or integer | Position within the sequence in a hierarchy level of the project |  As string: ='<position>' As integer: =<position> |  Position as string:='2' Position as integer:=2  
Socket | Socket |  Plug-Socket concept |  ='<socket name>' |  ='S1_BusBar'  
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

### [Example with three supports and three rails](javascript:void\(0\);)

Example for the placement of a busbar system with three rails and three supports.

The first support and the third support are placed at a distance of 20 mm from the ends of the rails.

Result:
    
        =Map{Pair{'holder',<number of holders>}, Pair{'startoffset',<value>}, Pair{'endoffset',<value>}}

Components positioned on a busbar system are mounted side-by-side, flush with the first support (Holder_0). So that no space is wasted between the last allowable component and the next support, the next support (Holder_2) is assigned an ID that is extended with the plus-sign before the ID value, e.g. +15050.1.3;0;3.

In order to place an additional component on an already positioned component, the 3D macro of the component to be placed must be equipped with a user-defined mounting point, e.g. MP1. In this example, the component to be placed, which has a mounting point of MP1, can be attached to mounting point MA1 of the already positioned component.

### Tip

If the placement is to be carried out in relation to a previously placed object, it is recommended to use the Position parameter to specify the sequence of the objects to be placed.

### Read more

     * [Handle and mounting points](eecpropanel_k_mates_for_devices.htm)
