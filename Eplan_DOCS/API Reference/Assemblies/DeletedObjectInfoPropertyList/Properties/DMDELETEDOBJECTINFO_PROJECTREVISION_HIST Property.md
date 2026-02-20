# DMDELETEDOBJECTINFO_PROJECTREVISION_HIST Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic197.html

---

Associated project revision (further) # 36611.

Syntax

**C#**



public PropertyValue DMDELETEDOBJECTINFO_PROJECTREVISION_HIST( 

   int index

) {get; set;}

public:

property PropertyValue^ DMDELETEDOBJECTINFO_PROJECTREVISION_HIST {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Using the index, this property outputs the associated project revision of the other deleted pages which are entered at the deletion marker. In other words, the associated project revision of the second deleted page is output using the index [1]; the associated project revision of the third deleted page is output using the index [2] etc. The first deleted page has the highest index value. (The associated project revision of the first deleted page is output to the "Associated project revision" property (ID 36610).)
