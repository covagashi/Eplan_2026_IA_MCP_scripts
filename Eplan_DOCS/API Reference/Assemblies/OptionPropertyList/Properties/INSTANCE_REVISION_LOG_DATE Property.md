# INSTANCE_REVISION_LOG_DATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionPropertyList~INSTANCE_REVISION_LOG_DATE().html

---

Modification date (change tracking) # 19032.

Syntax

**C#**



public PropertyValue INSTANCE_REVISION_LOG_DATE {get; set;}

public:

property PropertyValue^ INSTANCE_REVISION_LOG_DATE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.DateTime.

Remarks

Date on which an object in a revision was modified. This property is displayed by default in the automatically generated revision marker. The time is output in the local time of the user in accordance with the set time zone.
