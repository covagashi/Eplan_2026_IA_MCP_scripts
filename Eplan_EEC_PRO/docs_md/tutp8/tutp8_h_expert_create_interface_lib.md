---
title: "Creating the library for interfaces"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutp8_h_expert_create_interface_lib.htm"
file: "tutp8_h_expert_create_interface_lib"
category: "tutp8"
---

# Creating the library for interfaces

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Creating the library for interfaces The interfaces can be created directly in the mechatronic modular system. However, it is more practical to create these in a separate library and import them into all the libraries that require these interfaces. The names of interfaces can be selected freely. But it has become common to let the names begin with a capital âIâ. Create a library for the interfaces with the name T_Interfaces that imports the system library Engineering. Note If another discipline of the tutorial has already been edited, the T_Interfaces already exists. In this case the existing interfaces only have to be added. See [Creating libraries](eecbase_k_libraries.htm). How to create the interfaces:
    1. Call up the popup menu of the T_Interfaces library and select New > Engineering > Interface.
    2. Add ISchematic in the Name field.
    3. Save the interface.
    4. Repeat Steps 1 to 3 with the following names:
       * ISchematicPage
       * ISensor
       * IMechSensor
       * ISensorPressure
       * ISensorInductive
       * ISensorOptical
All interfaces that are required for the extension points are now defined for the ECAD P8 discipline. The IMechSensor interface is later implemented at all mechatronic sensors. This way you can easily calculate how many schematic pages have to be installed.
