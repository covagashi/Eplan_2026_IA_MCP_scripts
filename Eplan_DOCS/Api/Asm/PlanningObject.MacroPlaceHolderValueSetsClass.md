# PlanningObject.MacroPlaceHolderValueSetsClass

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningObject+MacroPlaceHolderValueSetsClass.html

---

Represents macro placeholder records of a planning object

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.DataModel.Planning.PlanningObject.MacroPlaceHolderValueSetsClass**

Syntax

**C#**



[DefaultMember("Item")]

public class PlanningObject.MacroPlaceHolderValueSetsClass

[DefaultMember("Item")]

public ref class PlanningObject.MacroPlaceHolderValueSetsClass


Example

**C#**

```


// getting macro placeholder value sets from planning object

var oMacroPlaceHolderValueSets = oPlanningObject.MacroPlaceHolderValueSets;

// defining value as string in multiple languages

string text = "Test!!!";

MultiLangString mls = new MultiLangString();

mls.AddString(ISOCode.Language.L_en_US, text);

mls.AddString(ISOCode.Language.L_de_DE, text);

// changing every variable to defined value

foreach (var oMacroPlaceHolderValueSet in oMacroPlaceHolderValueSets)

{

    foreach (string variable in oMacroPlaceHolderValueSet.VariableNames)

    {

        oMacroPlaceHolderValueSet[variable] = mls;

    }

}

// writing data back to planning object

oMacroPlaceHolderValueSets.Store();

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [PlanningObject.MacroPlaceHolderValueSetsClass Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningObject+MacroPlaceHolderValueSetsClass~_ctor.html) | Constructor |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Count](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningObject+MacroPlaceHolderValueSetsClass~Count.html) | Returns number of macro placeholder value sets |
| Public Property | [Item](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningObject+MacroPlaceHolderValueSetsClass~Item.html) | Overloaded. |
| Public Property | [Source](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningObject+MacroPlaceHolderValueSetsClass~Source.html) | Planning object to which macro placeholder value sets belong |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Contains](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningObject+MacroPlaceHolderValueSetsClass~Contains.html) | Determines whether planning object stores macro placeholder record |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningObject+MacroPlaceHolderValueSetsClass~CopyTo.html) | Copy collection to an array |
| Public Method | [Dispose](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningObject+MacroPlaceHolderValueSetsClass~Dispose().html) | Destructor for deterministic finalization of MacroPlaceHolderValueSetsClass object. |
| Public Method | [GetEnumerator](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningObject+MacroPlaceHolderValueSetsClass~GetEnumerator.html) | Gets enumertator in collection of MacroPlaceholderValueSets |
| Public Method | [GetEnumerator2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningObject+MacroPlaceHolderValueSetsClass~GetEnumerator2.html) | Gets enumertator in collection of MacroPlaceholderValueSets. The same as GetEnumerator. |
| Public Method | [Store](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningObject+MacroPlaceHolderValueSetsClass~Store.html) | Stores back macro placeholder value sets to planning object. |
| Public Method | [UpdateFromMacro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningObject+MacroPlaceHolderValueSetsClass~UpdateFromMacro.html) | Updates planning object's macro placeholder value sets with data from macro (e.g. after macro has changed) |


