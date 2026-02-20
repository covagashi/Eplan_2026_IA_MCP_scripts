# INSTANCE_REVISION_LOG_MARKER_FORMAT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1065.html

---

Segment definition: Preceding sign also at the beginning # 44046.

Syntax

**C#**



public PropertyValue DMPLAOBJECTDEFINITION_BEGINWITHPREFIX {get; set;}

public:

property PropertyValue^ DMPLAOBJECTDEFINITION_BEGINWITHPREFIX {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

If this check box is enabled, the preceding sign of a segment with this segment definition is always displayed in the full designation. The preceding sign is displayed also if a segment forms a top hierarchy level in the tree structure and its designation is at the beginning of the full designation.

If the check box is deactivated, the preceding sign will be hidden if the segment in question is at the beginning of the full designation. This is the default setting.
