# PAGE_REVISION_LOG_EDITINGAREA Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_REVISION_LOG_EDITINGAREA(Int32).html

---

Defined working section (from change tracking) # 11079.

Syntax

**C#**



public PropertyValue PAGE_REVISION_LOG_EDITINGAREA( 

   int index

) {get; set;}

public:

property PropertyValue^ PAGE_REVISION_LOG_EDITINGAREA {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

The property is used during the revisioning of defined working sections. Displays the defined working section to which the page (or the layout space) belongs that was changed in a revision. A max. of 1,000 is allowed. You can, for example, use the property as a filter criterion in the page navigator in order to filter pages that were changed at a specific revision (e.g. Index 2).
