# ARTICLE_MEASURED_VARIABLE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_MEASURED_VARIABLE().html

---

Measurand # 26460.

Syntax

**C#**



public MDPropertyValue ARTICLE_MEASURED_VARIABLE {get; set;}

public:

property MDPropertyValue^ ARTICLE_MEASURED_VARIABLE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Physical quantity or characteristic detected by a measuring instrument or sensor. This can be, for example, temperature, pressure, length, volume, mass or another measurable property. The measurand thus defines exactly what is measured.
