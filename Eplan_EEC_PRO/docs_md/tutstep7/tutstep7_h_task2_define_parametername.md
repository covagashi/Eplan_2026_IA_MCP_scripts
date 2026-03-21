---
title: "Defining parameter names for model variables"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task2_define_parametername.htm"
file: "tutstep7_h_task2_define_parametername"
category: "tutstep7"
---

# Defining parameter names for model variables

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Defining parameter names for model variables Model variables are required when creating the structure and the addresses. The names of the model variables for certain tasks are defined in EEC and parameters with the same names are created in the model. The values of these parameters influence the generation process. The model variables are defined as follows:
    1. Select Model > Model Variables to open the model variables.
    2. Click on the I/O Generator area.
3\. Define the following model variables: Name | Value | Description  
---|---|---  
Bit Range ParameterName | IO_BitRange | The name of the parameter that specifies the bit range of the bus.  
Incoming Bus Line Parameter Name | IO_IncomingBus | The name of the parameter that specifies the incoming bus of a controller device. Only the basic controller object has no incoming bus.  
Input Block Size Parameter Name | IO_InputBlockSize | The name of the parameter that specifies the input block size of a control device.  
Input Start Address Format Parameter Name | IO_InputStartAddressFormat | The name of the parameter that specifies the input start address format of a control device.  
Input Start Address Parameter Name | IO_InputStartAddress |   
Outgoing Bus Line Parameter Name | IO_OutgoingBus | The name of the parameter that specifies the outgoing bus of a control device.  
Output Block Size Parameter Name | IO_OutputBlockSize | The name of the parameter that specifies the output block size of a control device.  
Output Start Address Format Parameter Name | IO_OutputStartAddressFormat | The name of the parameter that specifies the output start address format of a control device.  
Output Start Address Parameter Name | IO_OutputStartAddress |   
Place Parameter Name | IO_Place | The name of the parameter that specifies the location of a control device.  
Places Parameter Name | IO_Places | The name of the parameter that specifies the locations that are searched using the sensors/actuators connected to the control device.
