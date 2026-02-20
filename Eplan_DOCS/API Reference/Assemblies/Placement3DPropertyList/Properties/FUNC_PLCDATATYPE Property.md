# FUNC_PLCDATATYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLCDATATYPE().html

---

Data type # 20405.

Syntax

**C#**



public PropertyValue FUNC_PLCDATATYPE {get; set;}

public:

property PropertyValue^ FUNC_PLCDATATYPE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Data type of a PLC connection point. Meaningful entries are, for example, BOOL, BYTE, WORD, DWORD, LWORD. The data type depends on the PLC type.
