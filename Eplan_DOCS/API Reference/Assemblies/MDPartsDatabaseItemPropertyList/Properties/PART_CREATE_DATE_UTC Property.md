# PART_CREATE_DATE_UTC Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~PART_CREATE_DATE_UTC().html

---

Creation date (UTC) # 22985.

Syntax

**C#**



public MDPropertyValue PART_CREATE_DATE_UTC {get; set;}

public:

property MDPropertyValue^ PART_CREATE_DATE_UTC {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.DateTime.

Remarks

Shows date and time when the record was created. The time is output in the Coordinated Universal Time (UTC).
