---
title: "Navigating from a macro in P8 to a discipline component in EEC"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_switch_from_p8_to_eec.htm"
file: "eececad_k_switch_from_p8_to_eec"
category: "eececad"
---

# Navigating from a macro in P8 to a discipline component in EEC

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Navigating from a macro in P8 to a discipline component in EEC

During the development phase the possibility of navigating from a macro in the generated schematic to the discipline component in the mechatronic modular system is helpful.

### Note

If multiple instances of EEC are open, only one component in the first instance of EEC is jumped to.

Requirements:

     * An action for P8 is set up.
     * The optional P8 Integration Service Add-On function is installed (see [EEC P8 Integration Service Add-On](admin_h_installation_optionalfeature_p8_integration.htm)).
     * The option Delete placeholders after generation is deactivated in the settings.

### [Setting up Action for P8](javascript:void\(0\);)

    1. Open Eplan Electric P8.
    2. Open the popup menu of the toolbar.  

    3. Click Customize ribbon.
    4. Select Further commands (tools) in the drop-down of the left selection window.
    5. Click Open the component in EEC.
    6. In the right selection window select the tools subgroup after which the new EEC group is to be inserted, e.g. Synchronize.
    7. Click New command group, to create the EEC group.
    8. Assign a name to the new command group, for example EEC.
    9. Mark the new command group.
    10. Click the blue arrow  pointing towards the right to insert the command Open component in EEC in the new command group.
    11. Confirm with OK to finish the creation of the group.
    12. The new EEC group is now displayed in the ribbon on the right next to the Synchronize group.

If a schematic has been generated successfully, you can navigate from each macro of the schematic to the corresponding discipline component in the configuration.

    1. Select a macro in the schematic.
    2. Click Open component in EEC in the EEC toolbar.
    3. The corresponding discipline component opens in EEC.
