---
title: "Creating discipline components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_create_discipline_component.htm"
file: "eecbase_k_create_discipline_component"
category: "eecbase"
---

# Creating discipline components

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Creating discipline components

Discipline components are mechatronic components to which, as a rule, a resource, e.g. a macro file, is assigned. No resources are assigned to abstract discipline components. They are only used to define superclasses from which concrete discipline components are subsequently derived. The derived discipline components inherit all properties of the superclass (parameters, methods, etc.) If the names of resources and their storage in a folder structure equal the discipline components to be created and units of the model, the discipline components and the units can be created by means of a mass import.

### [Create an individual concrete discipline component](javascript:void\(0\);)

To create concrete discipline components:

    1. Call up the popup menu of a library or a unit and select New > Discipline name > Discipline component here.

    1. Click [Import...] and select a resource file to import it.

The creation of the discipline components is accelerated by applying the name of the resource.

### Note

The name of a new object should not contain a special character (){}[].:,;-/\Â§$%&#~<>|= so that on the one hand it is file system-compliant and on the other hand no problems occur during the creation of formulas.

    1. Enter a comment optionally. If an ECAD macro contains a description (P8 Property 11057), this is written into an identified area of the comment field.
    2. Save with [Ctrl] \+ [S] or .

The subsequent saving of the editor results in the component being created. A name must be unique within a unit.

### [Create an individual abstract discipline component](javascript:void\(0\);)

To create abstract discipline components:

    1. Call up the popup menu of a library or a unit and select New > Discipline name > Discipline component here.

    1. Enter the name of the abstract discipline component in the Name field.

### Note

The name of a new object should not contain a special character (){}[].:,;-/\Â§$%&#~<>|= so that on the one hand it is file system-compliant and on the other hand no problems occur during the creation of formulas.

    1. Select an optional image with .
    2. Optionally select a different superclass.
    3. Select the Abstract option.
    4. Enter a comment optionally.
    5. Save with [Ctrl] \+ [S] or .
    6. The component is displayed in the tree structure of the model.

The name of a component within a unit must be unique.

### [Creating a discipline components using mass import / creating a model from resources](javascript:void\(0\);)

Instead of creating discipline components individually and in the process applying the name of the resource to the name of the new discipline components, you can also use this mechanism to generate several discipline components by importing the resources.

#### Creating specific discipline components of all the resources of a folder

    1. Call up the popup menu of a library or a unit and select Create Model from Resources here.
    2. The Create Model from Resources wizard opens.
    2. In the Source field enter the path to the resources or select a folder with [Browse...].
    3. Click [Next >].
    4. The wizard displays all resources in a table that are located below the specified folder.

The table lists the following information for each resource:

     * Path: The path including the resource file.
     * Unit: The unit in which the discipline component is inserted.
     * Name: The name used to create the discipline component.
     * Class: The class used to create the discipline component.
     * Existing: Yes or  No indicates whether a discipline component with the resource already exists or not.
    4. Click [Finish].
    5. The discipline components are then created with the name of the resources including unit structure in the library.

#### Creating specific discipline components of selected resources of a folder

    1. Call up the popup menu of a library or a unit and select Create Model from Resources here.
    2. The Create Model from Resources wizard opens.
    2. In the Source field enter the path to the resources or select a folder with [Browse...].
    3. Click [Next >].
    4. The wizard displays all resources in a table that are located below the specified folder.

The table lists the following information for each resource:

     * Path: The path including the resource file.
     * Unit: The unit in which the discipline component is inserted.
     * Name: The name used to create the discipline component.
     * Class: The class used to create the discipline component.
     * Existing: Yes or  No indicates whether a discipline component with the resource already exists or not.
    4. Select the option For selection only.
    5. Select the resources to which the wizard is to be applied.
    6. Click [Finish].
    7. The discipline components are then created with the name of the resources including unit structure in the library.

#### Generating discipline components with other classes

    1. Call up the popup menu of a library or a unit and select Create Model from Resources here.
    2. The Create Model from Resources wizard opens.
    2. In the Source field enter the path to the resources or select a folder with [Browse...].
    3. Click [Next >].
    4. The wizard displays all resources in a table that are located below the specified folder.

The table lists the following information for each resource:

     * Path: The path including the resource file.
     * Unit: The unit in which the discipline component is inserted.
     * Name: The name used to create the discipline component.
     * Class: The class used to create the discipline component.
     * Existing: Yes or  No indicates whether a discipline component with the resource already exists or not.
    4. Click on the Search & Replace Selection area.
    5. Select one or more resources in the table.
    6. Select a new class in the Class field.
    7. Apply the class by using the [Change] button.
    8. The changed class for the selected resource is displayed in the table.
    8. Click [Finish].
    9. The discipline components are then created with the name of the resources including unit structure in the library.
