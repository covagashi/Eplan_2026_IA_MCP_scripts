# PLCIOENTRY_DIRECTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlcIOPropertyList~PLCIOENTRY_DIRECTION().html

---

Direction # 23403.

Syntax

**C#**



public PropertyValue PLCIOENTRY_DIRECTION {get; set;}

public:

property PropertyValue^ PLCIOENTRY_DIRECTION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

PLC connection points can be inputs or outputs. Input and output addresses can be recognized by the direction (input, output, undefined).
