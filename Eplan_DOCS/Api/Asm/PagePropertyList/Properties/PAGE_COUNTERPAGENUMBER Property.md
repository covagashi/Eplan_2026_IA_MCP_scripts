# PAGE_COUNTERPAGENUMBER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_COUNTERPAGENUMBER().html

---

Counter page number # 25020.

Syntax

**C#**



public PropertyValue PAGE_COUNTERPAGENUMBER {get; set;}

public:

property PropertyValue^ PAGE_COUNTERPAGENUMBER {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

This property automatically increments the pages in the project in accordance with the order in the page structure. You can insert this property as special text and use it for displaying a sequential page number, for example in the page properties, in the graphical editor or on report pages.
