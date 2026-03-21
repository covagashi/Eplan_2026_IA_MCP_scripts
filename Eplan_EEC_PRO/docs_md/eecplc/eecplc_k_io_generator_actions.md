---
title: "IO generator actions"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_io_generator_actions.htm"
file: "eecplc_k_io_generator_actions"
category: "eecplc"
---

# IO generator actions

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## IO generator actions

The IO generator offers the following FieldBusCommand-derived commands:

    1. [Plc.GenerateFieldbusCommand](refcommands_r_plc_generatefieldbuscommand.htm): Generates all start addresses and connections. Existing connections and start addresses are new created. Start addresses and connections which are determined by formulas remain unchanged.
    2. [Plc.UpdateFieldbusCommand](refcommands_r_plc_updatefieldbuscommand.htm): Generates start addresses and connections of control components, sensors and actuators, which have no connection or start address yet and of sensors and actuators, whose connections do not exist anymore (e.g. because a control component is deleted).
    3. [Plc.GenerateFieldbusCommand](refcommands_r_plc_generatefieldbuscommand.htm): Generates all start addresses and connections new. Connections and start addresses, which are calculated by formulas are replaced.
    4. [Plc.ResetFieldbusCommand](refcommands_r_plc_resetfieldbuscommand.htm): Deletes all start addresses and connections.
    5. [Plc.RecreateAddressesCommand](refcommands_r_plc_regenerateaddressescommand.htm): Generates all start addresses new. This command only affects control components, sensors and actuators remain unaffected.
    6. [Plc.UpdateAddressesCommand](refcommands_r_plc_updateaddressescommand.htm): Supplements the addresses that are not yet available. This command only affects control components, sensors and actuators remain unaffected.
    7. [Plc.OverwriteAddressesCommand](refcommands_r_plc_overwriteaddressescommand.htm): Creates new start addresses, any existing formulas for start addresses are not taken into account, sensors and actuators remain unaffected.
    8. [Plc.ResetAddressesCommand](refcommands_r_plc_resetaddressescommand.htm): Deletes previously calculated start addresses, while leaving connections unaffected.
    9. [Plc.RegenerateConnectionsCommand](refcommands_r_plc_regenerateconnectionscommand.htm): Generates all connections new. This command only affects sensors and actuators, control components remain unaffected.
    10. [Plc.UpdateConnectionsCommand](refcommands_r_plc_updateconnectionscommand.htm): Creates the non-existing connections. This command only affects sensors and actuators, control components remain unaffected.
    11. [Plc.OverwriteConnectionsCommand](refcommands_r_plc_overwriteconnectionscommand.htm): Generates all connections new. Connections, which are calculated by formulas are replaced. This command only affects sensors and actuators, control components remain unaffected.
    12. [Plc.ResetConnectionsCommand](refcommands_r_plc_resetconnectionscommand.htm): Deletes previously calculated connections. This command only affects sensors and actuators, control components remain unaffected.
    13. In the Console view, error messages, warnings, and information from the IO generator are displayed.
