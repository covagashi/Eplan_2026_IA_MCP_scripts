# Setting Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Search~Setting.html

---

Gets/Sets whether the specified setting of a search is enabled

Syntax

**C#**



public bool this[ 

   Search.Settings id

]; {get; set;}

public:

property bool default [Search.Settings] {

   bool get(Search.Settings id);

   void set (Search.Settings id, bool value);

}


#### Parameters

*id*
:   Search setting value. Cannot be null.

#### Property Value

Value of the setting.
