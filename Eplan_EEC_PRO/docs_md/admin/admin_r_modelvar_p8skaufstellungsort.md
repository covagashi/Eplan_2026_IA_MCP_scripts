---
title: "Parameter Name For The Sequence Of The Installation Sites"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_modelvar_p8skaufstellungsort.htm"
file: "admin_r_modelvar_p8skaufstellungsort"
category: "admin"
---

# Parameter Name For The Sequence Of The Installation Sites

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Parameter Name For The Sequence Of The Installation Sites

Path to model variable:

Disciplines > ECAD > Eplan Electric P8 > Structure identifier management

With the Parameter Name For The Sequence Of The Installation Sites model variable the name of a parameter is specified that stores the list of installation sites in a specific sequence.

To be able to specify a specific sequence of installation sites in the schematic, a parameter by the same name must be inserted in the component of the WiringDiagram super class.

The output value is a list that consists either only of designations or pairs that are composed of a designation and a description.

### [Example for List](javascript:void\(0\);)
    
    
    =List{'Ground', 'Floor 1', 'Floor 2', 'Top'}

Result:

Row | Complete structure identifier | Structure description | Original description | Usage | Status  
---|---|---|---|---|---  
1 | Ground |  |  | ? |   
2 | Floor 1 |  |  | ? |   
3 | Floor 2 |  |  | ? |   
4 | Top |  |  | ? |   
5 | <Empty identifier> |  | <Empty identifier> | ? |   
  
### [Example for Map](javascript:void\(0\);)

The description can be specified in every available language. The syntax is as follows: <Language abbreviation>@<Description>;. After the last description a semicolon must be added!
    
    
    =List{Pair{'Ground', 'de_DE@Erdgeschoss;en_US@Ground Floor;'},
    	Pair{'Floor 1', 'de_DE@Erstes Geschoss;en_US@First Floor;'},
    	Pair{'Floor 2', 'de_DE@Zweites Geschoss;en_US@Second Floor;'},
    	Pair{'Top', 'de_DE@Obergeschoss;en_US@Top Floor;'},}

Result (set dialog language: de_DE):

Row | Complete structure identifier | Structure description | Original description | Usage | Status  
---|---|---|---|---|---  
1 | Ground | Erdgeschoss |  | ? |   
2 | Floor 1 | Erstes Geschoss |  | ? |   
3 | Floor 2 | Zweites Geschoss |  | ? |   
4 | Top | Obergeschoss |  | ? |   
5 | <Empty identifier> |  | <Empty identifier> | ? |   
  
Result (set dialog language: en_US):

Row | Complete structure identifier | Structure description | Original description | Usage | Status  
---|---|---|---|---|---  
1 | Ground | Ground Floor |  | ? |   
2 | Floor 1 | First Floor |  | ? |   
3 | Floor 2 | Second Floor |  | ? |   
4 | Top | Top Floor |  | ? |   
5 | <Empty identifier> |  | <Empty identifier> | ? |
