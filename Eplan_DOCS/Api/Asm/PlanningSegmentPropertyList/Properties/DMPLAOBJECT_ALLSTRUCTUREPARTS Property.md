# DMPLAOBJECT_ALLSTRUCTUREPARTS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~DMPLAOBJECT_ALLSTRUCTUREPARTS().html

---

Structure identifier (Segment) # 44032.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_ALLSTRUCTUREPARTS {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_ALLSTRUCTUREPARTS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Specifies all structure identifiers including preceding sign entered at the structure segment or planning object, provided they have a value. No preceding sign is displayed for empty structure identifiers. For example, instead of the string "==A1+-", only "==A1" is displayed.
