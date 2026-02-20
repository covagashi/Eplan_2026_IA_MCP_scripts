# ListSelectDecisionContext

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.ListSelectDecisionContext.html

---

This class can be used for a standard Eplan decider

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.Base.ListSelectDecisionContext**

Syntax

**C#**



public class ListSelectDecisionContext

public ref class ListSelectDecisionContext


Example

Example of using Decider class with a ListSelectDecisionContext :

**C#**

```
StringCollection collection = new StringCollection();

collection.Add("Content 1");

collection.Add("Content 2");

collection.Add("Content 3");

ListSelectDecisionContext listSelectDecisionContext = new ListSelectDecisionContext(collection, "Content 2", "Dialog Title");

Decider oDecision = new Decider();

EnumDecisionReturn eAnswer = oDecision.Decide(listSelectDecisionContext);

if (eAnswer != EnumDecisionReturn.eOK)

{

    return false;

}

if (listSelectDecisionContext.AllowMultiSelect)

{

    StringCollection selectedEntries = listSelectDecisionContext.SelectedEntries;

}

else

{

    long index = listSelectDecisionContext.SelectedIndex;

    string strEntry = listSelectDecisionContext.SelectedEntry;

}

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [ListSelectDecisionContext Constructor](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ListSelectDecisionContext~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AllowMultiSelect](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ListSelectDecisionContext~AllowMultiSelect.html) | Set or get the flag for multi selection. |
| Public Property | [Entries](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ListSelectDecisionContext~Entries.html) | Gets all entries |
| Public Property | [SelectedEntries](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ListSelectDecisionContext~SelectedEntries.html) | Gets all selected entries (Use this property if multi selection is enabled) |
| Public Property | [SelectedEntry](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ListSelectDecisionContext~SelectedEntry.html) | Gets the selected entries |
| Public Property | [SelectedIndex](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ListSelectDecisionContext~SelectedIndex.html) | Gets the selected index from Entries |
| Public Property | [Title](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ListSelectDecisionContext~Title.html) | The title for the decider. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ListSelectDecisionContext~Dispose().html) | Destructor for deterministic finalization of ListSelectDecisionContext object. |


