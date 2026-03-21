---
title: "Creating text discipline components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tuttext_h_create_text_discipline_components_create_text_discipline_components.htm"
file: "tuttext_h_create_text_discipline_components_create_text_discipline_components"
category: "tuttext"
---

# Creating text discipline components

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Creating text discipline components Below three concrete text objects are to be created which reference the already created text fragments as resources. Begin by creating the ListOfComponents unit in the T_Mechatronic_ModularSystem. See [Creating units](eecbase_k_create_unit.htm). Begin by creating the concrete discipline components in the ListOfComponents unit. See [Creating discipline components](eecbase_k_create_discipline_component.htm). Discipline component | Resource file  
---|---  
Body | Body.txt  
Chapter | Chapter.txt  
Line | Line.txt  
When importing the text resources, the parameters contained in them are automatically detected and the corresponding parameters are created in the Parameter unit:
