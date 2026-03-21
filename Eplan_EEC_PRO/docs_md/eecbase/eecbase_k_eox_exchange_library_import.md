---
title: "Importing libraries/projects as an EOX file"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_eox_exchange_library_import.htm"
file: "eecbase_k_eox_exchange_library_import"
category: "eecbase"
---

# Importing libraries/projects as an EOX file

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Importing libraries/projects as an EOX file

One of three options is used during the import of an EOX file:

### [Adding](javascript:void\(0\);)

The assembly to be imported is added to the existing model with the Add option, without existing assemblies being overwritten. No objects are deleted.

### [Overwriting](javascript:void\(0\);)

With the Overwrite option, existing assemblies of the same name are replaced with assemblies to be imported of the same name. Objects that are not part of the assemblies to be imported are deleted.

### [Adding/overwriting](javascript:void\(0\);)

With the Add/overwrite option the existing assemblies and the assemblies to be imported are compared with the assemblies of the common back-end. This option therefore only makes sense if both model data have the same origin.

On the basis of revision 1, two users (User1 and User2) work independently of each other on copies of this revision status. User 1 receives an EOX file from User 2, and imports it using the Add/overwrite option.

     * User2 adds new classes.
     * Classes deleted by User2 are deleted at User1âs end.
     * Classes deleted by User1 are not replaced by existing classes by User2.
     * For classes that were changed by both users, a decision has to be made which change is to be applied.

The following scenarios help to identify which option is to be applied in which case.

### [Working steps for importing an EOX file](javascript:void\(0\);)

The data of a model, i.e., the libraries and projects, are imported as an EOX file.

The following steps are necessary to import an EOX file:

    1. Select File > Import.

The Import wizard opens.

    1. Select Model > Model data (EOX).
    2. Confirm via [Next >].
    3. In the Import EOX section select the EOX file to be imported.
    4. Highlight the libraries and projects to be imported.

Selected libraries/projects are identified with a check mark , while the dependent libraries/projects are identified by a square .

    1. In the Import options area select the option Add or Overwrite or Add/overwrite.
       * Add adds all new assemblies to the current workspace.
       * Overwrite adds new assemblies to the current workspace and overwrites assemblies of the same name.
       * Add/overwrite merges assemblies of the same name. In the process a comparison between the previous revision (common back-end) and the change statuses of the EOX file to be imported and the current model takes place.
    2. If you have selected the Add/overwrite option, select a Common back-end in addition.
    3. Confirm with [Finish].

The wizard is terminated and the Synchronize view opened.

The following symbols can be displayed in the Synchronize view:

Symbol | Meaning  
---|---  
| The incoming changes shown with a plus sign (+) indicate that a component is missing in your assembly. This will be added.  
| The incoming changes shown with a minus sign (-) indicate that there is one more component in your assembly. This will be removed.  
| The incoming changes shown with the red double arrow indicate that interaction on the part of the user is required.  
  
If the synchronization does not show any changes for which an interaction of the user is required, the changes can be applied with .

During the synchronization, the following information is written to the console:

     * The absolute names of added components and parameters.
     * The absolute names of deleted components and parameters.
     * The absolute names of modified components and parameters.

The following scenarios illustrate the different merge results.

### [Scenario 1](javascript:void\(0\);)

The following scenario is based on a project (base), which is modified by two users (User1 and User2) independently of each other by deleting or adding.

User1 has deleted the instance GripperB, and added the instance GripperD.

User2 has deleted the instance GripperC, and added the instance GripperE.

### [Adding](javascript:void\(0\);)

The assembly of User1 is to be added to the assembly of User2 (User2 performs the import procedure):

The class Gripper appears in the view Synchronize as an incoming change.

The instances GripperC and GripperD appear in the view Synchronize as incoming changes with a plus sign in the blue arrow. These will be added.

### Note

In this scenario, it is not clear whether GripperC and GripperD were created by User1 or deleted by User2. This requires coordination.

### [Overwriting](javascript:void\(0\);)

The assembly of User2 is to be overwritten with the assembly of User1 (User2 performs the import procedure):

The class Gripper appears in the view Synchronize as an incoming change.

The instances GripperB and GripperE appear in the view Synchronize as incoming changes with a minus sign in the blue arrow. These will be deleted.

The instances GripperC and GripperD appear in the view Synchronize as incoming changes with a plus sign in the blue arrow. These will be added.

### Note

In this scenario, it is not clear whether GripperC and GripperD were created by User1 or deleted by User2. This requires coordination.

This scenario can be used to return to a project saved as an EOX file. All changes made up to this point will be lost.

### [Adding/overwriting](javascript:void\(0\);)

The assembly of User2 is to be merged with the assembly of User1:

The class Gripper appears in the view Synchronize as an incoming change.

The instance GripperB appears in the view Synchronize as an incoming change with a minus sign in the blue arrow. This will be deleted.

The instance GripperD appears in the view Synchronize as an incoming change with a minus sign in the blue arrow. This will be added.

### Note

In this scenario, the reference to the base makes it clear that GripperB was deleted by User1, and GripperD created by User1.

### [Scenario 2](javascript:void\(0\);)

Scenario 2 is based on a project (base), which is modified by two users (User1 and User2) independently of each other by modifying the comment for GripperC.

User1 has changed the comment of GripperC to Gripper to grip.

User2 has changed the comment of GripperC to Fast gripper.

### [Adding](javascript:void\(0\);)

The assembly of User1 is to be added to the assembly of User2 (User2 performs the import procedure):

