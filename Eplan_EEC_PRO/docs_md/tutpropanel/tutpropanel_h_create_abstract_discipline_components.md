---
title: "Creating abstract discipline components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutpropanel_h_create_abstract_discipline_components.htm"
file: "tutpropanel_h_create_abstract_discipline_components"
category: "tutpropanel"
---

# Creating abstract discipline components

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Creating abstract discipline components Devices, terminals and cable ducts are used in different versions. For these discipline components you first create abstract discipline components and from there the different versions are derived. See [Creating discipline components](eecbase_k_create_discipline_component.htm) Create the following abstract discipline components in the ECAD.ProPanel unit: Name |  Super class |  Parameter  
---|---|---  
abstractCableDuct | WireDuct |  Coordinate Dimension EPN Id Plug  
abstractDevice | Device |  Coordinate DeviceTag DT_Code DT_Counter EPN Mate Plug Position Width  
abstractTerminal | Device |  Coordinate EPN Plug Position
