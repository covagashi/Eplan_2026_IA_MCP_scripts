---
title: "Instantiate components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutmechatronic_h_instantiate_component.htm"
file: "tutmechatronic_h_instantiate_component"
category: "tutmechatronic"
---

# Instantiate components

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Instantiate components In the previous step, you already selected the Feeder component, which was installed in the project as an instance in the project wizard. Without doing so first, you would have to instantiate the Feeder component manually. A component is instantiated by dragging it from the Library Catalog view to a project in the Project Catalog view. Instantiate means that an instance is created from the component specification. If the Feeder component has not been instantiated yet, proceed as follows:
     * Drag the Feeder component onto the Mechatronic object in the Feeder project.
The Mechatronic object is the root object of a mechatronic configuration (later in the tutorial, you will also encounter non-mechatronic configurations, meaning discipline-specific configurations). Remarks:
     * Try also to instantiate other components from the library by dragging them onto the Mechatronic object. This is not permitted for any objects except Feeder (the mouse pointer becomes a No Parking sign). This has to do with the rule defined in the architecture model that says that only Station can be the top element of a configuration (see [Specify the top-level component](tutmechatronic_h_assign_top_level_component.htm)). However, it is possible to integrate the Feeder component multiple times.
     * In the last screenshot, the term Feeder can be seen three times: As the name of a library component (class), as the project name, and as the name of the instance of the Feeder component in the project (instance). The identical names of classes and instances occur very often in practice, particularly when the class is used in a project only once.
In order to still give objects unique names, the absolute name should be used when in doubt, which is derived from the paths displayed in the tree structures:
     * T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder (Class)
     * Feeder (Project)
     * Feeder.Mechatronic.Feeder (Instance)
