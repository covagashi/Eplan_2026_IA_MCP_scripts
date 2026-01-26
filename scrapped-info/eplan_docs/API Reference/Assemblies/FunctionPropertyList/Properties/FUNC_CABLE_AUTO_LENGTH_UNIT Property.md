# FUNC_CABLE_AUTO_LENGTH_UNIT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_CABLE_AUTO_LENGTH_UNIT().html

---

Cable / Conduit: Length with unit of project # 20079.

Syntax

**C#**



public PropertyValue FUNC_CABLE_AUTO_LENGTH_UNIT {get; set;}

public:

property PropertyValue^ FUNC_CABLE_AUTO_LENGTH_UNIT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Length of the cable or conduit, including units, converted into the units defined in the project settings.
