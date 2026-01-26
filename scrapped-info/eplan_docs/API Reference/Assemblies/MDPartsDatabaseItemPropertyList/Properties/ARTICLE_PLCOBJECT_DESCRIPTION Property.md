# ARTICLE_PLCOBJECT_DESCRIPTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_PLCOBJECT_DESCRIPTION().html

---

Object description # 22038.

Syntax

**C#**



public MDPropertyValue ARTICLE_PLCOBJECT_DESCRIPTION {get; set;}

public:

property MDPropertyValue^ ARTICLE_PLCOBJECT_DESCRIPTION {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. Outputs the object description for parts in the "PLC" product group that has been entered in parts management on the "Properties" tab > hierarchy level "PLC data".
