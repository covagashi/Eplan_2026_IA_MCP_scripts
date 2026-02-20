# DMDELETEDOBJECTINFO_USER_HIST Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeletedObjectInfoPropertyList~DMDELETEDOBJECTINFO_USER_HIST(Int32).html

---

User name (further) # 36607.

Syntax

**C#**



public PropertyValue DMDELETEDOBJECTINFO_USER_HIST( 

   int index

) {get; set;}

public:

property PropertyValue^ DMDELETEDOBJECTINFO_USER_HIST {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Using the index, this property outputs the user name of the other deleted objects which were placed at the same place as the deletion marker. In other words, the user name of the second deleted object is output using the index [1]; the user name of the third deleted object is output using the index [2] etc. The first deleted object has the highest index value. (The user name of the last deleted object is output to the "User name" property (ID 36602).)
