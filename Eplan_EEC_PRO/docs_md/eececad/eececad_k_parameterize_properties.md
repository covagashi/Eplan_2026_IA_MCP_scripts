---
title: "Setting properties for projects or pages"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_parameterize_properties.htm"
file: "eececad_k_parameterize_properties"
category: "eececad"
---

# Setting properties for projects or pages

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

# Setting properties for projects or pages

There are several possibilities for setting properties for projects or pages:

    1. You use a parameter that uses the prefix of the [Prefix For Eplan Electric P8 Properties](admin_r_modelvar_p8propertiesprefix.htm) model variables in the name. The syntax is: PropId_<property number>.

### Example for property without index

The parameter name used to set the value for the <1002> Structure description property is PropId_1002.

A parameter of the String type is sufficient for properties without index.

### Example for property with index

The parameter name used to set the value for the <11901 1> Supplementary field[1] property is PropId_11901.

A parameter of the Map type is to be used for properties with index.

The key-value pairs specify the index and its value.

Example for the properties of <11901 1> Supplementary field[1] and <11901 2> Supplementary field[2]:

=Map{Pair{'1', 'SupplementaryFieldText_1'}, Pair{'2', 'SupplementaryFieldText_2'}}.

    1. You are using a parameter of the PropertyMap type. The PropertyMap contains either a list of values or a map with pairs of indexes and values of the properties. In the case of a PropertyMap with a list of values, the position of the value in the list corresponds to the index of the property.

### Example for PropertyMap with list

Example for the properties of <11901 1> Supplementary field[1], <11901 2> Supplementary field[2], <11901 4> Supplementary field[4], as well as <11057 1> Macro description[1]:

=Map{Pair{'11901', List{'SupplementaryFieldText_1','SupplementaryFieldText_2','','SupplementaryFieldText_4'}, Pair{'11057', 'MacroDescriptionText'}}.

### Example for PropertyMap with map

Example for the properties of <11901 1> Supplementary field[1], <11901 2> Supplementary field[2], <11901 4> Supplementary field[4], as well as <11057 1> Macro description[1]:

=Map{Pair{'11901', Map{Pair{'1','SupplementaryFieldText_1'},Pair{'2','SupplementaryFieldText_2'},Pair{'4','SupplementaryFieldText_4'}}}, Pair{'11057', 'MacroDescriptionText_1'}}.

For path 1, key-value pairs are transferred as the value, whereby the key corresponds to the name of the user supplementary field.

Example for User supplementary field[2]:

ProjectSupplementaryFields=Map{Pair{'Eplan.Project.UserSupplementaryField2','230/400VAC'}}

A string is specified as the value for path 2.

Example for User supplementary field[2]:

PropId_40002='230/400VAC'

### Note

If both ways are used to set the value of the same user supplementary field, the value of the parameter specified via the model variable is always used.
