# PAGE_OBJECTCODE_STRUCTUREWITHOUTPREFIX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_OBJECTCODE_STRUCTUREWITHOUTPREFIX().html

---

Structure identifier with separators stored in the object identifier # 11038.

Syntax

**C#**



public PropertyValue PAGE_OBJECTCODE_STRUCTUREWITHOUTPREFIX {get; set;}

public:

property PropertyValue^ PAGE_OBJECTCODE_STRUCTUREWITHOUTPREFIX {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

The unique structure identifier without leading separator stored in the object identifier. An empty string is output either if no valid structure identifier is stored in the object identifier or if several structure identifiers are stored. This property serves for display purposes in the page navigator.
