# DMPLAOBJECT_IGNORE_MANDATORY_PROPERTY_VERIFICATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic843.html

---

Linked segments: Name # 44063.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_LINK_CHILD_NAME( 

   int index

) {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_LINK_CHILD_NAME {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 100.

Shows at a segment which other segments are linked to this segment through links. Up to 100 links can be differentiated by using the index. The complete designation of the linked segment is displayed as a value.
