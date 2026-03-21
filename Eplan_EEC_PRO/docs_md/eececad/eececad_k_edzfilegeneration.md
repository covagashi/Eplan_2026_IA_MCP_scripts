---
title: "Eplan Data Zip (EDZ file) generation"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_edzfilegeneration.htm"
file: "eececad_k_edzfilegeneration"
category: "eececad"
---

# Eplan Data Zip (EDZ file) generation

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Eplan Data Zip (EDZ file) generation

An EDZ file contains all the specifications that are required to create one or more macros from them in P8.

An EDZ file can be created without an installation of Eplan Electric P8 on the same computer. A valid installation of Eplan Electric P8 is required to create the P8 macros from the EDZ file.

The generation is carried out by means of the command ECAD.GenerateEdzForEcadProjectCommand.

Prerequisites for the generation of the EDZ file are:

     * A part.xml file has to exist. This can be created by the text discipline if is not yet provided by other subsystems. The file is to be specified as an argument partXmlFilePath.
     * An image file for the part has to exist. The file is to be specified as an argument pictureFilepath.
     * A C# script has to exist whose absolute file name is specified by the model variable Name of the parameter for a C# script and whose arguments are specified by the model variable Name of the parameter for C# script arguments.
     * The model variables under Eplan Data Zip (.edz) generation are to be taken into consideration.
