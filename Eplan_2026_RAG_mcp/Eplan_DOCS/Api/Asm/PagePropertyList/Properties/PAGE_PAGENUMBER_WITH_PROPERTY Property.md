# PAGE_PAGENUMBER_WITH_PROPERTY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_PAGENUMBER_WITH_PROPERTY().html

---

Page counter per property # 11064.

Syntax

**C#**



public PropertyValue PAGE_PAGENUMBER_WITH_PROPERTY {get; set;}

public:

property PropertyValue^ PAGE_PAGENUMBER_WITH_PROPERTY {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

With this property you can have the information displayed in the page properties or in a plot frame on the number of pages including the present one exist with a specific property (for example Page "4" with function designation "A31"). The property is specified in the "Number of pages / Page name per property" project setting. A report run is used to count the pages with the same value as this property, and the counter is written to the "Page counter per property" property.
