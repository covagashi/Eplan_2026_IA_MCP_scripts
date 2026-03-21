---
title: "Installing and configuring the fragment FR_SymbolTable in actuators and sensors"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task3_insert_fr_symboltable_1.htm"
file: "tutstep7_h_task3_insert_fr_symboltable_1"
category: "tutstep7"
---

# Installing and configuring the fragment FR_SymbolTable in actuators and sensors

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Installing and configuring the fragment FR_SymbolTable in actuators and sensors The fragment FR_SymbolTable is installed in all actuators and sensors and the parameters contained therein are provided with values.  
    1. Open the component Valve in the Actuators unit.
    2. Drag the fragment FR_SymbolTable from the Step7 unit into the component editor.
    3. Select the installed fragment FR_SymbolTable.
    4. Enter the following formulas and values for the parameters:
Parameter | Value  
---|---  
Symbol | =mc.$Symbol  
Address | =mc.$Bit0_QX  
DataType | BOOL  
Comment | =mc.mc.mc.name+'_'+mc.mc.name+'_'+mc.name  
    1. Repeat steps 1 to 4 for the components Position sensor_inductive, Position sensor_optical, and Pressure sensor and enter the following formulas and values for the parameters:
Parameter | Value  
---|---  
Symbol | =mc.$Symbol  
Address | =mc.$Bit0_IX  
DataType | BOOL  
Comment | =mc.mc.mc.name+'_'+mc.mc.name+'_'+mc.name
