---
title: "Disable components via disabler"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutmechatronic_h_disable_component.htm"
file: "tutmechatronic_h_disable_component"
category: "tutmechatronic"
---

# Disable components via disabler

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Disable components via disabler The presence of a component can be controlled via the so-called Disabler. If the condition entered here is true, the component will be disabled. For the example project, this means that disablers are set up for the function Functiongroups Inspect and Discard, for the sensors Position_2, Position_3, and Position_4 of the Axis function unit, and for the actuator Valve_2.
    1. Open the Feeder component.
    2. Click the Inspect component.
    3. In the Disabled field, enter the formula =not(mc.$Option_Inspect_available).
    4. Repeat the steps 1 to 3 for the Discard component.
With not, you negate the return value of the subsequent method mc.$Option_Inspect_available. Use this trick in order to apply, with the Option_Inspect_available parameter, positive logic (Option_Inspect_available = true: Inspect is enabled; Option_Inspect_available = false: Inspect is disabled). In the formula, mc (mechatronic component) refers to the (superordinate) mechatronic component â in this case, Feeder. From this, $Option_Inspect_available takes the value of the parameter of the same name. The point is used as the path separator, similar to the file path whose folders and subfolders are separated by slashes. Tip The input of formulas is simplified by a Content Assistant. For example, if you have written =not(mc., followed by [Ctrl] \+ [Space bar], possible additions are shown in a dialog. In many cases, values can be adopted from this dialog by selecting them, which simplifies manual input. For the axes, this has to be done for the position sensors Position_2, Position_3, and Position_4.
    1. Open the component Axis.
    2. In the editor, click the Position_2 component.
    3. In the Disabled field, enter the formula =not(mc.$Sensor_2_available).
    4. Repeat the previous steps for Position_3 with the formula =not(mc.$Sensor_3_available) and for Position_4 with =not(mc.$Sensor_4_available).
In the formula, mc (mechatronic component) references the superordinate component of the sensor, i.e., Axis. If after the point there were another mc, it would take you to a next higher level in the machine model for the Move Functiongroup, which uses Axis as the only component. In the subformula $Sensor_2_available, the dollar sign represents the parameter, followed by the parameter name, that is, the axis parameter Sensor_2_available. This subformula must be negated with the not function not() in order to obtain the correct value. The formula language is described in the section [Formulas](refformulas_r_formulas.htm). A disabler is also set up for the installed component Valve_2 of the component Cylinder.
    1. Open the component Cylinder.
    2. In the editor, click the Valve_2 component.
    3. In the Disabled field, enter the following formula =not(mc.$Sensor_Two_Valves).
