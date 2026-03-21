---
title: "\u003cparameter\u003e"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refimx_r_parameter.htm"
file: "refimx_r_parameter"
category: "refimx"
---

# \u003cparameter\u003e

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  <parameter> IMX The <parameter> tag writes a value into the parameter of the project component specified in the parent tag. The type and value of the parameter can be passed directly as attributes or in the child tag <value>. To write a component as a value in a parameter, the parameter must be of the Component type or a type derived from it. If a different type is specified, the value is stored as <<null>>. The path to a component below Mechatronics or Mechatronic starts with a period (.), e.g. .Feeder.Move. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
name | required |  |  | Specifies the name of the parameter. The name is interpreted relative to the parent project component.  
type | optional | String, Boolean, Integer, Double, Object, Formula | String | Specifies the type of the parameter value. If type is not specified, the value is converted into type String.  
value | optional |  |  | Specifies the value of the parameter.  
Allowed sub-elements | Quantity  
---|---  
[<value>](refimx_r_value.htm) | any  
[Example code](javascript:void\(0\);)
    
        <mo name="Feeder02" typeClass="T_Mechatronic_ModularSystem.Stations.Feeder" save="true">
    	<parameter name="Option_Inspect_available" type="Boolean" value="true"/>
    	<parameter name="Additional_Move_Object" type="Object" value=".Feeder02.Move"/>
    </mo>

Description: For the component Feeder02 the value true is assigned to the Option_Inspect_available parameter. In addition the Move object of the component Feeder02 is assigned to the Additional_Move_Object parameter as the value.
