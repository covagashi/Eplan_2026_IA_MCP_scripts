# FUNC_DEVICETAG_FULL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_DEVICETAG_FULL().html

---

DT (full, without project structures) # 20009.

Syntax

**C#**



public PropertyValue FUNC_DEVICETAG_FULL {get; set;}

public:

property PropertyValue^ FUNC_DEVICETAG_FULL {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Provides the device tag without the project structures, i.e., the following is output:

The result is "K1" for "=A1-K1," "K1" for "-K1" and "K1-K2" for "=A1-K1-K2".
