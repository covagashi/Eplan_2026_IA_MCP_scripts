# ARTICLE_EDP_IMPORT_DATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_EDP_IMPORT_DATE().html

---

Data Portal import date # 22391.

Syntax

**C#**



public MDPropertyValue ARTICLE_EDP_IMPORT_DATE {get; set;}

public:

property MDPropertyValue^ ARTICLE_EDP_IMPORT_DATE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.DateTime.

Remarks

This property can be used to specifically filter for the parts in the parts management that were imported from the Eplan Data Portal. A date is entered for this property when a part is imported from the Eplan Data Portal. The import date cannot be edited (for example via external editing), and is also not taken into consideration during the data exchange (for example during the export and import in EDZ or XML format). While copying and pasting a part, the value of this property is not transferred to the new part. In such a case the property is subsequently empty.
