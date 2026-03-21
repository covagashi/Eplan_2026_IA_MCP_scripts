# PAGE_REVISION_LOG_DRAFT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_REVISION_LOG_DRAFT().html

---

Page in draft mode # 11076.

Syntax

**C#**



public PropertyValue PAGE_REVISION_LOG_DRAFT {get; set;}

public:

property PropertyValue^ PAGE_REVISION_LOG_DRAFT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

As soon as you make changes to a page in a revision, it is marked as a "draft". This is shown visually with a watermark on the page, and the page is assigned this property. This mark is retained until you complete the page.
