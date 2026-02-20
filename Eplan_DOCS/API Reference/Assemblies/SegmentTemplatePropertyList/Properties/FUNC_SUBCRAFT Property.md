# FUNC_SUBCRAFT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplatePropertyList~FUNC_SUBCRAFT().html

---

Subtrade # 20467.

Syntax

**C#**



public PropertyValue FUNC_SUBCRAFT {get; set;}

public:

property PropertyValue^ FUNC_SUBCRAFT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

A trade can consist of multiple so-called "subtrades". For instance, the trade "Cooling" can consist of the subtrades "Water cooling" and "Oil cooling". The specification of subtrades as additional function property makes it possible to construct very detailed reports in Eplan Fluid.
