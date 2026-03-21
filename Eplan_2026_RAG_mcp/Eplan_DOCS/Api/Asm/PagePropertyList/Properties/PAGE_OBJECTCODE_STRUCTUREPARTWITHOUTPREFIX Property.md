# PAGE_OBJECTCODE_STRUCTUREPARTWITHOUTPREFIX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_OBJECTCODE_STRUCTUREPARTWITHOUTPREFIX(Int32).html

---

Part of the structure identifier without separators stored in the object identifier # 11039.

Syntax

**C#**



public PropertyValue PAGE_OBJECTCODE_STRUCTUREPARTWITHOUTPREFIX( 

   int index

) {get; set;}

public:

property PropertyValue^ PAGE_OBJECTCODE_STRUCTUREPARTWITHOUTPREFIX {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 10.

Supplies a part of the unique structure identifier without leading separator stored in the object identifier. An empty string is output either if no valid structure identifier is stored in the object identifier or if several structure identifiers are stored. This property serves to display in the page navigator.
