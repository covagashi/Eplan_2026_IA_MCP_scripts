---
title: "Generate structure"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_linking_dcs_generate_structure.htm"
file: "eecbase_k_linking_dcs_generate_structure"
category: "eecbase"
---

# Generate structure

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

Structure Generating Discipline structure Generating

## Generate structure

In a complete mechatronic project configuration, the discipline-specific components are found in different locations of the configuration. For example, in the case of the ListOfComponents discipline, the document body is integrated directly at the Feeder station; see the following figure.

Individual fragments, for example, Sensors_Actuators_Line, are found in the mechatronic configuration at the corresponding components â in this case, sensors and actuators.

By using the structure generator, it is possible to isolate the discipline-specific structure and to generate it according to the configuration of the project and the corresponding discipline. The created structure serves as a basis for creating the actual components list in the text format (project document). The structure generator of the text discipline is started via the Mechatronic context menu:

The result of the structure generator is the specific structure of the respective discipline. This is represented in the Project Catalog at the bottom end:

It is possible to navigate between the components in the project and the created structure. For navigating from the created structure to the Mechatronic, one selects, within the BOM structure, in the context menu of an object Go to... > Mechatronic (Go to... > Mechatronic):

This way, for example, the sensor-actuator line of the ListOfComponents is displayed in the Mechatronic:

The reverse navigation is also possible. By selecting a discipline-specific component in the project, one can navigate to the corresponding component in the created structure:
