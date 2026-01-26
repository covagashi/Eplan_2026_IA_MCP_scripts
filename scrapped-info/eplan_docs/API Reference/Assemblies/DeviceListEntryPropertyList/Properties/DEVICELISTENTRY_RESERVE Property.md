# DEVICELISTENTRY_RESERVE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceListEntryPropertyList~DEVICELISTENTRY_RESERVE().html

---

Spare quantity # 23206.

Syntax

**C#**



public PropertyValue DEVICELISTENTRY_RESERVE {get; set;}

public:

property PropertyValue^ DEVICELISTENTRY_RESERVE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

This property is read-only..

Contains the difference between the property Total number allowed and the property Used unit quantity. This property can be displayed in the device list.
