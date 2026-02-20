# PROJ_ARTICLEREF_SUBCRAFT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~PROJ_ARTICLEREF_SUBCRAFT(Int32).html

---

Subtrade of part reference # 20914.

Syntax

**C#**



public PropertyValue PROJ_ARTICLEREF_SUBCRAFT( 

   int index

) {get; set;}

public:

property PropertyValue^ PROJ_ARTICLEREF_SUBCRAFT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Subtrade of the associated part reference. A max. of 50 definitions can be defined using the index.
