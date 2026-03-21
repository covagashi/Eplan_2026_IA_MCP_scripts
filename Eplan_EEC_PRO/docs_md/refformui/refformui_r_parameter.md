---
title: "Parameter"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_parameter.htm"
file: "refformui_r_parameter"
category: "refformui"
---

# Parameter

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Parameter An important aspect in the use of Form-UIs is the access to parameters and their stored values. Determine the parameter with a specific name: The method parameter('Place') returns as the result the parameter with the name Place, resp. null if the parameter does not exist Determine the parameter value: To access the parameter value, two equivalent notations are allowed, for example parameter('Place').value determines the stored value of the parameter Place as well as $Place. If the name of the parameter contains a character that the formula interprets as a delimiter, the notation parameter('<name>') should be used (also see [Dollar sign $](refformulas_r_project_components_dollar.htm)). Changing the value of the parameter: If it has to be possible for the value of a parameter to be not only displayed, but also changed, only the notation parameter('<name>').value is permitted.
