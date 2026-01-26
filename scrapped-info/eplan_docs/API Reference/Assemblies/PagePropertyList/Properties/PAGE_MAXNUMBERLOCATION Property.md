# PAGE_MAXNUMBERLOCATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_MAXNUMBERLOCATION().html

---

Highest page number per structure # 11043.

Syntax

**C#**



public PropertyValue PAGE_MAXNUMBERLOCATION {get; set;}

public:

property PropertyValue^ PAGE_MAXNUMBERLOCATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Indicates the highest number of pages used within a structure identifier. For example, if three pages are available with the page numbers "1," "3" and "5" under the location designation "ET1", "5" is output here.
