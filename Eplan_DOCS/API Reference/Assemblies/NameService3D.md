# NameService3D

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService3D.html

---

Class for managing the Function3D names (device tags) on the specified InstallationSpace

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.HEServices.NameService3D**

Syntax

**C#**



public class NameService3D

public ref class NameService3D


Remarks

When using EPLAN interactively the structure identifiers of a Function 3D on a installation space are adjusted automatically according to the installation space in which the Function 3D is located. In API, the methods of the NameService3D class helps to do this.

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [NameService3D Constructor](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService3D~_ctor.html) | Constructor. Creates a NameService3D object. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AdjustFullName](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService3D~AdjustFullName.html) | Evaluates for a given Function3D the full name from the visible name and sets that evaluated value at the function-object |
| Public Method | [AdjustVisibleName](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService3D~AdjustVisibleName.html) | Evaluates for a given Function3D the visible name and visible name format from the fullname of the function and sets these evaluated values at the function-object |
| Public Method | [Dispose](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService3D~Dispose().html) | Destructor |
| Public Method | [EvaluateAndSetAllNames](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService3D~EvaluateAndSetAllNames.html) | Evaluates the full name for all placed 3D functions in installation space by calling EvaluateName for all those objects. |
| Public Method | [EvaluateAndSetAllVisibleNames](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService3D~EvaluateAndSetAllVisibleNames.html) | Evaluate the visible names from the full names for all placed 3D functions in installation space. |
| Public Method | [EvaluateName](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService3D~EvaluateName.html) | Method evaluates the full name for a Function3D by using the visible device tag of that Function3D and building the full name by graphical search on the installation space where the Function3D is placed. |
| Public Methodstatic (Shared in Visual Basic) | [RenameDevice](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService3D~RenameDevice.html) | Changes the full names of the found device. |
| Public Methodstatic (Shared in Visual Basic) | [RenameFunction](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService3D~RenameFunction.html) | Changes the full names of the function and its children. |
| Public Methodstatic (Shared in Visual Basic) | [SetName](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService3D~SetName.html) | Sets a default device tag to the function. |


