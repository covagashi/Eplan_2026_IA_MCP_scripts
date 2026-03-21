# LOCATION_DESCRIPTION_SUPPLEMENTARYFIELD Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList~LOCATION_DESCRIPTION_SUPPLEMENTARYFIELD(Int32).html

---

Structure description Supplementary field # 1009.

Syntax

**C#**



public PropertyValue LOCATION_DESCRIPTION_SUPPLEMENTARYFIELD( 

   int index

) {get; set;}

public:

property PropertyValue^ LOCATION_DESCRIPTION_SUPPLEMENTARYFIELD {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 10.

Describing supplementary text for the structure identifier, displayed in structure identifier management.
