# FUNC_PLCNO_TARGETSEARCH_FOR_AUTOSYMBOLICADDRESS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCNO_TARGETSEARCH_FOR_AUTOSYMBOLICADDRESS().html

---

Without sensor / actuator search for symbolic address # 20196.

Syntax

**C#**



public PropertyValue FUNC_PLCNO_TARGETSEARCH_FOR_AUTOSYMBOLICADDRESS {get; set;}

public:

property PropertyValue^ FUNC_PLCNO_TARGETSEARCH_FOR_AUTOSYMBOLICADDRESS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

If this property is enabled, no sensor/actuator search is carried out when establishing the "Symbolic address (automatic)" for an I/O connection point. Instead, the address is output when the "Use address if search for symbolic address is unsuccessful" project setting is enabled.
