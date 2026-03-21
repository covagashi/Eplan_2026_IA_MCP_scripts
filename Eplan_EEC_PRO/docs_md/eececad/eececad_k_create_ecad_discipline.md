---
title: "Creating an ECAD discipline"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_create_ecad_discipline.htm"
file: "eececad_k_create_ecad_discipline"
category: "eececad"
---

# Creating an ECAD discipline

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Creating an ECAD discipline

Requirement:

     * The ECAD license module is part of the current installation.
     * A valid version of Eplan Electric P8 is installed.

The ECAD system library that is to be imported into the current modular system library is required so that the ECAD discipline can be processed. This system library contains the discipline-specific basic classes and methods for Eplan Electric P8.

In addition the T_Ecad_Ui library can be imported. This contains preassembled commands to execute the generation of the ECAD structure and of the schematics. In principle you can create these commands yourself (see [Creating project documents](eececad_k_generate_project_docu.htm)). The T_Ecad_Ui library is provided by the <EEC installation folder>\install\Tutorial\P8\Ecad_Ui.eox file as a part of the tutorial. The library is added to the library catalog by importing the EOX file.

For the discipline Eplan Electric P8 settings are to be set (see [Eplan Electric P8](admin_r_prefs_ecad_p8.htm)) and model variables to be agreed (see [Eplan Electric P8](admin_r_modelvar_eplanp8.htm)).
