---
title: "Selection formulas"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_variantmanagement_extensions_selection_formula.htm"
file: "eecbase_k_variantmanagement_extensions_selection_formula"
category: "eecbase"
---

# Selection formulas

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

## Selection formulas

For placeholders and extension points a selection formula can be specified (see the following figure), which determines during instantiation and / or updates which of the visible library components is to be instantiated. With manual configuration, the selection can be limited to a subset of the library components of the extension point.

The following rules apply to the calculation of the selection formula:

     * The selection formula yields a Boolean value or an integer:
       * true means that each possible component is instantiated exactly once and / or that the instance is retained.
       * false means that no component is instantiated and / or that the instance is deleted.
       * An integer specifies the number of components to be instantiated that correspond to the specified type. If a type is specified from which multiple types can be derived, the number of components is instantiated from each derived type.

### Note

Manual updating of the extension points:

If the number of components to be instantiated is larger than the specification for multiplicity allows, the instantiation is not performed. A corresponding error message is output.

Updating the extension points during the creation of a project:

If the number of components to be instantiated is larger than the specification for multiplicity allows, the instantiation is performed. It is recommended to check the model for validity by using the menu item Model > Validate model

     * The formula is evaluated in the context of the component to be instantiated, meaning as if the instance were installed at the extension point. All parameters of the instance can be accessed, as well as, of course, the enclosing component (mc). But it is not possible to access components contained in the instance (e.g., mos or rmos on the instance itself).
     * When the formula cache is enabled ([Engineering.StartFormulaCacheCommand](refcommands_r_engineering_startformulacachecommand.htm)), the result of the expressions used in the selection formula, rmos and mos, must not contain any objects inserted on extension points. If this cannot be avoided, the [Engineering.UpdateExtensionsCommand](refcommands_r_engineering_updateextensionscommand.htm) may have to be executed several times, or the formula cache has to be disabled ([Engineering.StopFormulaCacheCommand](refcommands_r_engineering_stopformulacachecommand.htm)).
     * Debugging:

If the selection formula does not yield a Boolean value, or if a formula error occurs, this will be displayed after updating the extension points: The affected library components are instantiated, and â in analogy to the Disabler â the result of the selection formula for this project component is displayed on the parameter page. The result can be analyzed with the formula inspector.

### Note

If the selection formula cannot determine a value, the placeholder and / or extension point will behave as if there is no selection formula.

The model variable Maximum Number Of Classes To Check For Placeholder Selection Formula defines a limit from which a warning will be issued. The warning alerts the user that the evaluation of the selection formula will take up a longer period of time. This happens when many library components correspond to the type of the extension point (e.g., if Engineering.Component is selected as the type). The selection formula must then be calculated for every possible library component.

### [Example](javascript:void\(0\);)

Selection formula:
    
        =mc.$SelectionConditionAndType.name.startsWith('A')

Here, instantiation is made dependent on a condition in the enclosing mechatronic component, combined with a class nomenclature.

### Note

When instantiating via Drag & Drop, the selection formula for the placeholder or extension point is not calculated during the drag process, so that the instantiation cannot be excluded. If the instantiated component contains further extension points with selection formulas, these will be evaluated.
