---
title: "Maintenance of model data"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_maintenance.htm"
file: "eecbase_k_maintenance"
category: "eecbase"
---

# Maintenance of model data

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Maintenance of model data

## [Set mechatronic root names to current locale](javascript:void\(0\);)

Replaces the names of all MechatronicRoot objects of a model with the language currently set.

The name of the mechatronic in the project can be changed individually. The action Model > Maintenance > Set mechatronic root names to current locale sets the names of all MechatronicRoot objects of a model to the translation of âMechatronicâ in the language currently set.

The following figure shows the name of a MechatronicRoot before (left) and after (right) executing this action.

## [Set Project Library Names To Current Locale](javascript:void\(0\);)

Sets the names of all project libraries of a model to the translation in the language currently set.

The following figure shows the name of a project library before (left) and after (right) executing this action.

## [Maintain copy sources](javascript:void\(0\);)

When copying a class, the original is noted in the copy. Similar to the absolute names in formulas, this is immune to move operations. The copy source remains valid even after deletion or creation with the same name, but different class.

This action updates the copy sources and deletes notes on invalid classes.

## [Maintain absolute type names in formulas](javascript:void\(0\);)

Using this action, all formulas are updated where absolute names of components are used.

Absolute names of components in formulas (e.g., when using rmos, mos, type, ref, etc.) are typically immune to move operations of the objects referenced.

But this mechanism may fail as a result of operations such as deletion or new creation with the same name. To prevent this, this action can be executed where indicated so as to update all formulas.

Prior to any model export to an EOX file, it is recommended that the absolute names of components in formulas be updated.

## [Convert object names file system compliant...](javascript:void\(0\);)

The names of objects allow characters which are not file system compliant. Due to this action the names of all objects of the model are changed in a way that they correspond to the conventions of the file system.

## [Check Native Method Contributions](javascript:void\(0\);)

If native methods were developed for the current model, you can check with this function whether the plugin is loaded and the implementation of the native method is available.
