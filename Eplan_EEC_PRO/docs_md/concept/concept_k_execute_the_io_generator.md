---
title: "Executing the IO generator"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/concept_k_execute_the_io_generator.htm"
file: "concept_k_execute_the_io_generator"
category: "concept"
---

# Executing the IO generator

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Executing the IO generator

During the configuration process, only one IO-generator action has to be run in order to create addresses and connections. The IO generator offers the following actions for this purpose:

    1. Update the IO configuration: All addresses and connections that have been created manually or calculated using a formula, i.e. whose value is not <<null>>, remain unchanged. Addresses and connections that are not yet available, i.e. whose value equals <<null>>, are created. Invalid connections (for example, sensors referring to addresses that are no longer available to the controller) are deleted and created anew.
    2. Overwrite the IO configuration: The IO generator assigns addresses for all available terminal connection points and connects them with sensors and actuators. Addresses and connections specified by formulas are not taken into consideration in the process.
    3. Reset the IO configuration: This action deletes all addresses and connections that were not created by formulas.
    4. Regenerating the IO configuration corresponds to the reset command with subsequent updating of the IO configuration.
