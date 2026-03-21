# ActiveScheme Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSections~ActiveScheme.html

---

Gets/Sets active working section scheme for current user.

Syntax

**C#**



public string ActiveScheme {get; set;}

public:

property String^ ActiveScheme {

   String^ get();

   void set (    String^ value);

}


Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | While setting value when State is equal to Disabled or EnabledTemporary. |
