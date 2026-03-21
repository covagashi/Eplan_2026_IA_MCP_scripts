---
title: "property(String key)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_system_property.htm"
file: "refformulas_r_system_property"
category: "refformulas"
---

# property(String key)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  property(String key) System methods The property method allows accessing to the values of the parameters that were passed in the call of the WebEEC page. This way you can pass the available data of a superior system to the EEC model. Syntax:  
      
        http://<host>:<port>?<parameter_name_1>=<value>&<parameter_name_x>=<value>

**property(String key)**  
---  
Argument | String | key | Key, whose value should be returned.  
Return value | String | The value of the key  
[Examples](javascript:void\(0\);) In this example the values of the parameters orderno and type are passed via Web call.
    
        http://<host>:<port>?orderno=996633&type=N36M45

Formula to read out the URL parameter orderno in the EEC_Model:
    
        =type('Engineering.System').property('orderno')

Formula to read out the URL parameter type in the EEC_Model:
    
        =type('Engineering.System').property('type')

For the model development you can simulate web calls by means of entries in the initialization file (ec.ini). The parameter passing follows in the initialization file of this syntax: -Dcom.mind8.rap.<parameter_name>=<value> To simulate the parameter passing of the example above the names of entries in the initialization file (ec.ini) are as follows:
    
        -Dcom.mind8.rap.orderno=996633
    -Dcom.mind8.rap.type=N36M45
