---
title: "ECAD3D structure"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecpropanel_k_ecad3d_structure.htm"
file: "eecpropanel_k_ecad3d_structure"
category: "eecpropanel"
---

# ECAD3D structure

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## ECAD3D structure

The structure of the components is stored internally in the ECAD3D discipline. The following level structure applies:

All the components of the lowest level can be installed into each other.

The ECAD3D library is required in order to expand a modular system to include Pro Panel objects. This library provides all discipline components as well as parameter types.

The ECAD3D library makes the following components available:

Type | Description  
---|---  
LayoutSpace | Three-dimensional installation space, in which the switching cabinet is placed. Can be exported as a 3D graphics macro.  
Enclosure | Enclosure  
EnclosurePart | Switching cabinet part, e.g. door  
Plane | Mounting surface, e.g. outside of the door  
MountingPanel | Mounting panel in the switching cabinet  
FreeMountingPanel | Mounting panel without switching cabinet  
Area | Locked area for cut-outs or placement of devices  
Cutout | Cutout, drill hole or threaded hole  
WireDuct | Wire duct (goods sold by the meter)  
MountingRail | Mounting rail (goods sold by the meter)  
BusBarSystem | Busbar system  
Device | Component, e.g. terminal clamp, for further differentiation, see components for placement  
  
### Read more

     * [Parameter](eecpropanel_k_parameter.htm)
