---
title: "Parameter Name For The Sequence Of The Functional Assignments"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_modelvar_p8skfunktionalezuordnunganlage.htm"
file: "admin_r_modelvar_p8skfunktionalezuordnunganlage"
category: "admin"
---

# Parameter Name For The Sequence Of The Functional Assignments

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Parameter Name For The Sequence Of The Functional Assignments

Path to model variable:

Disciplines > ECAD > Eplan Electric P8 > Structure identifier management

The name of a parameter is specified with the model variables Parameter Name For The Sequence Of The Functional Assignments which saves the list of the functional assignments in a certain sequence.

To be able to specify a certain sequence of functional assignments in the schematic, a parameter by the same name must be inserted in the component of the WiringDiagram super class.

The output value is a list that consists either only of designations or pairs that are composed of a designation and a description.

### [Example for List](javascript:void\(0\);)
    
        =List{'Conveyor', 'Press', 'Grinder', 'Mill'}

Result:

Row | Complete structure identifier | Structure description | Original description | Usage | Status  
---|---|---|---|---|---  
1 | Conveyor |  |  | ? |   
2 | Press |  |  | ? |   
3 | Grinder |  |  | ? |   
4 | Puncher |  |  | ? |   
5 | <Empty identifier> |  | <Empty identifier> | ? |   
  
### [Example for Map](javascript:void\(0\);)

The description can be specified in every available language. The syntax is as follows: <Language abbreviation>@<Description>;. After the last description a semicolon must be added!
    
        =List{Pair{'Conveyor', 'de_DE@RollenfÃ¶rderer;en_US@Roller conveyor;'},
    	Pair{'Press', 'de_DE@Hydraulikpresse;en_US@Hydraulic press;'},
    	Pair{'Grinder', 'de_DE@Kantenschleifer;en_US@Edge grinder;'},
    	Pair{'Puncher', 'de_DE@Stanzmaschine;en_US@Punching machine;'},}

Result (set dialog language: de_DE):

Row | Complete structure identifier | Structure description | Original description | Usage | Status  
---|---|---|---|---|---  
1 | Conveyor | RollenfÃ¶rderer |  | ? |   
2 | Press | Hydraulikpresse |  | ? |   
3 | Grinder | Kantenschleifer |  | ? |   
4 | Puncher | Stanzmaschine |  | ? |   
5 | <Empty identifier> |  | <Empty identifier> | ? |   
  
Result (set dialog language: en_US):

Row | Complete structure identifier | Structure description | Original description | Usage | Status  
---|---|---|---|---|---  
1 | Conveyor | Roller conveyor |  | ? |   
2 | Press | Hydraulic press |  | ? |   
3 | Grinder | Edge grinder |  | ? |   
4 | Puncher | Punching machine |  | ? |   
5 | <Empty identifier> |  | <Empty identifier> | ? |
