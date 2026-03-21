---
title: "Parameterizing of project components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_parameterizing_project_components.htm"
file: "eecbase_k_parameterizing_project_components"
category: "eecbase"
---

# Parameterizing of project components

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Parameterizing of project components

Project components can be parameterized to library components according to the definition, i.e., parameter values can be assigned. The 'Floor' component added for an IT_SolutionMap _Floor_ already has a number of parameter values. These are values already assigned in the library. They are imported into the Default field as default settings:

The Parameter editor page of a project component is structured in a way similar to the editor page of the library component. In additional, there is a further field Result. The result is calculated from the Value field. If it is empty, the value is taken from the Default field.

Project-specific parameter values can be assigned in the Value field. Any existing default values will be overwritten. The result will be adjusted accordingly. For example, if the floor number is given as A 0, but A 4 is desired, A 4 will be entered in the Value field of the corresponding parameter. This can be seen in the above figure.

Thus, the default value of the Number parameter is overwritten, and represented in the Result field.

Parameter values can also be calculated using formulas. This way, no manual entry would be required. In this case formulas are entered in the Value field, and the result is calculated automatically.

The precise usage of formulas and their syntax are described in the section [Formula language]().
