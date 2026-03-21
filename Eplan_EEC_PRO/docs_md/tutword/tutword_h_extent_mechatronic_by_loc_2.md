---
title: "Adding a row to mechatronic components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutword_h_extent_mechatronic_by_loc_2.htm"
file: "tutword_h_extent_mechatronic_by_loc_2"
category: "tutword"
---

# Adding a row to mechatronic components

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Adding a row to mechatronic components Add the discipline component Row to all non-abstract components Actuator and Sensor:
     * Valve
     * Cylinder
     * Positionsensor_inductive
     * Positionsensor_optical
     * Pressuresensor
The task is to use formulas to calculate the parameter values of the Row component:
    1. To do so, double-click to open Row and switch to the Parameter editor page.
    1. Enter the formula =mroot.name + mc.absoluteName.substring(mroot.absoluteName.size, mc.absoluteName.size - 1) for the Descriptor parameter.
    1. Enter the formula =dc.dos.indexOf(this) + 1 for the Pos parameter.
Explanation of the formulas: For Descriptor, the absolute name (e.g., Feeder.Mechatronic.Feeder.Insert.Stack.Positionsensor_optical) is to be used to determine the component (e.g., Feeder.Insert.Stack.Positionsensor_optical). To do so, the result of mroot.name (e.g., Feeder) is added to the result of the mc.absoluteName.substring  method. The length of the absolute name (mroot.absoluteName.size = e.g. Feeder.Mechatronic.Feeder = 41) and the length of the name starting at the parent component (mc.absoluteName.size-1 = e.g. Feeder.Mechatronic.Feeder.Insert.Stack.Positionsensor_optical = 84) is transferred to the substring method. The position of the discipline component for Pos is determined from the list of discipline components. dc.dos is used to identify a list of all children of the parent discipline components and indexOf(this) to determine its own position. Since the counter in lists begins at 0 (zero), a 1 is added. Another point is added with \+ '.'.
