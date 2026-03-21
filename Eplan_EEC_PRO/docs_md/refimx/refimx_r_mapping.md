---
title: "\u003cmapping\u003e"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refimx_r_mapping.htm"
file: "refimx_r_mapping"
category: "refimx"
---

# \u003cmapping\u003e

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  <mapping> The tag <mapping> makes it possible to use an alias instead of the absolute name of a library component, a parameter or commands. When reading the IMX file alias names are replaced by absolute names. The tag has no attributes. Allowed sub-elements | Quantity  
---|---  
[<moTypeClass>](refimx_r_motypeclass.htm) | any  
[<parameterName>](refimx_r_parametername.htm) | any  
[Example code](javascript:void\(0\);)
    
        <mapping>
    	<moTypeClass alias="Cylinder" realName="T_Mechatronic_ModularSystem.Mechatronic.Actuators.Cylinder"/>
    	<moTypeClass alias="Valve" realName="T_Mechatronic_ModularSystem.Mechatronic.Actuators.Valve"/>
    </mapping>
