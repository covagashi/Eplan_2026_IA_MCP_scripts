---
title: "Entering formulas for the parameters of the S7_313C component"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task2_insert_formulas1.htm"
file: "tutstep7_h_task2_insert_formulas1"
category: "tutstep7"
---

# Entering formulas for the parameters of the S7_313C component

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Entering formulas for the parameters of the S7_313C component The parameters of the S7_313C component require fixed values and formulas, with whose help the parameter values of the project components are determined.
    1. Open the S7_313C component.
    2. Open the Parameter editor.
    3. Enter the following formula for the Bit0_IX parameter:
    
        ='I' + $IO_InputStartAddress

    1. Repeat step 3 for the parameters Bit1_IX to Bit23_IX with the following formula (the bit address must be increased by 1 each time):
    
        ='I' + $IO_InputStartAddress.addressAdd(1, 0, 8)
    ...
    ='I' + $IO_InputStartAddress.addressAdd(23, 0, 8)

    1. Repeat step 3 for the parameter Bit0_QX with the following formula:
    
        ='O' + $IO_OutputStartAddress

    1. Repeat step 3 for the parameters Bit1_QX to Bit15_QX with the following formula (the bit address must be increased by 1 each time):
    
        ='O' + $IO_OutputStartAddress.addressAdd(1, 0, 8)
    ...
    ='O' + $IO_OutputStartAddress.addressAdd(15, 0, 8)

    1. Enter these fixed values for the following parameters:
Parameter name | Value  
---|---  
IO_BitRange | 8  
IO_InputBlockSize | 24  
IO_InputStartAddress | 0.0  
IO_InputStartAddressFormat | x.0  
IO_OutgoingBus | IO  
IO_OutputBlockSize | 16  
IO_OutputStartAddress | 0.0  
IO_OutputStartAddressFormat | x.0  
IO_Place | PLC  
IO_Places | PLC
