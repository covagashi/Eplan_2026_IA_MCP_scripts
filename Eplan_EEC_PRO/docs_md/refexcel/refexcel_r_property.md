---
title: "\u003cproperty\u003e"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refexcel_r_property.htm"
file: "refexcel_r_property"
category: "refexcel"
---

# \u003cproperty\u003e

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  <property> The <property> tag fills a parameter whose name is specified with the key attribute with the value of the value attribute. The parameter must be located in the parent component. The tag has no sub-elements. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
key | required |  |  | Specifies the name of the parameter.  
value | required |  |  | Specifies the value of the parameter.  
[Example](javascript:void\(0\);) For this example, the modular system of the tutorial can be used. No modifications are permissible therein: Content of the Excel table: The worksheet name for this example must be named Mechatronic. | ParameterName | ParameterValue  
---|---|---  
1 | Option_Inspect_Available | true  
Schema file content:
    
        <?xml version="1.0" encoding="UTF-8"?>
    <schema tableName="Mechatronic" >
    	<node id="Station" name="Feeder" typeClass="T_Mechatronic_ModularSystem.Stations.Feeder">
    		<properties>
    			<property key="${ParameterName}" value="${ParameterValue}" />
    		</properties>
    	</node>
    </schema>

Template file content:
    
        <?xml version="1.0" encoding="UTF-8"?>
    <imx xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xi="http://www.w3.org/2001/XInclude" version="1.0">
    	<project name="Feeder" save="true">
    		<libraries>
    			<add type="String" value="T_Mechatronic_ModularSystem"/>
    		</libraries>
    		<importFragment/>
    	</project>
    </imx>

Result: By means of the Schema file the specification tableName ="Mechatronic" the Excel worksheet named Mechatronic is evaluated. The specification of the component, which contains the parameter, is given by the <node> tag with name ="Feeder". If the component is not existing, it is created as an instance of typeClass="T_Mechatronic_ModularSystem.Stations.Feeder". The <property> tag specifies with key="${ParameterName}", that the column named ParameterName contains the name of the parameter and with value="${ParameterValue}", that the column named ParameterValue contains the parameter value. By means of these specifications the parameter Option_Inspect_available is set to the value true.
