# ManualPageDescription Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~ManualPageDescription.html

---

Text used for describing page, if automatic page description if switched off.

Syntax

**C#**



public MultiLangString ManualPageDescription {get; set;}

public:

property MultiLangString^ ManualPageDescription {

   MultiLangString^ get();

   void set (    MultiLangString^ value);

}


Remarks

If setting a `null` value to this property empty multilang string is set. When any not empty value is set then property `IsAutomaticPageDescription` is set to `false`.
