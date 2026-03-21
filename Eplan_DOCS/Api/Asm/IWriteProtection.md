# IWriteProtection

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IWriteProtection.html

---

Defines methods to manipulate write protection on object.

Syntax

**C#**



public interface IWriteProtection

public interface class IWriteProtection


Example

The following example shows how to use the interface.

**C#**

```


oFunction.Properties.HARNESS_NAME = "old value";

oFunction.WriteProtected = true;

using (UndoStep oUndoStep = new UndoManager().CreateUndoStep())

{

    oFunction.Properties.HARNESS_NAME = "new value";

}

Console.WriteLine(oFunction.Properties.HARNESS_NAME.ToString());  //will be 'old value' returned

```

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [WriteProtected](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IWriteProtection~WriteProtected.html) | Checks if an object is currently write protected or sets manual write protection |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [GetWriteProtectionFlagSet](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IWriteProtection~GetWriteProtectionFlagSet.html) | Checks what kind of a write protection was set. |
| Method | [PauseWriteProtection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IWriteProtection~PauseWriteProtection.html) | Temporarily disables write protection. Note that current write protection flags are not cleared. |


