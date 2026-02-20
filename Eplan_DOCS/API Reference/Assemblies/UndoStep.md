# UndoStep

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UndoStep.html

---

Class representing DataModel's Undo.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.DataModel.UndoStep**

Syntax

**C#**



public sealed class UndoStep

public ref class UndoStep sealed


Remarks

The class implements [System.IDisposable](#) interface. All the functions that perform only changes to persistent objects of a project has basically Undo protocol capability. All features, that make the changes directly in the file system or registry are not covered by the Undo technology. This concerns for example opening/closing project, restore, creating UserDefinedPropertyDefinition, etc. Using of UndoStep allows to use GUI UndoList. E.q. it is possible to use Edit->Redo after UndoStep::DoUndo() call but not possible when using Transactions. No transaction is needed within UndoStep. It is not possible to call DoUndo() twice to reverse two steps. If a project is changed via API without using an UndoStep, the undo history of EPLAN is cleared. See also "Undoing and Redoing Actions" chapter of Eplan Help.

Example

UndoStep usage - only inside "using".

**C#**

```
using (UndoStep undo = new UndoManager().CreateUndoStep())

{

	SelectionSet oSS = new SelectionSet();

	Function f = oSS.Selection[0] as Function;

	f.Properties.FUNC_CUSTOM_SUPPLEMENTARYFIELD01 = "new value";

	// ... code ...				//

    // and if needed DoUndo call//

    undo.DoUndo();

}
```

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CloseOpenUndo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UndoStep~CloseOpenUndo.html) | Close and open Undo protocol. Call this method to mark step in Undo action list. |
| Public Method | [CloseUndo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UndoStep~CloseUndo.html) | Close Undo protocol. After call this method Undo action is not possible. |
| Public Method | [Dispose](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UndoStep~Dispose().html) | Virtual deterministic destructor. |
| Public Method | [DoUndo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UndoStep~DoUndo.html) | Overloaded. Make Undo action - reverse all operations up to last CloseOpenUndo call or initalization of UndoStep object. |
| Public Method | [SetUndoDescription](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UndoStep~SetUndoDescription.html) | Set description of Undo action. |


