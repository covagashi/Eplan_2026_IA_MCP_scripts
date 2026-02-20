# ValidParents Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinition~ValidParents.html

---

Array with identifying names of segment definitions.

Syntax

**C#**



public string[] ValidParents {get; set;}

public:

property array<String^>^ ValidParents {

   array<String^>^ get();

   void set (    array<String^>^ value);

}


Remarks

This list is used to determine possible parents that a planning object with this segment definition can have. A planning object with segment definition which identifying name is in this list, can be a parent of other planning object. If a segment definition with identifying name from this property has sub segment definitions then planning object with those definitions are also valid parents.

This property can contain an empty string which means that planning object with this segment definition can have a project as parent.
