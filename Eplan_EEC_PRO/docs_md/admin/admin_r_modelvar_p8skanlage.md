---
title: "Parameter Name For The Sequence Of Function Designations"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_modelvar_p8skanlage.htm"
file: "admin_r_modelvar_p8skanlage"
category: "admin"
---

# Parameter Name For The Sequence Of Function Designations

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
---|---|---|---|---|---This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
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
  
This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Parameter Name For The Sequence Of Function Designations

Path to model variable:

Disciplines > ECAD > Eplan Electric P8 > Structure identifier management

With the Parameter Name For The Sequence Of Function Designations model variables the name of a parameter is specified that stores the list of installation location designation in a certain sequence.

To be able to specify a certain sequence for location designations in the schematic, a parameter by the same name must be inserted in the component of the super class Schematic.

The output value is a list that consists either only of designations or pairs that are composed of a designation and a description.

### [Example for Map](javascript:void\(0\);)
    
        = List {
    	Pair{'A1', List{
    		Pair{'1002', 'Description1 A1'},
    		Pair{'1007', 'Description2 A1'},
    		Pair{'1008', 'Description3 A1'},
    		Pair{'1009 1', 'Description Additional Field1 A1'},
    		Pair{'1009 2', 'Description Additional Field2 A1'},
    		Pair{'1009 3', 'Description Additional Field3 A1'}
    	}},
    	Pair{'A2', 'Description A2'}
    }

Result (set dialog language: en_US):

Row | Complete structure identifier | Structure description <1002> | Original designation | Usage | Status | Structure description 2 <1007> | Structure description 3 <1008> | Structure description Supplementary field[1] <1009 1> | Structure description Supplementary field[2] <1009 2> | Structure description Supplementary field[3] <1009 3>  
---|---|---|---|---|---|---|---|---|---|---  
1 | A1 | Description1 A1 | A1 | No |  | Description2 A1 | Description3 A1 | Description Additional Field1 A1 | Description Additional Field2 A1 | Description Additional Field3 A1  
2 | A2 | Production | A2 | No |  |  |  |  |  |   
3 | <Empty identifier> |  | <Empty identifier> | * |  |  |  |  |  |   
  
### Read more

     * [Structure identifier management](../../../../Plattform/2026/Content/htm/pleditorgui_k_start.htm)
