---
title: "Use formulas for plugs, sockets, and PLC inputs"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutp8_h_assign_formulas_to_plugs_sockets_plc_inputs.htm"
file: "tutp8_h_assign_formulas_to_plugs_sockets_plc_inputs"
category: "tutp8"
---

# Use formulas for plugs, sockets, and PLC inputs

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Use formulas for plugs, sockets, and PLC inputs Before using the formula for calculating the plug parameter values, the fixed values have to be deleted first.
    1. In the Project Catalog open the Feeder component.
    2. Set the Option_Inspect_available parameter to true.
    3. Open the Mechatronic structure.
    4. For each sensor, delete the value of the IP parameter.
An abstract sensor is required so that the formula for the plug parameter has to be defined only in one location. The concrete sensors are then derived from the abstract sensor and inherit amongst other its parameters. In the ECAD.PLC_Inputs unit create the abstract sensor with the name abstract_Sensor with the Fragment superclass. See [Creating discipline components](eecbase_k_create_discipline_component.htm). Assign the abstract_Sensor class as the super class to the three sensors:
    1. Open Sensor_Pressure.
    2. In the Super class field, select abstract_Sensor.
    3. Repeat Steps 1 to 2 for the sensors Sensor_optical and Sensor_Inductive.
The abstract sensor requires a parameter that stores a list of sensors as well as a parameter for the function text. In the ECAD.Parameter unit create a parameter with the name Sensors and the type Collection, as well as a parameter with the name Functiontext and the type String. See [Create parameter](eecbase_k_create_parameter.htm). Assign the parameters IP, DT, Sensors and Functiontext to the abstract sensor:
    1. Open the abstract_Sensor class.
    2. Open the Parameters editor page.
    3. Add the parameters IP, DT and Sensors.
    4. In the Value field enter the following formula for the IP parameter:
        
                ='I' + ($Sensors.indexOf(origin.ifNull(this)) /8) + '.' + $Sensors.indexOf(origin.ifNull(this)).mod(8)

    5. This formula combines the various parts of a plug parameter. As such, the letter âIâ is assembled with two values that are separated by â.â. The first value is the position of the sensor in the list divided by 8. The second value is the position of the sensor in the list modulo 8.
    6. Enter the following formula for the Sensors parameter:
        
                =mroot.rmos('T_Mechatronic_ModularSystem.ECAD.PLC_Inputs.abstract_Sensor')

    7. This formula is used to determine a list of all subordinate components of the abstract_Sensor type.
At a later point you enter a formula for the DT parameter. The calculation of the socket parameters on the pages requires a parameter that contains the page number. Create the Page parameter of the String type in the ECAD.Parameter unit, and assign this parameter to the abstract_Page page. The parameter is inherited to the Page subclass. Formulas have to be entered in the abstract page for the values of the Page and PageDescription parameters. The formulas for the socket parameters Input1 to Input8 are entered directly in the Page page:
    1. Open the abstract page abstractPage.
    2. Open the Parameters editor page.
    3. Enter the following formula in the Value field of the Page parameter:
        
                =mroot.rmos('T_Mechatronic_ModularSystem.ECAD.Page.Page').indexOf(origin.ifNull(this))

    4. This formula is used to determine a list of all subordinate components of the Page type, and in it the pageâs own position.
    5. Enter the following formula for the PageDescription parameter:
        
                =name

    6. This formula determines the name of the page.
    7. On the Page page enter the following formulas for the parameters Input1 to Input8:
Name | Value  
---|---  
Input1 | ='I' + $Page + '.0'  
Input2 | ='I' + $Page + '.1'  
Input3 | ='I' + $Page + '.2'  
Input4 | ='I' + $Page + '.3'  
Input5 | ='I' + $Page + '.4'  
Input6 | ='I' + $Page + '.5'  
Input7 | ='I' + $Page + '.6'  
Input8 | ='I' + $Page + '.7'  
    8. These formulas are used to assemble the socket names on which the plugs of the sensors will fit later on. The socket name consists of the letter "I", the content of the Page parameter (here, 0 or 1), and the extension ".0" to ".7". This results in the socket names I0.0 to I0.7 and I1.0 to I1.7.
