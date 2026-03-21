---
title: "Support for variants of window macros"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_support_of_window_macro_variants.htm"
file: "eececad_k_support_of_window_macro_variants"
category: "eececad"
---

# Support for variants of window macros

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Support for variants of window macros

Window macros with all representation types and variants are supported. Window macros are identified by the representation type (Neutral, Single-Line, Multi-Line, Graphic, etc.) and the variant (A, B, C, etc.). Corresponding model variables exist for these parameters. When importing a window macro, the parameters Representation type and Variant are generated, provided they exist in the window macro. A Selection value is created for the parameter of the variants for each available variant.

The use of window macros has the advantage that only one discipline component with one resource has to be created. In the parameter view of the discipline component, the parameters Representation type and Variant (if available) must be added, and, for example, filled with a permissible value via a formula.

### Note

The same parameters should be created in all variants of a window macro, because formulas that reference missing parameters of a variant would otherwise cause aborting during generation of the schematic.

### Note

During the synchronization of the external resource, EEC collects all the parameters from all variants. It is not an error if a parameter of the same type appears in different variants. If it is missing from a variant, it is not an error either.

If during the generation process EEC finds a window macro with several variants, it will use the model variables Name Of The Parameter For The Representation Type of Window Macros and Name Of The Parameter For The Variant of Window Macros in order to select the correct variant. If these model variables are not specified, the generation process is terminated, and a corresponding error message is shown.

### Read more

     * [Parameter Name For The Window Macro Variant](admin_r_modelvar_p8variant.htm)
     * [Parameter Name For The Window Macro Representation Type](admin_r_modelvar_p8representationtype.htm)
