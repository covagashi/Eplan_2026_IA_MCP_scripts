---
title: "Synchronization of project properties"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_synchronize_project_properties.htm"
file: "eececad_k_synchronize_project_properties"
category: "eececad"
---

# Synchronization of project properties

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Synchronization of project properties

Eplan Electric P8 project properties can be calculated in EEC and transferred to the Eplan project to be created.

Transfer of project data from EEC to Eplan Electric P8:

The properties of an Eplan Electric P8 project can be configured in EEC and transferred at the time of generation. Eplan-specific project properties have unique identifying numbers (ID) (for example 10230) as well as a name. To allow the EEC user access to all possible properties, while remaining independent of the Eplan Electric P8 version used, EEC establishes the reference to the project properties via the ID.

### Note

Project properties have been introduced in Eplan Electric P8 as of Version 2.5 that dispose of an identifying name instead of an identifying number, for example [ESS] Report control <ESS.Project.Reports>. These cannot be influenced by EEC by means of model variables!

Setting project properties from EEC:

     * Display project property IDs in Eplan Electric P8:

To display the IDs of the project properties in Eplan Electric P8, the following setting has to be carried out in Eplan Electric P8: Options > Settings... activate the switch User > Representation > Interface: Display identifying numbers.

     * Determining project property IDs:

Select the project and then select in the menu Project > Properties .... All properties whose value column is not grayed out can be written from EEC, for example 20919 ("order number").

Note: Some properties that cannot be edited in Eplan Electric P8 can be set via Eplan Electric P8 API.

     * Generate a parameter object for project property in EEC:

The project properties are mirrored in EEC by parameter objects whose names consists of two parts: The common prefix and a number, for example, PropId_20919.   
The prefix applies to the entire model and can be modified in EEC in the Model > Model variables > ECAD > Eplan Electric P8 > Prefix for Eplan Electric P8 properties menu.

     * Assigning parameter objects to schematic diagram objects:

Project properties are defined in EEC by assigning the parameter objects with the name scheme mentioned above to the wiring diagram objects. During the generation the values are transferred to Eplan Electric P8 automatically.

     * Setting parameter values:

There are two types of properties: normal and indexed properties. Normal properties contain the value in EEC as a string. Indexed properties are assigned data of the data type List resp. Map. The index always starts at 1. Prior to the access, the API checks whether the permissible range has been exceeded.

Examples of access:
    
        PropId_10150=List{Pair{1,'Initiale Version'},Pair{2,'Testdaten geÃ¤ndert'}}
    
        PropId_10230='KL'

An object of the Schematic type can be saved only if a resource has been assigned or if the object is marked as "abstract". An abstract object is used to define a classification level in order to generate objects that are derived from an abstract object with all the properties of the latter automatically.
