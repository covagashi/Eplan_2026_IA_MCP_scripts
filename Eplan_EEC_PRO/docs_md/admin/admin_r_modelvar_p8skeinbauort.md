---
title: "Parameter Name For The Sequence Of The Location Designations"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_modelvar_p8skeinbauort.htm"
file: "admin_r_modelvar_p8skeinbauort"
category: "admin"
---

# Parameter Name For The Sequence Of The Location Designations

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

## Parameter Name For The Sequence Of The Location Designations

Path to model variable:

Disciplines > ECAD > Eplan Electric P8 > Structure identifier management

With the Parameter name for the sequence of location designations model variables the name of a parameter is specified that stores the list of location designations in a certain sequence.

To be able to specify a certain sequence of the location designations in the schematic, a parameter by the same name must be inserted in the component of the super class Schematic.

The output value is a list that consists either only of designations or pairs that are composed of a designation and a description.

### [Example for List](javascript:void\(0\);)
    
        =List{'Mains', '24VDC', 'Conveyor', 'PLC'}

Result:

Row | Complete structure identifier | Structure description | Original description | Usage | Status  
---|---|---|---|---|---  
1 | Mains |  |  | ? |   
2 | 24VDC |  |  | ? |   
2 | Conveyor |  |  | ? |   
2 | PLC |  |  | ? |   
3 | <Empty identifier> |  | <Empty identifier> | ? |   
  
### [Example for Map](javascript:void\(0\);)

The description can be specified in every available language. The syntax is as follows: <Language abbreviation>@<Description>;. After the last description a semicolon must be added!
    
        =List{Pair{'Mains', 'de_DE@Einspeisung;en_US@Power supply;'},
    	Pair{'24VDC', 'de_DE@Versorgung 24VDC;en_US@24VDC supply;'},
    	Pair{'Conveyor', 'de_DE@RollenfÃ¶rderer;en_US@Roller conveyor;'},
    	Pair{'PLC', 'de_DE@Steuerung;en_US@Controller;'},}

Result (set dialog language: de_DE):

Row | Complete structure identifier | Structure description | Original description | Usage | Status  
---|---|---|---|---|---  
1 | Mains | Einspeisung |  | ? |   
2 | 24VDC | Versorgung 24VDC |  | ? |   
3 | Conveyor | RollenfÃ¶rderer |  | ? |   
4 | PLC | Controller |  | ? |   
5 | <Empty identifier> |  | <Empty identifier> | ? |   
  
Result (set dialog language: en_US):

Row | Complete structure identifier | Structure description | Original description | Usage | Status  
---|---|---|---|---|---  
1 | Mains | Power supply |  | ? |   
2 | 24VDC | 24VDC supply |  | ? |   
3 | Conveyor | Roller conveyor |  | ? |   
4 | PLC | Controller |  | ? |   
5 | <Empty identifier> |  | <Empty identifier> | ? |
