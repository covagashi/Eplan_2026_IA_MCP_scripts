# DMDELETEDOBJECTINFO_TIME_HIST Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeletedObjectInfoPropertyList~DMDELETEDOBJECTINFO_TIME_HIST(Int32).html

---

Delete date (further) # 36608.

Syntax

**C#**



public PropertyValue DMDELETEDOBJECTINFO_TIME_HIST( 

   int index

) {get; set;}

public:

property PropertyValue^ DMDELETEDOBJECTINFO_TIME_HIST {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.DateTime.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Using the index, this property outputs the delete date of the other deleted objects which were placed at the same place as the deletion marker. In other words, the delete date of the second deleted object is output using the index [1]; the delete date of the third deleted object is output using the index [2] etc. The first deleted object has the highest index value. (The delete date of the last deleted object is output to the "Delete date" property (ID 36603).) The time is output in the local time of the user in accordance with the set time zone.
