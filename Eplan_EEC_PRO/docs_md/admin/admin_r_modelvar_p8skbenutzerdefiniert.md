---
title: "Parameter Name For The Sequence Of The User-defined Structure Identifiers"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_modelvar_p8skbenutzerdefiniert.htm"
file: "admin_r_modelvar_p8skbenutzerdefiniert"
category: "admin"
---

# Parameter Name For The Sequence Of The User-defined Structure Identifiers

1This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here: 

## Parameter Name For The Sequence Of The User-defined Structure Identifiers

Path to model variable: Disciplines > ECAD > Eplan Electric P8 > Structure identifier management With the Parameter name for the sequence of user defined model variable the name of a parameter is specified that stores the list of user defined structure identifiers in a certain sequence. To be able to specify a certain sequence of user defined structure identifiers in the schematic, a parameter by the same name must be inserted in the component of the WiringDiagram super class. The output value is a list that consists either only of designations or pairs that are composed of a designation and a description.

### [Example for List](javascript:void\(0\);)
    
        =List{'E5A1', 'E5A2', 'E5A3', 'E5A4'}

Result: | Row | Complete structure identifier | Structure description | Original description | Usage | Status  
---|---|---|---|---|---  
1 | E5A1 |  |  | ? |   
2 | E5A2 |  |  | ? |   
3 | E5A3 |  |  | ? |   
4 | E5A4 |  |  | ? |   
5 | <Empty identifier> |  | <Empty identifier> | ? |   
  
### [Example for Map](javascript:void\(0\);)

The description can be specified in every available language. The syntax is as follows: <Language abbreviation>@<Description>;. After the last description a semicolon must be added!
    
        =List{Pair{'E5A1', 'de_DE@Werk 5 Halle 1;en_US@Plant 5 Hall 1;'},
    	Pair{'E5A2', 'de_DE@Werk 5 Halle 2;en_US@Plant 5 Hall 2;'},
    	Pair{'E5A3', 'de_DE@Werk 5 Halle 3;en_US@Plant 5 Hall 3;'},
    	Pair{'E5A4', 'de_DE@Werk 5 Halle 4;en_US@Plant 5 Hall 4;'},}

Result (set dialog language: de_DE):

Row | Complete structure identifier | Structure description | Original description | Usage | Status  
---|---|---|---|---|---  
1 | E5A1 | Werk 5 Halle 1 |  | ? |   
2 | E5A2 | Werk 5 Halle 2 |  | ? |   
3 | E5A3 | Werk 5 Halle 3 |  | ? |   
4 | E5A4 | Werk 5 Halle 4 |  | ? |   
5 | <Empty identifier> |  | <Empty identifier> | ? |   
  
Result (set dialog language: en_US):

Row | Complete structure identifier | Structure description | Original description | Usage | Status  
---|---|---|---|---|---  
1 | E5A1 | Plant 5 Hall 1 |  | ? |   
2 | E5A2 | Plant 5 Hall 2 |  | ? |   
3 | E5A3 | Plant 5 Hall 3 |  | ? |   
4 | E5A4 | Plant 5 Hall 4 |  | ? |   
5 | <Empty identifier> |  | <Empty identifier> | ? |
