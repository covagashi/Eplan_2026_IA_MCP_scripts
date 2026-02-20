# DMDELETEDOBJECTINFO_REVISION_LOG_DESCRIPTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic201.html

---

Deleted object: Revision description (change tracking) # 36615.

Syntax

**C#**



public PropertyValue DMDELETEDOBJECTINFO_REVISION_LOG_DESCRIPTION {get; set;}

public:

property PropertyValue^ DMDELETEDOBJECTINFO_REVISION_LOG_DESCRIPTION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Revision description for a deleted object. The text can be entered directly while deleting the object when the "Always prompt for description of page modification" project setting is enabled. The text can be edited later in the property dialog of the deletion marker.
