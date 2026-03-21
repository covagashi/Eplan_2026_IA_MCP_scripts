# AreUserDefinedSettings Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ContactImage~AreUserDefinedSettings.html

---

If `true` P8 uses settings from property [DisplayMask](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ContactImage~DisplayMask.html) to display contact image.

Syntax

**C#**



public bool AreUserDefinedSettings {get; set;}

public:

property bool AreUserDefinedSettings {

   bool get();

   void set (    bool value);

}


Remarks

If value is `false` then project settings are used.
