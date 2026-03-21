---
title: "Model variables for the IO generator"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_modelvariables_for_io_generator.htm"
file: "eecplc_k_modelvariables_for_io_generator"
category: "eecplc"
---

# Model variables for the IO generator

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Model variables for the IO generator

Only three basic objects are required to represent all of the components in a piece of PLC hardware. The user must furnish them with different default parameters - especially if automatic and dynamic calculation of addresses by the so-called IO generator is desired. Four of these parameters control structure formation, while the others are responsible for creating addresses. The IO generator creates the start addresses for the input and output groups based on the defined structure.

The functioning and parameterization of the IO generator is admittedly not described here. However, its parameters may also be of interest to other areas of the PLC discipline, which is why their definitions and usage are mentioned here once again. The names of the default parameters are stored as a model variable.

Parameters for structure formation:

     * IncomingBus: The name of the parameter that specifies the incoming bus of a controller device. Only the basic controller object has no incoming bus.
     * OutgoingBus: The name of the parameter that specifies the outgoing bus of a control device.
     * Location: The name of the parameter that specifies the location of a control device.
     * Locations: The name of the parameter that specifies the locations that are searched using the sensors/actuators connected to the control device.

Parameters for address generation:

     * InputStartAddressFormat, OutputStartAddressFormat: The name of the parameter that specifies the input or output start-address format of a control device.
     * InputBlockSize, OutputBlockSize: The name of the parameter that specifies the input or output block size of a control device.
     * BitArea: The name of the parameter that specifies the bit area (e.g. 8 or 16) of a control device.
     * InputStartAddress, OutputStartAddress: The name of the parameter that specifies the input start-address of a control device. The value of this parameter is calculated by the IO generator.
     * IOAssignment: Name of the parameter for the I/O assignment. The value of the parameter determines whether the inputs or outputs of sensors and actuators may be assigned to different input and output cards.  
Three modes are differentiated:
       * free: The assignment is free, meaning that the addresses of the sensors and actuators can be assigned to different input and output cards. This mode is the default behavior when a sensor or actuator does not dispose of the parameters for the I/O assignment. The Free mode creates the addressing previously carried out by the IO Generator.
       * IO separate: If a component disposes of both input and output signals, all the inputs are assigned to the same input card and all the outputs assigned to the same output card in this mode.
       * IO combined: If a component disposes of both input and output signals, all the inputs and outputs are assigned to the same control card in this mode. In this case the control card must offer both input and output addresses.

In the case of components that only dispose of inputs and outputs the IO_separate and IO_combined modes result in the same addressing.