The instance GripperC appears in the view Synchronize as an incoming change with a red double arrow. An interaction by User2 is required.

User2 must select a strategy:

The only strategy that can be chosen here is Select value. The value to be used as the target value must be chosen via the radio buttons EOX file (source) or Internal model or Merge value manually. The strategy chosen will also be applied to all other conflicts if the check box Use as global strategy has been selected.

### [Overwriting](javascript:void\(0\);)

The assembly of User2 is to be overwritten with the assembly of User1 (User2 performs the import procedure):

The instance GripperC is displayed in the view Synchronize as an incoming change with a blue arrow. This will be added.

### [Adding/merging](javascript:void\(0\);)

The assembly of User2 is to be merged with the assembly of User1 (User2 performs the import procedure):

The instance GripperC appears in the view Synchronize as an incoming change with a red double arrow. An interaction by User2 is required.

User2 must therefore select a strategy:

The only strategy that can be chosen here is Select value. The value to be used as the target value must be chosen via the radio buttons EOX file (source) or Internal model or Merge value manually. The strategy chosen will also be applied to all other conflicts if the check box Use as global strategy has been selected.

### Note

If in the imported EOX a class or instance has been deleted, the class will be deleted during the 3-Way Merge, and the instance will also be gone, but only after the project is re-created.

But if there is already another instance of the deleted class in the project, deleting the class should be thought over again.

The following solutions are possible:

    1. Not deleting the class.
    2. Deleting the class before synchronization, and creating a new class with the same properties. Subsequently the 3-ways-merge is restarted (see [Synchronize again](eecbase_k_eox_exchange_resynchronize.htm)).

### Note

Conflicts at the attributes level should always be solved before conflicts at the class level.

### [Scenario 3](javascript:void\(0\);)

Scenario 3 is based on an architecture and a modular system (base), which is modified by two users (User1 and User2) independently of each other.

User1 deletes the components Gripper and GripperA, and instead inserts the components Pusher and PusherA.

User2 deletes the component GripperA, and inserts the component GripperB.

### [Adding](javascript:void\(0\);)

The assemblies of User1 are to be added to the assemblies of User2 (User2 performs the import procedure):

The components Pusher and PusherA appear in the view Synchronize as an incoming change with a blue arrow. These will be added, no interaction is required.

The component Transfer appears in the view Synchronize as an incoming change with a blue arrow. This will be changed, no interaction is required.

### [Overwriting](javascript:void\(0\);)

The assemblies of User2 are to be overwritten with the assemblies of User1 (User2 performs the import procedure):

The components Gripper and GripperB appear in the view Synchronize as an incoming change with a blue arrow and minus sign. These are removed, no interaction is required.

The components Pusher and PusherA appear in the view Synchronize as an incoming change with a blue arrow. These will be added, no interaction is required.

The component Move appears in the view Synchronize as an incoming change with a blue arrow. This will be changed, no interaction is required.

### [Adding/overwriting](javascript:void\(0\);)

The assemblies of User2 are to be merged with the assemblies of User1 (User2 performs the import procedure):

The components Pusher and PusherA appear in the Synchronize view as an incoming change with a blue arrow. These will be added, no interaction is required.

The component Transfer appears in the view Synchronize as an incoming change with a blue arrow. This will be changed, no interaction is required.

The components Gripper and GripperB appear in the view Synchronize as an incoming change with a red double arrow. There is a conflict. The component Gripper cannot be deleted, because GripperB is an instance of the component Gripper.

More information on the conflict of a component is provided by opening the conflict component:

In this case, an internal conflict resolution is not possible; there is no selection of system strategies to choose from.

Instead, a strategy at the workspace level is recommended: The relation of the component GripperB with the component Gripper is to be deleted.

The following approach is possible to solve the relational conflict:

    1. User1 re-creates the component Gripper, and exports the EOX file again with the same name and in the same folder. Using [Synchronize with last configuration], User2 repeats the import of the EOX file (see [Synchronize again](eecbase_k_eox_exchange_resynchronize.htm)).
    2. User2 removes the component GripperB, and using [Synchronize with last configuration], repeats the import of the EOX file (see [Synchronize again](eecbase_k_eox_exchange_resynchronize.htm)).

### [Scenario 4](javascript:void\(0\);)

Scenario 4 is based on an architecture and a modular system (base), which is modified by a user (User1).

User1 adds to the modular system the component GripperB, removes instance of GripperA mounted in the component Transfer, and instead mounts an instance of GripperB. Then, User1 renames the instance of GripperB to GripperA.

### [Adding](javascript:void\(0\);)

The assemblies of User1 are to be added to the assemblies of Base (any user performs the import procedure):

The component GripperB appears in the view Synchronize as an incoming change both in the architecture and the modular system with a blue arrow and minus sign. This will be added.

The component Transfer appears in the view Synchronize as an incoming change in the architecture with a blue arrow. This will be added.

The component Transfer appears in the view Synchronize as an incoming change in the modular system with a red double arrow. There is a conflict. The component Transfer cannot be added, because GripperA is an instance of the component GripperB.

More information on the conflict is provided by opening the conflict component:

The conflict description mentions the specific conflict (1): An object with the same name but of a different type is already in use.

The component GripperA mounted in the Base assembly had an internal reference to component GripperA, but the component GripperA mounted in the User1 assembly had an internal reference to component GripperB. The conflict must be solved at the workspace level, for example, by renaming the mounted component GripperB.

To implement this manual strategy, a link to the component is provided in the internal model (2).
