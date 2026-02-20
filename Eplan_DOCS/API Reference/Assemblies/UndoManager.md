# UndoManager

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UndoManager.html

---

Class representing DataModel's Undo. It implements [System.IDisposable](#) interface.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.DataModel.UndoManager**

Syntax

**C#**



public class UndoManager

public ref class UndoManager


Example

UndoStep usage - only inside "using".

**C#**

```
using (UndoStep undo = new UndoManager().CreateUndoStep())

{

	using(Transaction txn = new TransactionManager().CreateTransaction())

	{

		Function f;

		f.Name = "F1";

		txn.Commit();

	}

    undo.DoUndo();

}
```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [UndoManager Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UndoManager~_ctor.html) | Constructor. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CreateUndoStep](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UndoManager~CreateUndoStep.html) | Creates object representing a UndoStep. |
| Public Method | [Dispose](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UndoManager~Dispose().html) | Virtual deterministic destructor. |


