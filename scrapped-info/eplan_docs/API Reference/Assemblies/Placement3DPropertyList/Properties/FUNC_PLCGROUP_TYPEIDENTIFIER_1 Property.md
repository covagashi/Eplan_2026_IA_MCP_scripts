# FUNC_PLCGROUP_TYPEIDENTIFIER_1 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLCGROUP_TYPEIDENTIFIER_1().html

---

PLC subdevice 1: PLC type designation # 20607.

Syntax

**C#**



public PropertyValue FUNC_PLCGROUP_TYPEIDENTIFIER_1 {get; set;}

public:

property PropertyValue^ FUNC_PLCGROUP_TYPEIDENTIFIER_1 {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

PLC type designation for a PLC subdevice 1 of a PLC card. If a PLC type designation is entered at the main device as well, the device identification for PLC subdevices that are treated as independent devices in the PLC configuration program is effected by means of this property. The entry has to be carried out in exactly the same notation as in the hardware catalog of the manufacturer.
