# ARTICLE_REPORT_SYMBOL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_REPORT_SYMBOL(Int32).html

---

Symbol for reports # 22228.

Syntax

**C#**



public MDPropertyValue ARTICLE_REPORT_SYMBOL( 

   int index

) {get; set;}

public:

property MDPropertyValue^ ARTICLE_REPORT_SYMBOL {

   MDPropertyValue^ get(int index);

   void set (int index, MDPropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 20.

In this property, you can enter symbols that will be used in the report of conditional forms. The symbols are entered in parts management on the "Properties" tab > hierarchy level "Data for reports", with a maximum of 20.
