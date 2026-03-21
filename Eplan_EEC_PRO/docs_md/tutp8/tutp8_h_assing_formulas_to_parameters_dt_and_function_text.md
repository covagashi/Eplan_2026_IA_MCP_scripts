---
title: "Assign formulas to parameters for DT and function texts"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutp8_h_assing_formulas_to_parameters_dt_and_function_text.htm"
file: "tutp8_h_assing_formulas_to_parameters_dt_and_function_text"
category: "tutp8"
---

# Assign formulas to parameters for DT and function texts

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Assign formulas to parameters for DT and function texts The Function text parameter was already created for the function texts and inserted into the abstract sensor abstractSensor. The DT parameter in the abstract sensor is given as a value a formula that assembles a device tag.
    1. Open the abstract_Sensor sensor.
    2. Open the Parameters editor page.
    3. Enter the following formula for the DT parameter:
        
                ='S' + ($Sensors.indexOf(origin.ifNull(this))+1)

    4. This formula assembles the texts S1 to S10 from the letter âSâ and the position of the sensor.
    5. Enter the following formula for the Functiontext formula:
        
                =mc.absoluteName.substring(mroot.absoluteName.size+1, mc.absoluteName.size - 1).replaceAll('\\.',' ')

    6. The Functiontext parameter determines only part of the required function text, but does shorten the formulas that still have to be entered in the next step for the function texts of the page.
Enter the formulas for the function texts of the Page discipline component.
    1. In the ECAD.Page unit, open the Page discipline component.
    2. Open the Parameters editor page.
    3. Enter the following formulas for the parameters Functiontext1 to Functiontext8:  

Name | Value  
---|---  
Functiontext1 | =if dos.size>0 then dos.at(0).$Functiontext else '' endif  
Functiontext2 | =if dos.size>1 then dos.at(1).$Functiontext else '' endif  
Functiontext3 | =if dos.size>2 then dos.at(2).$Functiontext else '' endif  
Functiontext4 | =if dos.size>3 then dos.at(3).$Functiontext else '' endif  
Functiontext5 | =if dos.size>4 then dos.at(4).$Functiontext else '' endif  
Functiontext6 | =if dos.size>5 then dos.at(5).$Functiontext else '' endif  
Functiontext7 | =if dos.size>6 then dos.at(6).$Functiontext else '' endif  
Functiontext8 | =if dos.size>7 then dos.at(7).$Functiontext else '' endif  
    4. These formulas determine the value (text) of the Functiontext parameter of the respective discipline-specific component.
