---
title: "Handle and mounting points"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecpropanel_k_mates_for_devices.htm"
file: "eecpropanel_k_mates_for_devices"
category: "eecpropanel"
---

# Handle and mounting points

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Handle and mounting points

### General

Handles (mates) are used not only for manual positioning, but also for generic positioning with the aid of the MateMarker, Mate and MateMap parameters.

3D objects in the 3D-graphics macros offer the following default handles:

If no coordinates are given for child devices, e.g. terminal clamps, the child is positioned via its **M4** handle on the M2 handle of its parent.

The **G1** handle constitutes a special case. It is not specified by default in a 3D-graphics macro, however. For devices whose mounting clamps are not positioned centrally for mounting on a mounting rail, the **G1** handle must be subsequently moved to a position on the left edge of the object that corresponds to the center of the clamp.

### Mounting panels

Mounting panels have mounting points that differ from the general handles:

### Enclosures

The handles that are used for enclosures differ from those of the parts:

Enclosures that have not yet been positioned have the following handles:C1, C2, C3 and C4.

Enclosures that have been positioned have the following handles:CUB1, CUB2, CUB3 and CUB4.

A map with the MateMap parameter with the following syntax is used for placement:
    
        =Map{
    	Pair{'src','<Mate>'},
    	Pair{'dest','<Mate'},
    	Pair{'dx',<value>},
    	Pair{'dy',<value>},
    	Pair{'dz',<value>},
    	Pair{'angle',<value>}
    }

For the placement shown in the above diagram, this sample formula is used:
    
        =Map{
    	Pair{'src','C4'},
    	Pair{'dest','CUB3'},
    	Pair{'dx',0},
    	Pair{'dy',0},
    	Pair{'dz',0},
    	Pair{'angle',90}
    }

Not all combinations of target and start handles are permitted, because this could lead to collisions. For the same reason, not all coordinate values are valid.

In order to place several enclosures that are located in the same level of the discipline structure in the same layout space we recommend using a formula with the following form for the MateMap parameter:
    
        =if droot.dos('Enclosure').indexOf(this)= 0
    	then
    	null
    	else
    	Map{ 
    		Pair {'src', 'C4'},
    		Pair {'dest', 'CUB3'},
    		Pair {'dx', 0},
    		Pair {'dy', 0},
    		Pair{'angle', 0}
    	}
    endif
