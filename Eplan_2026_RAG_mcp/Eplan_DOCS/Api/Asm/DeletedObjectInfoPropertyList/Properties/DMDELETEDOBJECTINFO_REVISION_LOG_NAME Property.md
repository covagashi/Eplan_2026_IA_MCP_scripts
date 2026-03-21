# DMDELETEDOBJECTINFO_REVISION_LOG_NAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeletedObjectInfoPropertyList~DMDELETEDOBJECTINFO_REVISION_LOG_NAME().html

---

Deleted object: Revision index # 36614.

Syntax

**C#**



public PropertyValue DMDELETEDOBJECTINFO_REVISION_LOG_NAME {get; set;}

public:

property PropertyValue^ DMDELETEDOBJECTINFO_REVISION_LOG_NAME {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Text for identifying a deleted object. The text can be entered directly while deleting the object when the "Always prompt for description of page modification" project setting is enabled. The text can be edited later in the property dialog of the deletion marker.
