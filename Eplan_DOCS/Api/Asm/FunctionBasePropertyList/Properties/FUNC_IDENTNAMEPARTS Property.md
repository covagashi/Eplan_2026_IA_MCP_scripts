# FUNC_IDENTNAMEPARTS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBasePropertyList~FUNC_IDENTNAMEPARTS().html

---

Identifying name elements # 20095.

Syntax

**C#**



public PropertyValue FUNC_IDENTNAMEPARTS {get; set;}

public:

property PropertyValue^ FUNC_IDENTNAMEPARTS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Outputs a single value for the DT that is structured in such a way that it can be separated into individual parts and the structure elements assigned, even when using block properties and when the "Edit DT in individual fields" property (ID 10090) is enabled. If there is no format for block properties and the "Edit DT in individual fields" property is not enabled, this property corresponds precisely to the "Name (identifying)" property (ID 20000); otherwise the property outputs the individual parts of the DT using separators.
