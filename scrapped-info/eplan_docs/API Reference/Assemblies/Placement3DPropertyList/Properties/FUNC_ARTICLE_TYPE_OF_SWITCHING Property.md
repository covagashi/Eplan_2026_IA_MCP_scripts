# FUNC_ARTICLE_TYPE_OF_SWITCHING Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_ARTICLE_TYPE_OF_SWITCHING(Int32).html

---

Circuit type # 26548.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_TYPE_OF_SWITCHING( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_TYPE_OF_SWITCHING {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

The way in which an electrical device or a component is connected in a circuit. Combination of the different switching possibilities of primary and secondary voltage windings. Example: Switching, cross-connection, etc.
