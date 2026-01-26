# PART_LASTCHANGE_DATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~PART_LASTCHANGE_DATE().html

---

Modification date # 22981.

Syntax

**C#**



public MDPropertyValue PART_LASTCHANGE_DATE {get; set;}

public:

property MDPropertyValue^ PART_LASTCHANGE_DATE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.DateTime.

Remarks

Shows the date and time of the last change. The time is output in the local time of the user in accordance with the set time zone.
