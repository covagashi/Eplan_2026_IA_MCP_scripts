# LOCATION_UPPERLOCATION_DESCRIPTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList~LOCATION_UPPERLOCATION_DESCRIPTION(Int32).html

---

Structure identifier superior: Description # 1012.

Syntax

**C#**



public PropertyValue LOCATION_UPPERLOCATION_DESCRIPTION( 

   int index

) {get; set;}

public:

property PropertyValue^ LOCATION_UPPERLOCATION_DESCRIPTION {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 10.
