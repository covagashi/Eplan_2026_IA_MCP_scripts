# FUNC_PLC_MASTERSYSTEMID Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLC_MASTERSYSTEMID().html

---

MasterSystemID # 20334.

Syntax

**C#**



public PropertyValue FUNC_PLC_MASTERSYSTEMID {get; set;}

public:

property PropertyValue^ FUNC_PLC_MASTERSYSTEMID {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The MasterSystemID is an identification number (network number) for interface assignment during the PLC data exchange with Siemens SIMATIC STEP 7. PROFIBUS DP networks have numerical values from 1 to 99, PROFINET IO networks have numerical values as of 100.
