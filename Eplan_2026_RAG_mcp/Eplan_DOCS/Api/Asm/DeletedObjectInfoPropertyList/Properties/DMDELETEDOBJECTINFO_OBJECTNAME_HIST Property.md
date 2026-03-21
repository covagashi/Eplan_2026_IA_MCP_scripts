# DMDELETEDOBJECTINFO_OBJECTNAME_HIST Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic195.html

---

Deleted object (further): Name # 36605.

Syntax

**C#**



public PropertyValue DMDELETEDOBJECTINFO_OBJECTNAME_HIST( 

   int index

) {get; set;}

public:

property PropertyValue^ DMDELETEDOBJECTINFO_OBJECTNAME_HIST {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Using the index, this property outputs the name of the other deleted objects which were placed at the same place as the deletion marker. In other words, the name of the second deleted object is output using the index [1]; the name of the third deleted object is output using the index [2] etc. The first deleted object has the highest index value. (The name of the last deleted object is output to the "Deleted object: name" property (ID 36600).)
