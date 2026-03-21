---
title: "Placement of enclosure parts "
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecpropanel_k_placement_enclosureparts.htm"
file: "eecpropanel_k_placement_enclosureparts"
category: "eecpropanel"
---

# Placement of enclosure parts 

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Placement of enclosure parts

As a rule, placed enclosures are complete.

In order to place devices on an enclosure part, the enclosure part must first be modeled with the EnclosurePart type or the MountingPanel type.

The following specifications can be used for the placement.

Parameter | Parameter type | Usage | Syntax | Example  
---|---|---|---|---  
Mounting surface identification | Id | Identification number of a mounting surface for the placement |  ='id of enclosure part' |  ID of the door: ='15100.6.1;14;0' ID of the door outside: ='16000.1.2;10004;0' ID of the door inside: ='16000.1.2;10005;0' ID of the flange plate: ='15000.2.1;0;0:15100.1.2;0;0' ID of the flange plate outside: ='16000.1.2;10045;0' ID of the flange plate inside: ='16000.1.2;10044;0' ID of the mounting panel: ='15100.3.1;0;0' ID of the mounting panel front: ='16000.1.2;10002;0' ID of the mounting panel rear: ='16000.1.2;10003;0'  
Plug | Plug | Plug-Socket principle |  ='plug name' |  ='S1_Enclosure'  
Position | String or integer | Position within the sequence in a hierarchy level of the project |  Position as string: ='<position>' Position as integer: =<position> |  Position as string:='2' Position as integer:=2  
Socket | Socket | Plug-Socket principle |  ='socket name' |  ='S1_Enclosure_Door'  
  
### Note

The unit that is set in Pro Panel is always used for the specifications of length, height, width, etc.

The specification of an angle can be effected either in degrees or in radians (see [Unit for Angles](admin_r_modelvar_propanel_angle.htm)).

### Tip

The ID of an enclosure part, its mounting surface or the mounting surface of a device has the property 36035 Item ID (relative to macro) in Eplan Electric P8.

See also [Editing and displaying part placement properties](../../../../Plattform/2026/Content/htm/panellayoutgui_h_eigenschaftenartikelplatzierungenbearbeiten.htm)
