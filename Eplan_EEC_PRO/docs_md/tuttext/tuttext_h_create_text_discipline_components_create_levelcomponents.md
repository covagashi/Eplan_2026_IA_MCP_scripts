---
title: "Create architecture components for the text discipline"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tuttext_h_create_text_discipline_components_create_levelcomponents.htm"
file: "tuttext_h_create_text_discipline_components_create_levelcomponents"
category: "tuttext"
---

# Create architecture components for the text discipline

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Create architecture components for the text discipline As a rule concrete discipline components are derived from abstract discipline components (architecture components). For the ListOfComponents these are architecture components for Body, Chapter and Line. Create the following architecture components in the Levelcomponents unit: Architecture component | Super class | Image | Image file | Abstract | Component of the top level | Output type | Sublevels  
---|---|---|---|---|---|---|---  
Body | ListOfComponentsComponents |  | install/icon-collection/Rumpf.gif | Yes | Yes | Template file | Chapter  
Chapter | ListOfComponentsComponents |  | install/icon-collection/Abschnitt.gif | Yes | No | Fragment | Line  
Line | ListOfComponentsComponents |  | install/icon-collection/Zeile.gif | Yes | No | Fragment | -  
See [Create architecture components](eecbase_k_create_architecture_component.htm). Result:
