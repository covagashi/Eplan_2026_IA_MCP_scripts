---
title: "User supplementary fields"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_parameterize_usersupplementaryfield.htm"
file: "eececad_k_parameterize_usersupplementaryfield"
category: "eececad"
---

# User supplementary fields

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

## User supplementary fields

The values of user supplementary fields can be set in two ways:

    1. By means of a Map type parameter. The name of the parameter has to be specified in the model variable Name of the parameter for user supplementary field.
    2. By means of a String type parameter. The name of the parameter follows the syntax PropId_<ID of the user supplementary field>.

For path 1, key-value pairs are transferred as the value, whereby the key corresponds to the name of the user supplementary field.

Example for User supplementary field[2]:

ProjectSupplementaryFields=Map{Pair{'Eplan.Project.UserSupplementaryField2','230/400VAC'}}

A string is specified as the value for path 2.

Example for User supplementary field[2]:

PropId_40002='230/400VAC'

### Note

If both ways are used to set the value of the same user supplementary field, the value of the parameter specified via the model variable is always used.
