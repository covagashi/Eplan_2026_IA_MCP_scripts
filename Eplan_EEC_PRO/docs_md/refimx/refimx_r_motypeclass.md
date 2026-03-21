---
title: "\u003cmoTypeClass\u003e"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refimx_r_motypeclass.htm"
file: "refimx_r_motypeclass"
category: "refimx"
---

# \u003cmoTypeClass\u003e

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  <moTypeClass> IMX The tag <moTypeClass> defines the alias for the absolute name of a library component. The tag has no sub-elements. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
alias | required |  |  | Alias name for a library component.  
realName | required |  |  | Absolute name of a library component.  
[Example code](javascript:void\(0\);)
    
        <mapping>
    	<moTypeClass alias="Cylinder" realName="T_Mechatronic_ModularSystem.Mechatronic.Actuators.Cylinder"/>
    	<moTypeClass alias="Valve" realName="T_Mechatronic_ModularSystem.Mechatronic.Actuators.Valve"/>
    </mapping>
