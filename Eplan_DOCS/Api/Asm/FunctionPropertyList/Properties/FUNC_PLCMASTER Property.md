# FUNC_PLCMASTER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCMASTER().html

---

Logical network: Name # 20414.

Syntax

**C#**



public PropertyValue FUNC_PLCMASTER {get; set;}

public:

property PropertyValue^ FUNC_PLCMASTER {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Name of the logical network to which the bus port belongs. This entry has to be unique within a physical network.
