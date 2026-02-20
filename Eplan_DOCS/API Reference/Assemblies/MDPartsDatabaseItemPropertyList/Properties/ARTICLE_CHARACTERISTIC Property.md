# ARTICLE_CHARACTERISTIC Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_CHARACTERISTIC().html

---

Characteristic curve # 26403.

Syntax

**C#**



public MDPropertyValue ARTICLE_CHARACTERISTIC {get; set;}

public:

property MDPropertyValue^ ARTICLE_CHARACTERISTIC {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Graphical representation of the relationship between two or more physical quantities of a product or item. Example: For a diode, the I-U characteristic curve shows the relation between the current (I) and the voltage (U) at the diode.
