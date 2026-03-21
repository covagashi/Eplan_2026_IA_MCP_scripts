---
title: "Engineering.CreateInstanceCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_engineering_createinstancecommand.htm"
file: "refcommands_r_engineering_createinstancecommand"
category: "refcommands"
---

# Engineering.CreateInstanceCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Engineering.CreateInstanceCommand Creates a new instance. Due to the different execute methods the following scenarios are covered:  
    1. An instance of the given class will be created with the entered name under the specified component.
Argument | Type | Description  
---|---|---  
classToInstantiate | Object | Class to be instantiated.  
instantiationParent | Object | Parent component, under which the new instance will be created.  
The component itself or the absolute name of the component may be entered.  
instanceName | String | The new name of the instance. If the name already exists a name collision clearing is executed.  
    2. An instance of the specified class will be created with the given name under the specified component and the calculation of the extension point of the instance is controlled at the same time.
Argument | Type | Description  
---|---|---  
classToInstantiate | Object | Class to be instantiated.  
instantiationParent | Object | Parent component, under which the new instance will be created.  
The component itself or the absolute name of the component may be entered.  
instanceName | String | The new name of the instance. If the name already exists a name collision clearing is executed.  
instantiateExtensions | Boolean | The values true or false control the calculation of extensions in the new instance.  
    3. An instance of the given class will be created with the entered name under the specified component on the specified placeholder.
Argument | Type | Description  
---|---|---  
classToInstantiate | Object | Class to be instantiated.  
instantiationParent | Object | Parent component, under which the new instance will be created.  
The component itself or the absolute name of the component may be entered.  
instanceName | String | The new name of the instance. If the name already exists a name collision clearing is executed.  
placeholderName | String | The placeholder where the new component is placed.  
    4. An instance of the specified class will be placed with the given name under the specified component and the calculation of the extension point of the instance is controlled at the same time.
Argument | Type | Description  
---|---|---  
classToInstantiate | Object | Class to be instantiated.  
instantiationParent | Object | Parent component, under which the new instance will be created.  
The component itself or the absolute name of the component may be entered.  
instanceName | String | The new name of the instance. If the name already exists a name collision clearing is executed.  
instantiateExtensions | Boolean | The values true or false control the calculation of extensions in the new instance.  
placeholderName | Boolean | The values true or false control the calculation of extensions in the new instance.
