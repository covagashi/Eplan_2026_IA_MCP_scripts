---
title: "Support for placeholder objects with value sets"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_support_of_placeholder_with_valuesets.htm"
file: "eececad_k_support_of_placeholder_with_valuesets"
category: "eececad"
---

# Support for placeholder objects with value sets

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Support for placeholder objects with value sets

Requirements:

     * A parameter specification with the notation #<Parameter name> is inserted in the Name field in the Placeholder object tab.

### Note

No more than one parameter definition may be entered in the Name field of the placeholder object.

To define a value set, the name of the parameter has to be entered in the variant table and corresponding values have to be specified. When reading in the resource a parameter by the same name is generated, whose selection values correspond to the entries in the variant table.

If the assigned value set is missing, or EEC does not find the value set due to differing uppercase / lowercase spelling, an error message appears and the generation process is aborted.

During the generation of the schematics, the portion #<> of the parameter definition is removed from the placeholder name. For example, the name #<ValueSet> becomes the new name ValueSet.

If the model variable Write macro parameter structure in parameter is set to the value true, a parameter whose name is specified in the model variable Name of the parameter for the macro parameter structure is inserted in the discipline component when the macro is read in. The parameter stores a list of maps containing, among other things, the names of the existing value sets.

In the settings, it is possible to define that the macro boxes are retained so that the user has the macro-specific popup menu items (Update macro... etc.) available at the macro box. This option can be set separately for window macros and symbol macros. Both options are disabled by default.

Similarly you can specify the removal of placeholder objects created in the schematics in the settings.

### Read more

     * [Eplan Electric P8](admin_r_prefs_ecad_p8.htm)
     * [Parameter Name For The Macro Parameter Structure](admin_r_modelvar_p8macrodata.htm)
     * [Write Macro Parameter Structure In Parameter](admin_r_modelvar_p8writemacrostructure.htm)
     * [Creating Placeholder Objects](../../../Plattform/2025/Content/htm/macrosgui_h_platzhalterobjekteerzeugen.htm)
