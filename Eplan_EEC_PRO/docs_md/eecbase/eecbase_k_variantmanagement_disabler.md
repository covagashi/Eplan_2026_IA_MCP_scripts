---
title: "Disabler"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_variantmanagement_disabler.htm"
file: "eecbase_k_variantmanagement_disabler"
category: "eecbase"
---

# Disabler

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Disabler

A very common form of variant management is the working with maximum specifications of machines and plants. A project with maximum configuration serves as the template here. Components not needed are deleted and / or disabled in the specific project.

EEC supports this approach through the Disabler concept. A disabler allows mechatronic and discipline-specific components to be disabled (not deleted). Individual components are disabled on the basis of parameter values, wit a disabler being either true or false.

### Note

By disabling via disablers, the components are preserved in the model, but they are left out from the calculation of formulas, for example, by way of mos, rmos, etc. This filtering in the calculation of formulas requires increased computation capacity, which can cause noticeable deceleration in the case of very extensive models. In such cases, one must check whether variant management should be realized via extension points rather than disablers.

Each mounted component has a disabler. In the following figure of the tutorial model, one can see that the feeder can be equipped with an inspection unit (Inspect). The inspection unit exists by default, but it can be disabled in the project via the evaluation of the formula of the disabler.

In this example, it is specifically the $Option_Inspect_available parameter that is evaluated.

If the parameter value is false, the result is a machine type that does not contain the inspection unit; see the following figure:

The evaluation of all disabler formulas in a model can be converted from negative to positive logic via the model variables Use positive logic in component activation formula. The following figure shows the conversion of the model variables:
