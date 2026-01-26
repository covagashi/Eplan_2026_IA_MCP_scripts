# FUNC_CIRCUITNUMBER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_CIRCUITNUMBER().html

---

Circuit number # 20317.

Syntax

**C#**



public PropertyValue FUNC_CIRCUITNUMBER {get; set;}

public:

property PropertyValue^ FUNC_CIRCUITNUMBER {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

This property is used to map the designations used in the standard DIN ISO 1219-2 for fluid power in Eplan. For fluid power devices the counter of the device is displayed here, meaning the contents of the property DT: Counter (ID 20014).

This property is used as part of a name. In order to set it, member `NameParts` must be used on object which name will be changed. Additionally for setting this property on a Page object, a function Page::SetName() or the Page constructor can be used.
