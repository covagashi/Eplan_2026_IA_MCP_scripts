---
title: "hasRole(String role)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_system_hasrole.htm"
file: "refformulas_r_system_hasrole"
category: "refformulas"
---

# hasRole(String role)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  hasRole(String role) System methods Delivers true if the authorized EEC user has the assigned user role, otherwise false is delivered. **hasRole(String role)**  
---  
Argument | String | role | User role  
Return value | Boolean | true = user has the assigned user role  
false = user has another user role  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=if type('Engineering.System').hasRole('Administrator') then 'Access allowed' else 'Access denied! No authorization' endif | Access denied! No authorization
