---
title: "Create parameter"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_create_parameter.htm"
file: "eecbase_k_create_parameter"
category: "eecbase"
---

# Create parameter

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Create parameter

You create parameters within a library. To organize the parameters, you can create any structures using units. You create a new parameter via the popup menu of a unit or another object.

Parameters are typed, i.e., there are different types of parameters that differ from each other in terms of the values assigned to them. For example, there are parameters for integers, strings or truth values (Boolean). To distinguish between two variants, one truth value will be enough, that is, a parameter of the Boolean type, which can assume the two values true or false.

To create a new parameter:

    1. Call up the popup menu of a library or a unit and select New > Engineering > Parameter.

    1. Enter a name for the new parameter.

### Note

The name of a new object should not contain a special character (){}[].:,;-/\Â§$%&#~<>|= so that on the one hand it is file system-compliant and on the other hand no problems occur during the creation of formulas.

    1. Enter a type or select a type via [..].
    2. Enter a comment optionally.
    3. Save with [Ctrl] \+ [S] or .

The component is created as a result of the assignment of a name and subsequently the saving of the editor. Without a valid name the name field is highlighted in red. A name must be unique within a unit.

If a given value does not conform to the type of the parameter, the result field is highlighted in red and a corresponding message is entered in the message log.
