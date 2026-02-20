# DMDELETEDOBJECTINFO_TIME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeletedObjectInfoPropertyList~DMDELETEDOBJECTINFO_TIME().html

---

Delete date # 36603.

Syntax

**C#**



public PropertyValue DMDELETEDOBJECTINFO_TIME {get; set;}

public:

property PropertyValue^ DMDELETEDOBJECTINFO_TIME {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.DateTime.

Remarks

Shows the time (time and date), at the deletion marker, at which the object was deleted. The time is output in the local time of the user in accordance with the set time zone.
