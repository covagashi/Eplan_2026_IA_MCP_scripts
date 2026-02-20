# CloseOpenUndo Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UndoStep~CloseOpenUndo.html

---

Close and open Undo protocol. Call this method to mark step in Undo action list.

Syntax

**C#**



public void CloseOpenUndo()

public:

void CloseOpenUndo();


Remarks

Note that after using this method calling [DoUndo(Boolean)](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UndoStep~DoUndo(Boolean).html) will reverse all operations up to this call.
