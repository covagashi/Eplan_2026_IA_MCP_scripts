# PlantDesignationNumbersOnly Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~PlantDesignationNumbersOnly.html

---

Representation of XDtcDeviceTagCheck.Hierarchy.PlantDesignationNumbersOnly setting value. In P8-GUI it can be found in the "File" -> "Settings..." Projects/<project>/Devices/DT syntax check:Structure identifier/Valid special characters. When this option is enabled (has `true` value) only numbers can be used in DeviceTag syntax. To make it work [EnableSyntaxCheck](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~EnableSyntaxCheck.html) must be `true`.

Syntax

**C#**



public bool PlantDesignationNumbersOnly {get; set;}

public:

property bool PlantDesignationNumbersOnly {

   bool get();

   void set (    bool value);

}


Remarks

This property might throw this same exceptions what functions **Eplan::EplApi::DataModel::ProjectSettings:** and **Eplan::EplApi::DataModel::ProjectSettings:** might throw.
