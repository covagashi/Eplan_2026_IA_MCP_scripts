---
title: "Modeling areas"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_modeling_areas.htm"
file: "eecplc_k_modeling_areas"
category: "eecplc"
---

# Modeling areas

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Modeling areas

A complete representation of controller software can be divided into three sub-areas:

     * Hardware configuration:

Objects allocated to this area can be used to model the controllerâs hardware components so that configuration data can be created for each PLC system. A detailed description is provided in the section [Hardware configuration](eecplc_k_hardware_configuration.htm).

     * Symbol lists:

Many control systems use symbol lists (also known as variable or allocation lists) for indirect addressing of input and output signals. For each signal, these lists contain the platform-specific absolute address, usually the data type, the symbolic address and a comment. The task of this sub-area is to take these symbol lists from the individual signals and assemble them in the data model. For this purpose, the methods of the text discipline are given precedence, because the symbol list usually has a very simple structure. A description is provided in the section on [Symbol lists](eecplc_k_symbollist.htm).

     * Program code:

The structure of the control program for the different PLC systems exhibits many similarities, but also major differences. As a result, not all PLC systems can be modeled solely on the basis of general specifications in the PLC library. Deeper integration of STEP 7, CoDeSys, etc. is accomplished via platform-specific extensions (STEP 7, CoDeSys, etc. libraries). Objects that have common features are integrated into the PLC discipline, while platform-specific objects, and especially the methods, are integrated into the respective platform disciplines. A detailed description of this sub-area can be found in the section on [Program code](eecplc_k_programcode.htm).

Automatic allocation of PLC addresses (IO generation) is discussed in a separate section (see the section on [IO generation](eecplc_k_io_generation.htm)).

### Read more

     * [Overview of the objects of the PLC discipline](eecplc_k_objects_overview.htm)
