# CONNECTION_PLANT_AUTOMATIC Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_PLANT_AUTOMATIC().html

---

Function designation: Main identifier (automatic) # 31102.

Syntax

**C#**



public PropertyValue CONNECTION_PLANT_AUTOMATIC {get; set;}

public:

property PropertyValue^ CONNECTION_PLANT_AUTOMATIC {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

If a DT is entered on the connection, the corresponding structure identifier is output. Otherwise, the structure identifier from the connection source is output. The source is determined by its position in the schematic and can be exchanged with the target over a connection definition point.
