---
title: "Management of page structure properties"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_management_of_pagestructureproperties.htm"
file: "eececad_k_management_of_pagestructureproperties"
category: "eececad"
---

# Management of page structure properties

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Management of page structure properties

Engineering providers, for example, due to different customer requirements, have to create wiring diagrams with different **Page structures** (e.g., numbering by higher-level function number/ location designation) from within a modular system. The objective behind the modular system draft is to design schematic pages in such a way that they can be deployed in schematics with different numbering concepts. This requires that a schematic page must be able to use formulas to determine the page structure in which it will be used.

Page structure properties can be modeled using the **Schematic object**. This way, alternative structural concepts can be realized in a model.

Since the page structure properties are defined in the **P8 wiring diagram templates** , it is also important to note that these definitions can be imported into the EEC model.

Thus, it is possible to manage the page structure properties in the schematic template and to import it into EEC model by way of synchronization.

All page structure properties supported by P8 are known to EEC as model variables (see [Eplan Electric P8](admin_r_modelvar_eplanp8.htm)).

The model variables specify the names of the parameters that represent the corresponding properties in EEC, e.g., the parameter for the page number of the eponymous property.

Whether this property is actually used to generate a schematic will be defined only by the schematic template. If the page structure with higher-level function number and location designation is defined there, EEC, too, will only use these properties.

The settings from the schematic template are adopted in the EEC model by synchronizing a schematic object with the external resource, the schematic template (basic project template) (see [Synchronization of discipline components](eecbase_k_synchronize_disciplinecomponents.htm)).

The properties of the basic project template are set up in the schematic object as parameters according to the settings in the model variables.

The modeling of the properties depends on the existence of parameters. Schematic pages, for example, query the schematic object whether there is a parameter for the location designation in order to take a decision regarding the numbering (the values of these parameters have no effect).

The following formula is used to check the existence of parameters and adjust the page numbering accordingly:
    
        =if dc.parameter('Location').isNull() then
    ...
    else
    ...
    endif

The previous option of setting the page structure globally in the settings does not exist anymore.

### Note

Note the DT syntax check setting in the project template. It also applies to the creation of pages. For example, if only numerals and uppercase letters are permitted, and if you want to create a page with the property $Location=St01, this will result in unexpected errors when creating a schematic. The same applies to editing the macros.

### [Detached representation of substructures](javascript:void\(0\);)

By default, the page navigator of P8 displays both function designation and location designation in a single level in the tree view.

Example for the default representation of the tree for a schematic page with a location designation of the notation main identifier.Sub-identifier.Sub-sub-identifier:

In order to achieve a broken-up representation of the substructures, the File > Settings > Projects > "Project name" > Display > Tree structure (pages) check box Detached representation of substructures in P8 is to be selected.

With this setting the tree for the same schematic of the example is displayed broken down:

In order for a schematic to be generated with this setting, the basic project template (*.zw1) has to be created again with this setting and assigned to the schematic component in EEC. If the name of the basic project template is unchanged, the resource for the schematic component only has to be synchronized in EEC.

Depending on the selected separator in the P8 project, the value of the parameter for the location designation has to be built up.

For the example shown above the value of the parameter for the location designation ='HK1.UK1.UUK1' for page 1 PLC_Sensors_1_8 and ='HK1.UK2.UUK2â for page 2 PLC_Sensors_9_16.

### Note

The name of the parameter for the location designation must be entered in the model variables!
