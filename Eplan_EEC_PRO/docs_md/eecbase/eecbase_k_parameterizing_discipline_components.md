---
title: "Parameterization of discipline components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_parameterizing_discipline_components.htm"
file: "eecbase_k_parameterizing_discipline_components"
category: "eecbase"
---

# Parameterization of discipline components

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Parameterization of discipline components

Using discipline-specific components, project-specific parameters can be created in the project documents. In the following figure, the $ProjectID parameter exists in the resource as a placeholder. During the generation, this will be replaced by the specific project parameter. The project parameter is set on the Parameters editor page.

Parameterization is carried out via the Parameters editor page. Apart from its type property, each parameter also has the fields Value, Default, Standardized, Type, Declared in and Comment:

The Value field describes the value of the parameter that the field is to assume when the component is integrated into a project. This value is assigned as a default value.

The Default field in this specific case is not filled. Its function is explained in Advanced Workflows.

The Standardized field is to tell the user in the project whether this parameter is to be configured by him or her or whether it should not be edited. The Standardized field can be filled with two values, true and false. If a parameter is standardized, the parameter is grayed out in the project. But it can still be overwritten.

The Type field identifies the type of the parameter.

The Declared in field shows the object in which the parameter is declared.

In the Comment field, a comment can be entered on the use or meaning of the parameter.

If a component, parameterized in the library, is integrated, the contents in the Value field provide the default values.
