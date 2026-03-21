---
title: "isUser(String name)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_system_isuser.htm"
file: "refformulas_r_system_isuser"
category: "refformulas"
---

# isUser(String name)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  isUser(String name) System methods Delivers true if the authorized EEC user is equal to the assigned user, otherwise false is delivered. **isUser(String name)**  
---  
Argument | String | name | User name  
Return value | Boolean | true = user has the assigned name  
false = user has another name  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
if type('Engineering.System').isUser('MyName') then 'MyName' else 'OtherName' endif | OtherName
