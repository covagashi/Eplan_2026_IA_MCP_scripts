---
title: "Parameter Name For The Sequence Of The Document Kinds"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_modelvar_p8skdokumentenart.htm"
file: "admin_r_modelvar_p8skdokumentenart"
category: "admin"
---

# Parameter Name For The Sequence Of The Document Kinds

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

## Parameter Name For The Sequence Of The Document Kinds

Path to model variable:

Disciplines > ECAD > Eplan Electric P8 > Structure identifier management

The name of a parameter that contains the list of the document types saved in a certain sequence, is specified with the model variable Parameter Name For The Sequence Of The Document Kinds.

To be able to specify a certain sequence of document types in a project, a parameter by the same name must be inserted in the component of the WiringDiagram super class.

The output value is a list that consists either only of designations or pairs that are composed of a designation and a description.

### [Example for List](javascript:void\(0\);)
    
        =List{'EPC', 'EMB', 'EFS', 'EPL'}

Result:

Row | Complete structure identifier | Structure description | Original description | Usage | Status  
---|---|---|---|---|---  
1 | EPC |  |  | ? |   
2 | EMB |  |  | ? |   
3 | EFS |  |  | ? |   
4 | EPL |  |  | ? |   
5 | <Empty identifier> |  | <Empty identifier> | ? |   
  
### [Example for Map](javascript:void\(0\);)

The description can be specified in every available language. The syntax is as follows: <Language abbreviation>@<Description>;. After the last description a semicolon must be added!
    
        =List{Pair{'EPC', 'de_DE@StÃ¼cklisten;en_US@Bills of material;'},
    	Pair{'EMB', 'de_DE@Verkabelungs- und Rohrleitungsdokumente;en_US@Wiring and tubing plans;'},
    	Pair{'EFS', 'de_DE@Schaltkreisdokumente;en_US@Schematics;'},
    	Pair{'EPL', 'de_DE@Ortslisten;en_US@Locations list;'},}

Result (set dialog language: de_DE):

Row | Complete structure identifier | Structure description | Original description | Usage | Status  
---|---|---|---|---|---  
1 | EPC | Bills of materials |  | ? |   
2 | EMB | Verkabelungs- und Rohrleitungsdokumente |  | ? |   
3 | EFS | Schaltkreisdokumente |  | ? |   
4 | EPL | Ortslisten |  | ? |   
5 | <Empty identifier> |  | <Empty identifier> | ? |   
  
Result (set dialog language: en_US):

Row | Complete structure identifier | Structure description | Original description | Usage | Status  
---|---|---|---|---|---  
1 | EPC | Bills of materials |  | ? |   
2 | EMB | Wiring and tubing plans |  | ? |   
3 | EFS | Schematics |  | ? |   
4 | EPL | Locations list |  | ? |   
5 | <Empty identifier> |  | <Empty identifier> | ? |
