---
title: "ECAD objects as components of mechatronics objects"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_ecad_objects_as_components_of_mechatronic_objects.htm"
file: "eececad_k_ecad_objects_as_components_of_mechatronic_objects"
category: "eececad"
---

# ECAD objects as components of mechatronics objects

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## ECAD objects as components of mechatronics objects

ECAD objects can be integrated directly into mechatronics objects. This way, mechatronics objects bring with them the corresponding electro-technical objects at the instantiation.

To utilize this mechanism, the electro-technical objects are added to the mechatronics (library) objects as components.

The following figure shows the mechatronics object Lights and its components. One can see that the mechatronics object brings with it the components Lights, as well as the mechatronics objects Lamp1 to Lamp4.

Parameter values that are calculated in the discipline structure result in formula errors during the configuration because the discipline structure does not yet exist at this point.

In order to avoid these formula errors, it is good practice to insert each discipline component into an "own" mechatronics component. This allows every parameter value required to already be calculated and transferred to the installed discipline component in the mechatronics structure.

The following figure illustrates this using the pressure sensor from the tutorial as an example:

    1. Originally all the parameters for the installed discipline component Sensor_Pressure were calculated in the discipline component.
    2. These parameters are now calculated in the mechatronics component. In this case the formulas are less complicated because it is not necessary to reference from the discipline structure into the mechatronical structure (with origin).
    3. The discipline component now obtains the parameter values from the mechatronics component in which it is installed (with mc.$Parametername).
