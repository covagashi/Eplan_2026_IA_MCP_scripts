---
title: "Structure identifier management in EplanÂ ElectricÂ P8"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_structure_identifier_management_in_p8.htm"
file: "eececad_k_structure_identifier_management_in_p8"
category: "eececad"
---

# Structure identifier management in EplanÂ ElectricÂ P8

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Structure identifier management in Eplan Electric P8

The management of structure identifiers in Eplan Electric P8 (for example, "Function designation" [preceding sign "="] and "Location designation" [preceding sign "+"]) affects two important areas of the electrical engineering documentation, which may also operate independently of each other.

    1. The order of schematic pages in a project.
       * The order of the schematic pages becomes visible in the page navigator, and is also the output order for printing and export (PDF, DXF etc.).
    2. The order of the schematic objects (devices, terminal strips, plugs, PLCs, cables, etc.) in a project.
       * The order of schematic objects influences the sequence in the navigators for devices, terminal strips, plugs, PLCs and cables.
       * Another, and partially more important, effect of the order of the above schematic objects becomes visible in the logic evaluations of the schematics, e.g., the source and target of a cable in the cable layout.

Both the schematic pages and schematic objects can contain structure identifier independently of each other. Thus, it is possible to find structure identifiers in a schematic object for which there is no schematic page.

If a new schematic page or new schematic object is created in Eplan Electric P8 (regardless of whether directly or via EEC), all new structure identifiers will be entered in the central structure identifier management. In the process, only new structure identifiers are created, and always, by default, added to the end of the list.

The management of the structure identifiers is opened in Eplan Electric P8 via the tab Tools > Command group Management > Structure identifier.

The following table shows an example of structure identifier management (tab List):

Row | Complete structure identifier | Structure description | Original description | Usage | Status  
---|---|---|---|---|---  
1 | <Empty identifier> |  | <Empty identifier> | ? |   
2 | B |  |  | No |   
3 | A |  |  | No |   
4 | CA |  |  | No |   
5 | CA1 |  |  | No |   
  
The order of the entries in structure identifier management is the determining order both for the schematic pages and also for all other schematic objects where structure identifiers play a role.

Previously, structure identifiers could be moved from within EEC only via the schematic pages in Eplan Electric P8. In the process the structure identifiers in accordance with the order of creation of the schematic pages in EEC (the order of the schematic pages in the ECAD structure of EEC project) were entered into the Eplan Electric P8 structure identifier management.

image/svg+xml ECAD Schematic Page2 Page1 Mechatronic EEC ECAD Schematic Page1 Page2 Mechatronic EEC Plant1 Location1 1 Page 1 P8 =Plant2+Location2/1 Plant2 Location2 1 Page 2 Schematic Plant2 Location2 1 Page 2 P8 Plant1 Location1 1 Page 1 Schematic =Plant1+Location1/1 =Plant2+Location2/1 =Plant1+Location1/1

In many cases is necessary for the identifier structure to have a different order in Eplan Electric P8 than that created by default via the creation of schematic pages from EEC. Therefore the structure identifiers need to be manipulated independently of the creation of schematic pages and / or schematic objects.

Generally, there are two ways of manipulating structure identifiers:

    1. Before the schematic pages and / or schematic objects in a schematic are created.

The structure identifiers (their order and any descriptions) are created first in an empty project. All schematic pages / schematic objects that are created in the schematic afterwards (and that contain existing structure identifiers) are sorted according to this order.

    1. After the schematic pages and / or schematic objects in a schematic are created.

Here, the order and, if appropriate, the description of the structure identifiers in a schematic in which pages and objects already exist is changed.

### Note

In general all structure identifiers can be assigned to the devices in the EEC. Depending on the number of pages and objects in the schematic this can take longer.

### [Example for change in the structure identifier](javascript:void\(0\);)

Structure identifier management before:

Row | Complete structure identifier | Structure description | Original description | Usage | Status  
---|---|---|---|---|---  
1 | <Empty identifier> |  | <Empty identifier> | ? |   
2 | B |  |  | No |   
3 | A |  |  | No |   
  
Structure identifier management afterwards:

Row | Complete structure identifier | Structure description | Original description | Usage | Status  
---|---|---|---|---|---  
1 | <Empty identifier> |  | <Empty identifier> | ? |   
2 | A | Higher-level function 1 |  | No |   
3 | B | Higher-level function 2 |  | No |   
  
Changing the order of the structure identifiers before the schematic pages / schematic objects are created:

To change the order of the structure identifiers from within EEC before the schematic pages / schematic objects are generated, a corresponding model variable is available for each structure identifier:

Parameter | Default name of the parameter  
---|---  
Parameter Name For The Sequence Of Function Designations | SKFunktionskennzeichen  
Parameter Name For Equipment Number List | SKAnlagennummer  
Parameter Name For Installation List | SKAufstellungsort  
Parameter Name For User-defined List | SKBenutzerdefiniert  
Parameter Name For Document Kind | SKDokumentenart  
Parameter Name For The Sequence Of Location Designations | SKOrtskennzeichen  
Parameter Name For Functional Assignment List | SKFunktionaleZuordnung  
  
The output value is a list that consists either only of designations or pairs that are composed of a designation and a description.

### [Example for List](javascript:void\(0\);)
    
        =List{'Anlage1', 'Anlage2', 'Anlage3'}

### [Example for Map](javascript:void\(0\);)
    
        =List{Pair{'A', 'de_DE@Beschreibung A;en_US@Description A;'}, 
    	Pair{'B', 'de_DE@Beschreibung B;en_US@Description B;'}, 
    	Pair{'C', 'de_DE@Beschreibung C;en_US@Description C;'}}

If the generation process adds further structure identifiers, they will be added to the existing ones in Eplan Electric P8. If an order already exists for a structure identifier in structure identifier management, EEC will try to merge the two lists.

For example, if the order is already defined in the project template as âBâ, âCâ, and EEC requests âAâ, âCâ, these elements do not contradict each other in terms of the order, and after the generation process, this produces either the list with âAâ, âBâ, âCâ or âBâ, âAâ, âCâ, because the order between âAâ and âBâ has not been defined.

### Read more

     * [Structure of the device tag](../../../../Plattform/2025/Content/htm/devicetaggui_k_aufbauvonbm.htm)
