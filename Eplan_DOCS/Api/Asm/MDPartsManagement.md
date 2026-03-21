# MDPartsManagement

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement.html

---

To open or create a parts database there is the management class MDPartsManagement.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.MasterData.MDPartsManagement**

Syntax

**C#**



public class MDPartsManagement

public ref class MDPartsManagement


Example

**C#**

```
MDPartsManagement pm = new MDPartsManagement();

MDPartsDatabase db = pm.OpenDatabase();
```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [MDPartsManagement Constructor](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~_ctor.html) | constructor of MDPartsManagement |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [PartsDatabaseState](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~PartsDatabaseState.html) | Value of state connection to database that is currently used. |
| Public Property | [SelectedPartsDatabase](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~SelectedPartsDatabase.html) | The parts database that is currently used. |
| Public Propertystatic (Shared in Visual Basic) | [SelectedPartsDatabaseAsString](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~SelectedPartsDatabaseAsString.html) | The parts database that is currently used as a connection string or a file. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CreateDatabase](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~CreateDatabase.html) | Create a new parts database. |
| Public Method | [ExportParts](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~ExportParts.html) | Exports parts and other parts management items like addresses, constructions, terminals, accessory lists and accessory placements from the system's parts database. |
| Public Method | [GetSelectedPartDatabaseItems](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~GetSelectedPartDatabaseItems.html) | Gets the selected PartItem(s) in the parts management (or parts navigator) |
| Public Method | [ImportParts](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~ImportParts.html) | Overloaded. Imports parts to the system database. |
| Public Method | [OpenDatabase](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~OpenDatabase.html) | Overloaded. Opens the given parts database. |
| Public Method | [RefreshPartsManagementDialog](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~RefreshPartsManagementDialog.html) | Refreshes the parts management dialog. That is useful after making changes on the parts database items. |
| Public Method | [RegisterAddin](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~RegisterAddin.html) | Registers an add-in for the parts management. The given action will be called for several 'actions'. |
| Public Method | [RegisterItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~RegisterItem.html) | Registers a new item type into the parts management. That item type will be shown in the tree view (while calling the 'actions' GetRootLevel and GetNextLevel). |
| Public Method | [RegisterTabsheet](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~RegisterTabsheet.html) | Registers an additional tab sheet for the given item type. |
| Public Method | [RemoveDatabase](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~RemoveDatabase.html) | Removes the given parts database. |
| Public Method | [SelectItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~SelectItem.html) | Selects the given item in the parts management dialog. |
| Public Method | [SetModified](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~SetModified.html) | Set the parts management dialog modified. |
| Public Method | [SumUpFunctionTemplates](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~SumUpFunctionTemplates.html) |  |
| Public Method | [UnregisterAddin](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~UnregisterAddin.html) | Unregisters an add-in that was registered with RegisterAddin. |
| Public Method | [UnregisterItem](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~UnregisterItem.html) | The given item type will be unregisterd. |
| Public Method | [UnregisterTabsheet](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~UnregisterTabsheet.html) | Unregisters a tab sheet that was registerd with RegisterTabsheet(). |
| Public Method | [UpgradePartsDb](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~UpgradePartsDb.html) | Overloaded. Upgrades parts database. |


