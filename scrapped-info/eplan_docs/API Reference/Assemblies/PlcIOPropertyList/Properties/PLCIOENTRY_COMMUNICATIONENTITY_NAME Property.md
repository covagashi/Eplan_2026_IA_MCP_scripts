# PLCIOENTRY_COMMUNICATIONENTITY_NAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlcIOPropertyList~PLCIOENTRY_COMMUNICATIONENTITY_NAME().html

---

Name of the communication unit # 23400.

Syntax

**C#**



public PropertyValue PLCIOENTRY_COMMUNICATIONENTITY_NAME {get; set;}

public:

property PropertyValue^ PLCIOENTRY_COMMUNICATIONENTITY_NAME {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is no longer in use and only taken into consideration in old projects. PLC addresses can be assigned to a particular communication unit of a PLC card. This property represents the second part of the reference to the communication unit. The first part of the reference is the database ID of the associated PLC box.
