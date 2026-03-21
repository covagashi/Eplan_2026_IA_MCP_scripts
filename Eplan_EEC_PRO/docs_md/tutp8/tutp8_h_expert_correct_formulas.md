---
title: "Modifying the formulas"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutp8_h_expert_correct_formulas.htm"
file: "tutp8_h_expert_correct_formulas"
category: "tutp8"
---

# Modifying the formulas

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Modifying the formulas New formulas are necessary due to the encapsulation of the discipline components and the usage of interface parameters. [The formulas for component M_Schematic](javascript:void\(0\);)
    1. Open the component M_Schematic.
    2. Switch to the Parameter editor page.
    3. Enter the following value for the FunctionDesignation parameter:
    
        =mc.$FunctionDesignation

    1. Save the component.
The formula =mc.$FunctionDesignation requires that a FunctionDesignation parameter exists in the higher-level component, meaning the Feeder component and that it supplies a suitable value. This parameter must still be inserted in the Feeder and have a value assigned to it. [Creating the FunctionDesignation parameter and inserting it into Feeder](javascript:void\(0\);)
    1. Mark the Mechatronic.Parameter unit in the T_Mechatronic_ModularSystem library.
    2. Select New > Engineering > Parameter.
    3. Specify the FunctionDesignation name.
    4. Specify the String type.
    5. Save the parameter.
Insert the FunctionDesignation parameter into the Feeder component.
    1. Open the Feeder component.
    2. Open the Parameters editor page.
    3. Drag the Plant parameter from the Parameter unit into the editor page.
    4. Enter the ='Feederâ formula as the value.
    5. Save the component.
[Modifying the formulas for the component M_SchematicPage](javascript:void\(0\);)
    1. Open the component M_SchematicPage.
    2. Switch to the Parameter editor page.
    3. Enter the following values for the parameters:
Name | Value  
---|---  
Functiontext1 | =if (mroot.mos('ISensor',4).size > $PageNo * 8 + 0) then mroot.mos('ISensor',4).at($PageNo * 8 + 0).$Functiontext else '' endif  
Functiontext2 | =if (mroot.mos('ISensor',4).size > $PageNo * 8 + 1) then mroot.mos('ISensor',4).at($PageNo * 8 + 1).$Functiontext else '' endif  
Functiontext3 | =if (mroot.mos('ISensor',4).size > $PageNo * 8 + 2) then mroot.mos('ISensor',4).at($PageNo * 8 + 2).$Functiontext else '' endif  
Functiontext4 | =if (mroot.mos('ISensor',4).size > $PageNo * 8 + 3) then mroot.mos('ISensor',4).at($PageNo * 8 + 3).$Functiontext else '' endif  
Functiontext5 | =if (mroot.mos('ISensor',4).size > $PageNo * 8 + 4) then mroot.mos('ISensor',4).at($PageNo * 8 + 4).$Functiontext else '' endif  
Functiontext6 | =if (mroot.mos('ISensor',4).size > $PageNo * 8 + 5) then mroot.mos('ISensor',4).at($PageNo * 8 + 5).$Functiontext else '' endif  
Functiontext7 | =if (mroot.mos('ISensor',4).size > $PageNo * 8 + 6) then mroot.mos('ISensor',4).at($PageNo * 8 + 6).$Functiontext else '' endif  
Functiontext8 | =if (mroot.mos('ISensor',4).size > $PageNo * 8 + 7) then mroot.mos('ISensor',4).at($PageNo * 8 + 7).$Functiontext else '' endif  
Input1 | ='I' + $PageNo + '.0'  
Input2 | ='I' + $PageNo + '.1'  
Input3 | ='I' + $PageNo + '.2'  
Input4 | ='I' + $PageNo + '.3'  
Input5 | ='I' + $PageNo + '.4'  
Input6 | ='I' + $PageNo + '.5'  
Input7 | ='I' + $PageNo + '.6'  
Input8 | ='I' + $PageNo + '.7'  
PageDescription | ='PLC_Sensors_' + ((($PageNo + 1) * 8) - 7) + '_' + (($PageNo + 1) * 8)  
PageNo | =$PageNumber.asInteger -1  
PageNumber | =mc.mos('ISchematicPage').indexOf(this) +1  
FunctionDesignation | =mc.$FunctionDesignation  
    1. Save the component.
[Modifying the formulas for the components M_Sensor_Inductive, M_Sensor_optical and M_Sensor_Pressure](javascript:void\(0\);)
    1. Open the component M_Sensor_Inductive.
    2. Switch to the Parameter editor page.
    3. Enter the following values for the parameters:
Name | Value  
---|---  
DT | ='S' + ($Sensors.indexOf(origin.ifNull(this))+1)  
Functiontext | =mc.absoluteName.substring(mroot.absoluteName.size+1, mc.absoluteName.size - 1).replaceAll('\\\\.',' ')  
IP | ='I' + (mroot.mos('ISensor',4).indexOf(this) / 8) + '.' + mroot.mos('ISensor',4).indexOf(this).mod(8)  
Sensors | =mroot.rmos('ISensor')  
    1. Save the component.
    2. Repeat Steps 1 to 4 for the components M_Sensor_optical and M_Sensor_Pressure.
