---
title: "\u003cmo\u003e"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refimx_r_mo.htm"
file: "refimx_r_mo"
category: "refimx"
---

# \u003cmo\u003e

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  <mo> IMX The tag <mo> addresses an existing project component or creates a new project component. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
name | required |  |  | Specifies the name of the existing or new project component. The name is interpreted relative to the parent project component.  
calcExtensions | optional | off, oneLevel, allLevels | off | Enables the update of extension points.  
off = Extension points are not updated.  
oneLevel = The extension point in the component of the current <mo> tag is updated. The update does not affect resulting child components with extension points.  
allLevels = The extension point in the component of the current <mo> tag is updated. The update affects all resulting child components with extension points.  
typeClass | required |  |  | Absolute name of the library component from which an instance is inserted into the project.  
save | optional | true, false | true | true = saves the project component after creation.  
false = the project component is not saved.  
Allowed sub-elements | Quantity  
---|---  
[<mo>]() | any  
[<parameter>](refimx_r_parameter.htm) | any  
[Example code](javascript:void\(0\);)
    
        <mo name="Feeder02" typeClass="T_Mechatronic_ModularSystem.Stations.Feeder" save="true">
    	<parameter name="Option_Inspect_available" type="Boolean" value="true"/>
    </mo>
