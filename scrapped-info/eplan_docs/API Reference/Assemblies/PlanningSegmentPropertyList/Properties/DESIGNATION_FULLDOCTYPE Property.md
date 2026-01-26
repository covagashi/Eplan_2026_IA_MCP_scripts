# DESIGNATION_FULLDOCTYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~DESIGNATION_FULLDOCTYPE().html

---

Document type # 1520.

Syntax

**C#**



public PropertyValue DESIGNATION_FULLDOCTYPE {get; set;}

public:

property PropertyValue^ DESIGNATION_FULLDOCTYPE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Part of the structure identifier of the document type that is entered at this structure segment or planning object. The entire structure identifier of a planning object consists of all parts of the superior structure segments and planning objects.
