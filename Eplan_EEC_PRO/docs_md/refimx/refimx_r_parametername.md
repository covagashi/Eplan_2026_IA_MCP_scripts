---
title: "\u003cparameterName\u003e"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refimx_r_parametername.htm"
file: "refimx_r_parametername"
category: "refimx"
---

# \u003cparameterName\u003e

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  <parameterName> IMX The tag <parameterName> defines the alias for the absolute name of a parameter. The tag has no sub-elements. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
alias | required |  |  | Alias name of a parameter.  
realName | required |  |  | Absolute name of a parameter.  
[Example code](javascript:void\(0\);)
    
        <mapping>
    	<parameterName alias="Plug" realName="T_Mechatronic_ModularSystem.Parameter.Plug"/>
    	<parameterName alias="Socket" realName="T_Mechatronic_ModularSystem.Parameter.Socket"/>
    </mapping>
