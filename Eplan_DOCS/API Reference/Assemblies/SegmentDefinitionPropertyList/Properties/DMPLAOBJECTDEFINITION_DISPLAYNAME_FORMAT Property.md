# DMPLAOBJECTDEFINITION_DISPLAYNAME_FORMAT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1067.html

---

Structure identifiers without separators # 44033.

Syntax

**C#**



public PropertyValue DMPLAOBJECTDEFINITION_NO_STRUCTUREDELIMITER {get; set;}

public:

property PropertyValue^ DMPLAOBJECTDEFINITION_NO_STRUCTUREDELIMITER {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

If this property is activated, same-type structure identifiers of nested segments are combined without separators.

Example: A segment has the structure identifier "=A1" and the subordinate segment "=12". In the full designation of the subordinate segment, "=A112" is displayed if the property is activated; otherwise, "=A1.12".
