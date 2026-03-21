---
title: "Parameterization with formulas"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_parameterizing_with_formulas.htm"
file: "eecbase_k_parameterizing_with_formulas"
category: "eecbase"
---

# Parameterization with formulas

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Parameterization with formulas

The use of formulas in library components allows for variants of components in the project to be calculated.

The formula is created directly in the parameter editor, in the Value column. When creating extensive formulas, it is recommended that the Formula editor view and / or modal formula editor be used. The modal formula editor is started by using the Popup menu > Open Formula editor. Both the Formula editor view as well as the modal formula editor support the user through syntax highlighting and Content Assist.

Related bracket pairs for the bracket types [ ], { } und ( ) are highlighted in the formula editor. To this purpose the cursor must be positioned in the formula editor after an opening or closing bracket in order to highlight the opposite bracket with a frame.

Only in the modal formula editor can you use the shortcut key Ctrl + F or use the Popup menu > Search/replace to search for a specific term and replace it with another term.

Using the key combination [Ctrl] \+ [Z], the last entry can be undone (UNDO), and restored (REDO) using the key combination [Ctrl] \+ [Y].

To develop a formula which delivers the expected result, you can proceed as follows:

    1. Open the project component, for which the formula is to be developed.
    2. Select the Value field of the corresponding parameter.
    3. Use the Formula editor for the development of the formula.

The result of the formula can be checked in the adjacent field Result.

If the calculated result corresponds to expectations, the formula is transferred to the library component using Popup menu > Move Formula to Library Component.

If it is a formula in a pre-instantiated library component, the formula is transferred into the superordinary library component using Popup menu > Move formula to Superordinary Library Component. In this case an interface formula (generally =mc.$<Parameter name>) is inserted in the parameter of the installed library component using Popup menu > Insert Interface Formula to Installed Library Component.

If it is a formula in a pre-instantiated project component, the formula is transfered into the installed library component using Popup menu > Move Formula to installed Library Component.

### Note

The Parameter editor in the project component must be saved to apply the changes and be able to see the effects.

With the  button you can stop and start the calculation of the formulas for mechatronic project components.

If the formula calculation is switched off, the renewed calculation of all parameters is not executed in the editor when a formula is being edited. The results already calculated are used for the calculation of the edited formula.

### Note

The  button is only displayed when the [de.eplan.eec.enableStartStopFormulaCalculation](admin_r_vmargs_enablestartstopformulacache.htm) runtime option is entered in the initialization file.
