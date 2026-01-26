# AllowSpecialCharacters Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~AllowSpecialCharacters.html

---

Representation of XDtcDeviceTagCheck.Hierarchy.AllowSpecialCharacters setting value. In P8-GUI it can be found in "File" -> "Settings..." Projects/<project>/Devices/DT syntax check:Structure identifier/Valid special characters. It provides possibility to use special characters in DeviceTag. Special characters are: `\_' `?' `\*' `,' . It might be changed by dynamic configuration. To make it work [EnableSyntaxCheck](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~EnableSyntaxCheck.html) must be `true`.

Syntax

**C#**



public bool AllowSpecialCharacters {get; set;}

public:

property bool AllowSpecialCharacters {

   bool get();

   void set (    bool value);

}


Remarks

This property might throw this same exceptions what functions **Eplan::EplApi::DataModel::ProjectSettings:** and **Eplan::EplApi::DataModel::ProjectSettings:** might throw.
