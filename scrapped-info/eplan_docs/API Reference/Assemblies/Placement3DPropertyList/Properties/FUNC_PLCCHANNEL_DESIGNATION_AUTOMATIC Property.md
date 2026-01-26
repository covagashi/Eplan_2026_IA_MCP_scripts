# FUNC_PLCCHANNEL_DESIGNATION_AUTOMATIC Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLCCHANNEL_DESIGNATION_AUTOMATIC().html

---

Channel designation (automatic) # 20428.

Syntax

**C#**



public PropertyValue FUNC_PLCCHANNEL_DESIGNATION_AUTOMATIC {get; set;}

public:

property PropertyValue^ FUNC_PLCCHANNEL_DESIGNATION_AUTOMATIC {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Channel designation of a PLC power supply connection point. Shows either the contents of the manually entered channel designation or the contents of the channel determined by a related I/O connection point.
