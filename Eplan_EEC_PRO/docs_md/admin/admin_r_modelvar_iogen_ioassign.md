---
title: "Name of the parameter for the I/O assignment"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_modelvar_iogen_ioassign.htm"
file: "admin_r_modelvar_iogen_ioassign"
category: "admin"
---

# Name of the parameter for the I/O assignment

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Name of the parameter for the I/O assignment

Path to model variable:

Disciplines > IO Generator

Specify the name of a parameter. Add this parameter to the PLC discipline components. The value of the parameter in the discipline components defines whether the input/output addresses can be assigned to different input/output cards.

Possible parameter values are:

     * free: The assignment is free, meaning that the addresses of the sensors and actuators can be assigned to different input and output cards. This mode is the default behavior when a sensor or actuator does not dispose of the parameters for the I/O assignment. The Free mode creates the addressing previously carried out by the IO Generator.
     * IO separate: If a component disposes of both input and output signals, all the inputs are assigned to the same input card and all the outputs assigned to the same output card in this mode.
     * IO combined: If a component disposes of both input and output signals, all the inputs and outputs are assigned to the same control card in this mode. In this case the control card must offer both input and output addresses.
