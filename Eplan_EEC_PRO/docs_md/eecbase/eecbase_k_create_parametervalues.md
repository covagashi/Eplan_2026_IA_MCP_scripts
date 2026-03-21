---
title: "Parameter values specified"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_create_parametervalues.htm"
file: "eecbase_k_create_parametervalues"
category: "eecbase"
---

# Parameter values specified

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

## Parameter values specified

You specify a default value for the parameter on the Formula editor page. The default value is either a fixed value or a formula that calculates a value at runtime.

To specify a default value:

    1. Open the Formula editor page.
    2. Enter a fixed value or a formula in the Value field.
    3. Save with [Ctrl] \+ [S] or .

The validity of the values to be entered can be checked by means of a formula in the Formula field. If a given value is not valid, the result field is highlighted in yellow and a message is entered in the message log with the text of the Warning field.

To specify a validity check:

    1. Open the Formula editor page.
    2. Enter a formula for the validity check in the Formula field.
    3. Enter an information text into the Warning field.
    4. Save with [Ctrl] \+ [S] or .

### [Example](javascript:void\(0\);)

The following formula checks whether the entered value lies between 50 and 100:
    
        =this.value < 100 and this.value > 50

### Note

The Observe conditions when checking formula results option in the settings must be activated in order for the conditions to be checked for valid values (see [Preferences for validation](admin_r_prefs_validation.htm)).

If only certain parameters are to be selectable, they can be created in the table Selection values.

To create selection values:

    1. Open the Formula editor page.
    2. Click  for each selection value.
    3. Enter the selection values in the table.
    4. Save with [Ctrl] \+ [S] or .

### Note

When creating selection values, the usual shortcut keys for Copy / Cut / Paste are not supported. These functions are available only through the popup menu.
