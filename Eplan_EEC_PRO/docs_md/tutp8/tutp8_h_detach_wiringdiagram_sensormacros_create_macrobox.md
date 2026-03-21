---
title: "Create macro boxes for sensors"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutp8_h_detach_wiringdiagram_sensormacros_create_macrobox.htm"
file: "tutp8_h_detach_wiringdiagram_sensormacros_create_macrobox"
category: "tutp8"
---

# Create macro boxes for sensors

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Create macro boxes for sensors Now, a fragment is prepared as a macro from each single sensor together with the associated plug. Note Make sure that the anchors of the placeholder objects are inside the macro boxes; otherwise, the macros cannot be created correctly.
    1. Select the following commands: Tab Insert > Command group Macros > Navigator > Insert macro box.
    2. Drag a macro box around each sensor together with the plug. The elements framed by the macro box may have to be moved first to a free position on the page. Make sure that the sensor and plug maintain their positions to each other.
    1. Highlight the macro box.
    2. Select the following commands: Tab Home > Command group Edit > Properties.
    3. The dialog Properties (components): Macro box opens.
    4. In the Name field, enter the text PLC_Inputs\Sensor_Inductive.
Note Do not use German umlauts (Ã, Ã, Ã, Ã¤, Ã¶, Ã¼) when entering the name. Note Specifying a folder (e.g. PLC_Inputs\\) when conducting a mass import of macros into EEC automatically creates a unit of the same name that facilitates structured arrangement of the macros.
    1. Open the Display tab.
    2. Click [New].
    3. The Property selection dialog opens:
    4. Select Macro: File name.
    5. Confirm with [OK].
    6. The Property selection dialog is closed and you are returned to the Properties (components) macro box dialog.
    7. Confirm with [OK].
    8. Repeat steps 1 to 10 for the other two sensors. Enter the texts PLC_Inputs\Sensor_optical and PLC_Inputs\Sensor_Pressure as the name of the other sensors.
