---
title: "Eplan Electric P8 configuration"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_eplanp8preferences.htm"
file: "eececad_k_eplanp8preferences"
category: "eececad"
---

# Eplan Electric P8 configuration

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Eplan Electric P8 configuration

The configuration file <EEC Installation Folder>\workspace\\.metadata\\.plugins\org.eclipse.core.runtime\\.settings\com.mind8.ecad.eplanp8.prefs is additionally responsible for the configuration of Eplan Electric P8.

In order to ensure that Eplan Electric P8 does not hang up unnoticed you can set in the configuration file the number of calls for creating P8 data after which Eplan Electric P8 is terminated.

Insert a line with the following syntax:
    
        com.mind8.ecad.eplanp8.countdown=<count>

The value for <count> specifies the number of calls after which a restart of Eplan Electric P8 is carried out.

Eplan Electric P8 is restarted by the next call to create P8 data.
