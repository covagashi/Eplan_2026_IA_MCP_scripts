# FUNC_DEVICETYPE_MANUAL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_DEVICETYPE_MANUAL().html

---

Device group # 20294.

Syntax

**C#**



public PropertyValue FUNC_DEVICETYPE_MANUAL {get; set;}

public:

property PropertyValue^ FUNC_DEVICETYPE_MANUAL {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Manual assignment of the function to a device group (which determines the DT format). Using this property, you can select another DT format for specific functions, e.g., a connection can then have a different DT format than a cable. If the property is empty, the device group will be derived automatically from the function definition.
