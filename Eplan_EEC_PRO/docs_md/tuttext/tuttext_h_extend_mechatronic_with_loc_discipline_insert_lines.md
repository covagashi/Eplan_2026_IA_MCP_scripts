---
title: "Adding lines to mechatronic components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tuttext_h_extend_mechatronic_with_loc_discipline_insert_lines.htm"
file: "tuttext_h_extend_mechatronic_with_loc_discipline_insert_lines"
category: "tuttext"
---

# Adding lines to mechatronic components

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Adding lines to mechatronic components Add the Text component Line to all non-abstract actuators and sensors that are located in the T_Mechatronic_ModularSystem library in the Mechatronic unit and the Actuators and Sensors subunits:
     * Valve
     * Cylinder
     * Pressuresensor
     * Positionsensor_inductive
     * Positionsensor_optical
The parameter values for Pos and Descriptor of the component Line are to be calculated with these formulas: Parameter | Formula  
---|---  
Descriptor | 
    
        =mroot.name + mc.absoluteName.substring(mroot.absoluteName.size, mc.absoluteName.size - 1)  
  
Pos. | 
    
        =dc.dos.indexOf(this) + 1  
  
For Descriptor, the absolute name (e.g., Feeder.Mechatronic.Feeder.Insert.Stack.Positionsensor_optical) is to be used to determine the sub string e.g., Feeder.Insert.Stack.Positionsensor_optical. To do so, the result of mroot.name (e.g., Feeder) is added to the result of the mc.absoluteName.substring method. The length of the absolute name (mroot.absoluteName.size = e.g. Feeder.Mechatronic.Feeder = 41) and the length of the name starting at the parent component (mc.absoluteName.size-1 = e.g. Feeder.Mechatronic.Feeder.Insert.Stack.PositionÂ­sensor_optical = 84) is transferred to the substring method. The position of the discipline component for Pos is determined from the list of discipline components. dc.dos is used to identify a list of all children of the parent discipline components and indexOf(this) to determine its own position. Since the counter in lists begins at 0 (zero), a 1 is added.
