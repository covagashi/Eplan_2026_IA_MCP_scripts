---
title: "Collecting parts data in a map"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_mapping_partsdata.htm"
file: "eececad_k_mapping_partsdata"
category: "eececad"
---

# Collecting parts data in a map

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Collecting parts data in a map

The parts data of the parts database can be read out and saved in a parameter called partsData. You limit the scope of the parts data to be read in by means of specifications in a further parameter called partsDataFilter.

The corresponding commands and actions are provided in the PartsData_Customizing library.

When the Get Parts Data action is executed, EEC generates a call for a C# script with arguments that correspond to the specifications in the partsDataFilter parameter in the <Installation folder>\workspace\PartsData\ExportParts.cs file and then executes the call. The parts data read out are temporarily stored in the <Installation folder>\workspace\PartsData\parts.xml file and transferred as a map into the partsData parameter.

The parts data can be evaluated further with the known methods of the formula language.

To implement reading out the parts database into an existing model:

    1. Import the <Installation folder>\install\partsdata\PartsData_Customizing.eox file.
    2. The PartsData_Customizing library is now located in the library catalog.
    3. Import the library PartsData_Customizing into the library of the mechatronics of your model.
    4. The commands and action can now be used in the mechatronic model.
    5. Create the partsData and partsDataFilter parameters with the Map type and add them to any mechatronic component.

To read out the parts data:

    1. Click Get Parts Data in the popup menu of the project component with the partsData parameter.
    2. The parts data are read out and stored in the partsData parameter.

To restrict the parts data to be read in:

    1. Enter a map with the following syntax for the partsDataFilter parameter.
        
                =Map{Pair{'PROPERTY_1','Value_1'},Pair{'PROPERTY_2','Value_2'},Pair{'PROPERTY_n','Value_n'}}

Example:
        
                =Map{Pair{'ARTICLE_MANUFACTURER','PXC'},Pair{'ARTICLE_PRODUCTGROUP','3'},Pair{'ARTICLE_DESCR1','Feed-through terminal with spring-cage connection'}}

### Note

Repeated reading-out of the parts database is not efficient. The action should be executed on a component of the highest level. All other components can use the formula language to extract their required values from the map in this component.

### Read more

     * [Map](refformulas_r_map_methods.htm)
