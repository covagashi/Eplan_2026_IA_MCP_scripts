---
title: "Extensions"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_variantmanagement_extensions.htm"
file: "eecbase_k_variantmanagement_extensions"
category: "eecbase"
---

# Extensions

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Extensions

In contrast to projects with disablers, which must contain all variants in the base library according to the maximum principle, each variant is stored in a separate library for projects with extension points. Using the extension points (interfaces), the components from the variant libraries are linked to the base library at the correct positions.

The extension points can be defined both for mechatronic components and discipline components. The disabler function can also be applied to extension points. In the Update variants explicitly mode (static disabler mode), the instances concerned can be deleted or re-instantiated, like class-defined components.

The properties of an extension point are defined at the class level.

Extension points are created as [Creating placeholders](eecbase_k_placeholder.htm) and assigned the Extension point attribute, as seen in the following image:

Extension points behave like normal placeholders in the project. Multiple mounting (multiplicity) is not checked at the time of the instantiation, but regularly at the time of validation. Any existing recursions are not checked.

The actions Update extensions and Remove extensions enable type conversions during the library development with existing projects. These actions must be enabled manually. There is no automatic updating of extension points. The associated commands allow for an automatic use in user-defined actions (see [BASE actions](eecbase_k_base_actions.htm)).

Method like the reconstruction of libraries to extension points:

    1. Start with all existing libraries, but without projects.
    2. Define the interfaces for the extension points: One interface in the modular system for each different variant position.
    3. Delete all fixed mounted variants (note down classes!) and reconstruct the newly added placeholders as extension points.
    4. Remove from the base library the imported variant libraries, and import the base library from the variant libraries.
    5. Enter the correct interfaces in the classes, as noted down under point 3.

Display of the implemented and extended interfaces in the editor

In the interface view of the editor, the relations to the interfaces are displayed in the Declared in column. For the model represented below, this produces for the class Station the following interface declaration:

The table lists the interfaces implemented by the component itself ahead of the inherited interfaces.

The following figure shows a model where the superclass Abstract_Station implements the interfaces I1 and I3. The Station class implements the I2 interface, which extends the I3 interface.
