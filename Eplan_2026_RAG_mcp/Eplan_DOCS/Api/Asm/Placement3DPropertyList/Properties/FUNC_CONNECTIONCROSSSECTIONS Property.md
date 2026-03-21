# FUNC_CONNECTIONCROSSSECTIONS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_CONNECTIONCROSSSECTIONS(Int32).html

---

Connection point cross-section / diameter # 20295.

Syntax

**C#**



public PropertyValue FUNC_CONNECTIONCROSSSECTIONS( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_CONNECTIONCROSSSECTIONS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Shows the connection point cross-sections / diameters of the function. The index can be used to define a max. of 100 sets of connection point cross-sections / diameters.
