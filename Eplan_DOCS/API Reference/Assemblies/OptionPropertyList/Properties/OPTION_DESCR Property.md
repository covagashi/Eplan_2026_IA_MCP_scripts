# OPTION_DESCR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionPropertyList~OPTION_DESCR().html

---

Project option: Description # 23106.

Syntax

**C#**



public PropertyValue OPTION_DESCR {get; set;}

public:

property PropertyValue^ OPTION_DESCR {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

The description can be multi-language and is shown in the status bar when the project option is selected in the project options navigator tree.
