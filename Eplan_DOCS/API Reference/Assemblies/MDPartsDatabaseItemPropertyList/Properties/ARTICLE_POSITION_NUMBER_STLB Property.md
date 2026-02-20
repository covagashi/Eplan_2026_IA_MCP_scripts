# ARTICLE_POSITION_NUMBER_STLB Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_POSITION_NUMBER_STLB().html

---

Performance description, standardized: Item number (device, utility, service) # 26532.

Syntax

**C#**



public MDPropertyValue ARTICLE_POSITION_NUMBER_STLB {get; set;}

public:

property MDPropertyValue^ ARTICLE_POSITION_NUMBER_STLB {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Unique identification number for a specific service item in the bill of quantities. Example: A specific number stands for the service "Concrete works: Concrete a foundation".
