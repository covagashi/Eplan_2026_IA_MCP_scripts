---
title: "Parameter name for the C# script arguments"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_modelvar_p8scriptargs.htm"
file: "admin_r_modelvar_p8scriptargs"
category: "admin"
---

# Parameter name for the C# script arguments

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Parameter name for the C# script arguments

Path to model variable:

Disciplines > ECAD > Eplan Electric P8

Specify the name of a parameter. Add this parameter to the P8 discipline components of the WiringDiagram type. The value of the parameter in the discipline components defines a list of arguments that are passed to a C# script, for example [refreshFSÂ»true,widthÂ»35,lengthÂ»100].

Currently, the data types string and int are supported for the arguments of the Start method. The order of the arguments does not have to be followed, because the assignment is realized via the parameter names.

As a further option, the parameter refreshFS can be entered. If the value of the parameter is true, the internal file system of the EEC is synchronized after execution of the script.
