---
title: "Assign formula to Disabler for the second page"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutp8_h_assign_formula_to_disabler_of_second_page.htm"
file: "tutp8_h_assign_formula_to_disabler_of_second_page"
category: "tutp8"
---

# Assign formula to Disabler for the second page

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Assign formula to Disabler for the second page To prevent an empty page in the schematic when the Inspect function group is disabled, a formula for the Disabler must be entered. See [Disabler](eecbase_k_variantmanagement_disabler.htm).
    1. For the installed discipline component PLC_Sensors_9_16 in the Feeder component enter the following formula into the Disabled field:
        
                =not(mroot.rmos('T_Mechatronic_ModularSystem.ECAD.PLC_Inputs.abstract_Sensor').size > 8)

    2. This formula determines whether the total number of (abstract) sensors is greater than 8 (.size > 8). If the number is less than 8, the page is disabled. If the number is greater than 8, the page is active.
