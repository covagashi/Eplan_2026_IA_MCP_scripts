# PAGE_REVISION_LOG_CHANGE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_REVISION_LOG_CHANGE(Int32).html

---

Reason for revision change (change tracking) # 11073.

Syntax

**C#**



public PropertyValue PAGE_REVISION_LOG_CHANGE( 

   int index

) {get; set;}

public:

property PropertyValue^ PAGE_REVISION_LOG_CHANGE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Reason for revision change (change tracking), max. 1,000 allowed.
