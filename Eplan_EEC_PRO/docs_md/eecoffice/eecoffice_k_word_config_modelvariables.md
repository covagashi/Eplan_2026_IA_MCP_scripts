---
title: "Model variables"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecoffice_k_word_config_modelvariables.htm"
file: "eecoffice_k_word_config_modelvariables"
category: "eecoffice"
---

# Model variables

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

Model variables

## Model variables

Word offers the following model variables, which can be used to change how the system behaves when reading in new resources.

     * [Opening Token For Parameter Replace Sequence](admin_r_modelvar_office_word_openingtoken.htm)
     * [Closing Token For Parameter Replace Sequence](admin_r_modelvar_office_word_closingtoken.htm)
     * [Create Parameters On Demand](admin_r_modelvar_office_word_createparameter.htm)
     * [Create Parameter Types On Demand](admin_r_modelvar_office_word_createparametertype.htm)
     * [Word Parameter Unit](admin_r_modelvar_office_word_parameterunit.htm)
     * [Create parameter units on demand](admin_r_modelvar_office_word_createparaunit.htm)
     * [Manage Resources Internally](admin_r_modelvar_office_word_resources.htm)

The following conditions apply to the opening and closing tokens of the parameter sequence:

     * The (*{ sequence may not be used for the opening token.
     * The }*) sequence may not be used for the closing token.

If the parser reads in a parameter sequence, the following actions are executed:

     * Create the parameter unit, if required (default is Word.Parameter).
     * Create the parameter types, if required (default is false).
     * Create the parameter, if required (default is false).
     * Storing the resources (default is false).
