# PART_CREATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~PART_CREATE().html

---

Creator / Creation date # 22902.

Syntax

**C#**



public MDPropertyValue PART_CREATE {get; set;}

public:

property MDPropertyValue^ PART_CREATE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Creation date of the part. The time is output in the local time of the user in accordance with the set time zone.
