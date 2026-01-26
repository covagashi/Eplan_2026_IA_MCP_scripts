# AllowUserCharacters Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~AllowUserCharacters.html

---

Representation of XDtcDeviceTagCheck.Hierarchy.AllowUserCharacters setting value. In P8-GUI it can be found in the "File" -> "Settings..." Projects/<project>/Devices/DT syntax check:Structure identifier/Special text characters. When this option is enabled, all characters in [UserCharacters](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~UserCharacters.html) string are possible to be used in DeviceTags. To make it work [EnableSyntaxCheck](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~EnableSyntaxCheck.html) must be `true`.

Syntax

**C#**



public bool AllowUserCharacters {get; set;}

public:

property bool AllowUserCharacters {

   bool get();

   void set (    bool value);

}


Remarks

This property might throw this same exceptions what functions **Eplan::EplApi::DataModel::ProjectSettings:** and **Eplan::EplApi::DataModel::ProjectSettings:** might throw.
