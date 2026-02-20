# PART_ADDRESS_LASTCHANGE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~PART_ADDRESS_LASTCHANGE().html

---

Last editor / Modification date (address) # 22937.

Syntax

**C#**



public MDPropertyValue PART_ADDRESS_LASTCHANGE {get; set;}

public:

property MDPropertyValue^ PART_ADDRESS_LASTCHANGE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Last change to manufacturer/supplier or customer details. Shows the sign-in name of the user who last edited the record along with the date and time of the last change. The time is output in the local time of the user in accordance with the set time zone.
