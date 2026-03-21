# FUNC_HOSE_CREATEDATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_HOSE_CREATEDATE().html

---

Manufacturing date # 20868.

Syntax

**C#**



public PropertyValue FUNC_HOSE_CREATEDATE {get; set;}

public:

property PropertyValue^ FUNC_HOSE_CREATEDATE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.DateTime.

Remarks

Manufacturing date (Year + Month), is used in the hose line identification. The time is output in the local time of the user in accordance with the set time zone.
