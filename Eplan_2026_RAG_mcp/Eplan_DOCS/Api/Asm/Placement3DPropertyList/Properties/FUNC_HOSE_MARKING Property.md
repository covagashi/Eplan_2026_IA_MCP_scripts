# FUNC_HOSE_MARKING Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_HOSE_MARKING().html

---

Hose line identification # 20867.

Syntax

**C#**



public PropertyValue FUNC_HOSE_MARKING {get; set;}

public:

property PropertyValue^ FUNC_HOSE_MARKING {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The hose line identification in Eplan fulfills the specifications of the hose line standard DIN 20066 and is made up of the values of the following data:

Abbreviation of the manufacturer

Value of the working pressure + Unit of the pressure indication

Year + Month of manufacturing
