---
title: "BASE actions"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_base_actions.htm"
file: "eecbase_k_base_actions"
category: "eecbase"
---

# BASE actions

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## BASE actions

The BASE actions implement the following commands:

    1. Engineering.AbortExecutionIfErrorCommand: Aborts die execution of all following commands, if an error occurred in one of the preceding commands.
    2. Engineering.ClearAllParameterValuesCommand: Deletes all parameter values of the mechatronic structure. In order to apply again, in the library specified values or formulas.
    3. Engineering.ExportEOXCommand: Exports the selected assemblies to an EOX file.
    4. Engineering.NewProjectCommand: Creates a new project. The use of the command is demonstrated in the demo model Project Management.
    5. Engineering.OpenCommand: Opens the object that is specified by absoluteName. A name that is relative to the EO component can be given instead of the absolute name. Examples of using OpenCommand are shown in the demo model Project Management.
    6. Engineering.RemoveExtensionsCommand: The execute method of this command removes the components, which are inserted on extension points. Due to the different execute methods, the effective range of the command may be limited to the areas âentire mechatronic structureâ, âbelow the passed mechatronic componentâ or âthe passed extension pointâ.
    7. Engineering.SaveObjectCommand: Saves the modifications on the model.
    8. Engineering.StartFormulaCacheCommand: Activates the formula cache. With activated formula cache all the results of the calculations are stored and are faster available in re-calculations. Objective data (e.g. schematics, program code, etc.) can thus be created faster. No arguments are passed for this command.
    9. Engineering.StopFormulaCacheCommand: Disables the formula cache. By disabling the formula caches all saved results are discarded. The formula cache must be disabled whenever the data that are used in formulas were changed. For example the cache must be discarded between the generation of the ECAD structure and the generation of the wiring diagrams, since the created structure affects the formula results of the page numbering.
    10. Engineering.UpdateExtensionsCommand: The execute methods of this command remove the invalid components, which are inserted on extension points and inserts new valid components. As remaining components are not changed. In order to remove all components, which are inserted on extension points the RemoveExtensionsCommandis used. Due to the different execute methods, the effective range of the command may be limited to the areas âentire mechatronic structureâ, âbelow the passed mechatronic componentâ or âthe passed extension pointâ.
    11. Engineering.UpdateStaticDisablerCommand: Sets the explicit version update of outdated projects. Only useful for projects with active explicit variant update (configurable at Window > Settings > Formulas > Disabler and in the project).
