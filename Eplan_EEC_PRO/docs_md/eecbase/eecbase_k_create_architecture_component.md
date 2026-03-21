---
title: "Create architecture components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_create_architecture_component.htm"
file: "eecbase_k_create_architecture_component"
category: "eecbase"
---

# Create architecture components

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Create architecture components

Architecture components are abstract components with a functional construction hierarchy.

### [Creating abstract architecture components of the MechatronicComponent type](javascript:void\(0\);)

    1. Call up the popup menu of a library or a unit and select the following menu items: New > Engineering > MechatronicComponent.

The editor of a new component is opened via the Attributes editor page.

    1. Enter a name for the new component.

### Note

The name of a new object should not contain a special character (){}[].:,;-/\Â§$%&#~<>|= so that on the one hand it is file system-compliant and on the other hand no problems occur during the creation of formulas.

    1. Select an optional image with .

The type of the component is entered in the Super class field. The type has to be changed with [..].

    1. Select the Abstract check box.
    2. Enter a comment optionally.
    3. Switch to the Level configuration editor page.

    1. Optionally select the Top-level element check box.
    2. Start the finder for subordinate components  and select one or more components from the search result.
    3. The selected components are applied in the list of the subordinate components.
    4. Save with [Ctrl] \+ [S] or .

The component is created as a result of the assignment of a name and subsequently the saving of the editor. Without a valid name the name field is highlighted in red. A name must be unique within a unit.

### [Creating abstract architecture components of any type](javascript:void\(0\);)

    1. Call up the popup menu of a library or a unit and select the following menu items: New > Object

The Create new library object dialog opens:

    1. Select a discipline component under Object > Component > DisciplineComponent.

The editor of a new component is opened via the Attributes editor page.

    1. Enter a name for the new component.

### Note

The name of a new object should not contain a special character (){}[].:,;-/\Â§$%&#~<>|= so that on the one hand it is file system-compliant and on the other hand no problems occur during the creation of formulas.

    1. Select an optional image with .

The type of the component is entered in the Super class field. The type can be changed with [..].

    1. Select the Abstract check box.
    2. Enter a comment optionally.
    3. Switch to the Level configuration editor page.

    1. Optionally select the Top-level element check box.
    2. Start the finder for subordinate components  and select one or more components from the search result.
    3. The selected components are applied in the list of the subordinate components.
    4. Save with [Ctrl] \+ [S] or .

The component is created as a result of the assignment of a name and subsequently the saving of the editor. Without a valid name the name field is highlighted in red. A name must be unique within a unit.
