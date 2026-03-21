# OPTIONFRAGMENT_DESCR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionFragmentPropertyList~OPTIONFRAGMENT_DESCR().html

---

Project option section: Description # 23105.

Syntax

**C#**



public PropertyValue OPTIONFRAGMENT_DESCR {get; set;}

public:

property PropertyValue^ OPTIONFRAGMENT_DESCR {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

The description can be multi-language and is shown in the status bar when the section is selected in the project options navigator tree.
