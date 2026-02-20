# ARTICLE_ELECTRICAL_INTERFACE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_ELECTRICAL_INTERFACE().html

---

Electrical interface # 26036.

Syntax

**C#**



public MDPropertyValue ARTICLE_ELECTRICAL_INTERFACE {get; set;}

public:

property MDPropertyValue^ ARTICLE_ELECTRICAL_INTERFACE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Describes the properties of the electrical interface which are used to make the process data available in the form of a measurement signal or a data protocol. Example: For a plug, the specific features such as number of poles, nominal voltage, nominal current and plug type describe the properties of this interface.
