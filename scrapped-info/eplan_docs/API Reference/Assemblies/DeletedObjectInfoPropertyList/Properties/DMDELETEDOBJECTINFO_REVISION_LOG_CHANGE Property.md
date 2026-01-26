# DMDELETEDOBJECTINFO_REVISION_LOG_CHANGE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic200.html

---

Deleted object: Reason for revision change (change tracking) # 36616.

Syntax

**C#**



public PropertyValue DMDELETEDOBJECTINFO_REVISION_LOG_CHANGE {get; set;}

public:

property PropertyValue^ DMDELETEDOBJECTINFO_REVISION_LOG_CHANGE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Revision change reason for a deleted object. The text can be entered directly while deleting the object when the "Always prompt for description of page modification" project setting is enabled. The text can be edited later in the property dialog of the deletion marker.
