# ARTICLE_PARTIAL_LENGTH Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_PARTIAL_LENGTH().html

---

Subset / length # 20496.

Syntax

**C#**



public MDPropertyValue ARTICLE_PARTIAL_LENGTH {get; set;}

public:

property MDPropertyValue^ ARTICLE_PARTIAL_LENGTH {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Subset of a part, e.g. 5 pieces of a part, which are only provided in conduits of up to 100. At parts for cables, connections and their accessories (for example shrink tubes or insulating tubes) the contents of this property is evaluated as a length with specification of the displayed measuring unit and the entry of decimal values is possible, for example "0.7 m". If you do not enter a unit, the unit of length specified in the project settings is used. The value entered here is synchronized with the cable length (Length field in the Cable tab of the property dialog) for the main part of a cable.
