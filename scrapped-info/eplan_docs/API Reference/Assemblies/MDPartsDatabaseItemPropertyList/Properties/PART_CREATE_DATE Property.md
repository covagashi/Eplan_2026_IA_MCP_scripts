# PART_CREATE_DATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~PART_CREATE_DATE().html

---

Creation date # 22983.

Syntax

**C#**



public MDPropertyValue PART_CREATE_DATE {get; set;}

public:

property MDPropertyValue^ PART_CREATE_DATE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.DateTime.

Remarks

Shows date and time when the record was created. The time is output in the local time of the user in accordance with the set time zone.
