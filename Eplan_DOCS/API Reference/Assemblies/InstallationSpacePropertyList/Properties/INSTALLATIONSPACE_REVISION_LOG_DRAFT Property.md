# INSTALLATIONSPACE_REVISION_LOG_DRAFT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic483.html

---

Layout space in draft mode # 36451.

Syntax

**C#**



public PropertyValue INSTALLATIONSPACE_REVISION_LOG_DRAFT {get; set;}

public:

property PropertyValue^ INSTALLATIONSPACE_REVISION_LOG_DRAFT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

When you carry out changes in a layout space in a revision, it is identified as "Draft". This is displayed graphically by a watermark in the 3D view and this property is assigned to the layout space. This identifier stays there until you close the layout space.
