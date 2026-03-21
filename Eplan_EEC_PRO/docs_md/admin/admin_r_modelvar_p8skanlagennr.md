---
title: "Parameter Name For The Sequence Of The Higher-level Function Numbers"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_modelvar_p8skanlagennr.htm"
file: "admin_r_modelvar_p8skanlagennr"
category: "admin"
---

# Parameter Name For The Sequence Of The Higher-level Function Numbers

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Parameter Name For The Sequence Of The Higher-level Function Numbers

Path to model variable:

Disciplines > ECAD > Eplan Electric P8 > Structure identifier management

With the Parameter Name For The Sequence Of The Higher-level Function Numbers model variable the name of a parameter is specified that stores the list of higher-level function numbers in a certain sequence.

To be able to specify a certain sequence of function numbers in the schematic, a parameter by the same name must be inserted in the component of the super class WiringDiagram.

The output value is a list that consists either only of designations or pairs that are composed of a designation and a description.

### [Example for List](javascript:void\(0\);)
    
        =List{'1', '2', '3', '4'}

Result:

Row | Complete structure identifier | Structure description | Original description | Usage | Status  
---|---|---|---|---|---  
1 | 1 |  |  | ? |   
2 | 2 |  |  | ? |   
3 | 3 |  |  | ? |   
2 | 4 |  |  | ? |   
3 | <Empty identifier> |  | <Empty identifier> | ? |   
  
### [Example for Map](javascript:void\(0\);)

The description can be specified in every available language. The syntax is as follows: <Language abbreviation>@<Description>;. After the last description a semicolon must be added!
    
        =List{Pair{'1', 'de_DE@Lagerhaltung;en_US@Stockkeeping;'},
    	Pair{'2', 'de_DE@Produktion;en_US@Production;'},
    	Pair{'3', 'de_DE@PrÃ¼ffeld;en_US@Test facility;'},
    	Pair{'4', 'de_DE@Versand;en_US@Dispatch;'},}

Result (set dialog language: de_DE):

Row | Complete structure identifier | Structure description | Original description | Usage | Status  
---|---|---|---|---|---  
1 | 1 | Lagerhaltung |  | ? |   
2 | 2 | Produktion |  | ? |   
3 | 3 | PrÃ¼ffeld |  | ? |   
4 | 4 | Versand |  | ? |   
5 | <Empty identifier> |  | <Empty identifier> | ? |   
  
Result (set dialog language: en_US):

Row | Complete structure identifier | Structure description | Original description | Usage | Status  
---|---|---|---|---|---  
1 | 1 | Stockkeeping |  | ? |   
2 | 2 | Production |  | ? |   
3 | 3 | Test facility |  | ? |   
4 | 4 | Dispatch |  | ? |   
5 | <Empty identifier> |  | <Empty identifier> | ? |
