# FUNC_CABLELENGTH Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_CABLELENGTH().html

---

Cable / Conduit: Length with unit # 20041.

Syntax

**C#**



public PropertyValue FUNC_CABLELENGTH {get; set;}

public:

property PropertyValue^ FUNC_CABLELENGTH {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Length of the cable or conduit with specification of the displayed measuring unit. If you do not enter a unit, the unit of length specified in the project settings is used.
