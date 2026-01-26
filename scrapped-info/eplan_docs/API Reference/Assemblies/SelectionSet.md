# SelectionSet

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet.html

---

Class providing functionality to get selected objects from a current dialog of EPLAN.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.HEServices.SelectionSet**

Syntax

**C#**



public class SelectionSet

public ref class SelectionSet


Remarks

The methods usually return an empty result if there is more than 1 one project open, except from SelectedProjects and GetCurrentProject(true).

Example

The following example shows how to use class SelectionSet.

**C#**

```
SelectionSet selectionSet = new SelectionSet();

StorableObject[] storableObjects = selectionSet.Selection;

if (storableObjects.Length == 0)

{

    Console.Out.WriteLine("No current selection!");

    return;

}

else

{

    Console.Out.WriteLine("Current selection contains of:");

    foreach (StorableObject so in storableObjects)

    {

        Console.Out.WriteLine("Object type: " + so.GetType().ToString());

    }

}

```

**C#**

```
SelectionSet selectionSet = new SelectionSet();

//If any selected object will be changed, LockProjectByDefault must be set to true before obtaining any object

selectionSet.LockProjectByDefault = true;

Project oProject = selectionSet.GetCurrentProject(false);

oProject.ProjectName = "new_name";

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [SelectionSet Constructor](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~_ctor.html) | Default constructor. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [CurrentlyEdited](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~CurrentlyEdited.html) | Determines Page or InstallationSpace currently edited in graphical editor. |
| Public Property | [Document](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~Document.html) | Determines whether a document is selected. This will only return a document, when the selection is inside the graphical editor. |
| Public Property | [IsOnlyOneObjectSelected](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~IsOnlyOneObjectSelected.html) | Determines whether exactly one object is selected. |
| Public Property | [IsPageSelected](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~IsPageSelected.html) | Determines whether a page is selected. |
| Public Property | [Layers](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~Layers.html) | Gets the selected layers of the active project as an array. |
| Public Property | [LockProjectByDefault](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~LockProjectByDefault.html) | If set to true, the objects returned and the rest objects from project by the SelectionSet method are locked. Default value is `false`. |
| Public Property | [LockSelectionByDefault](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~LockSelectionByDefault.html) | If set to true, the objects returned by the SelectionSet methods are locked. Default value is `true`. |
| Public Property | [Mates](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~Mates.html) | Returns selected mate objects |
| Public Property | [OpenedInstallationSpaces](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~OpenedInstallationSpaces.html) | Gets installation spaces opened in GED. |
| Public Property | [OpenedPages](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~OpenedPages.html) | Gets pages open in GED. |
| Public Property | [ProjectMessages](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~ProjectMessages.html) | Gets all selection project's messages. |
| Public Property | [SelectedProjects](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~SelectedProjects.html) | Return the selected projects of the active dialog as an array. If you select elements from different projects inside of one dialog you can determinate the selected projects. |
| Public Property | [Selection](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~Selection.html) | Gets the complete selection on the active window. Property `LockProjectByDefault` should be set to `true` before any changes on any inside elements of obtained objects. |
| Public Property | [SelectionRecursive](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~SelectionRecursive.html) | Gets the complete selection on the active window. Property `LockProjectByDefault` should be set to `true` before any changes on any inside elements of obtained objects. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [\_setObjectTypes](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~_setObjectTypes.html) | For internal use. |
| Public Method | [GetCurrentProject](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~GetCurrentProject.html) | Determines the active project. |
| Public Method | [GetSelectedObject](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~GetSelectedObject.html) | \Returns the first selected object. |
| Public Method | [GetSelectedPages](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~GetSelectedPages.html) | Gets the selected pages. |


