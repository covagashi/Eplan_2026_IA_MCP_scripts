---
title: "Placement of mounting panels"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecpropanel_k_placement_mountingpanels.htm"
file: "eecpropanel_k_placement_mountingpanels"
category: "eecpropanel"
---

# Placement of mounting panels

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Placement of mounting panels

As a rule, mounting panels are part of a placed enclosure, but can also be placed directly in a layout space.

In both cases a mounting panel of the MountingPanel type has to be modeled in order to place devices on it.

The following specifications can be used for the placement.

Parameter | Parameter type | Usage | Value | Example  
---|---|---|---|---  
Mounting surface identification | Id | Identification number of a mounting surface for the placement |  ='<ID of enclosure part>' |  ID of the mounting panel:='15100.3.1;0;0' ID of the mounting panel front:='16000.1.2;10002;0' ID of the mounting panel rear:='16000.1.2;10003;0'  
Plug | Plug | Plug-Socket principle |  ='<plug name>' |  ='S1_Enclosure'  
Position | String or integer | Position within the sequence in a hierarchy level of the project |  Position as string: ='<position>' Position as integer: =<position> |  Position as string:='2' Position as integer:=2  
Socket | Socket | Plug-Socket principle |  ='<socket name>' |  ='S1_Enclosure_MountingPanel'  
  
### Note

The unit that is set in Pro Panel is always used for the specifications of length, height, width, etc.

The specification of an angle can be effected either in degrees or in radians (see [Unit for Angles](admin_r_modelvar_propanel_angle.htm)).

### Tip

The ID of an enclosure part, its mounting surface or the mounting surface of a device has the property 36035 Item ID (relative to macro) in Eplan Electric P8.

See also [Editing and displaying part placement properties](../../../../Plattform/2026/Content/htm/panellayoutgui_h_eigenschaftenartikelplatzierungenbearbeiten.htm)
