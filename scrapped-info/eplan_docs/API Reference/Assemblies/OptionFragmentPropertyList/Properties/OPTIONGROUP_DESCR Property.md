# OPTIONGROUP_DESCR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionFragmentPropertyList~OPTIONGROUP_DESCR().html

---

Project option group: Description # 23104.

Syntax

**C#**



public PropertyValue OPTIONGROUP_DESCR {get; set;}

public:

property PropertyValue^ OPTIONGROUP_DESCR {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

The description can be multi-language and is shown in the status bar when the project options group is selected in the project options navigator tree.
