# PROJ_ARTICLEREF_CRAFT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ARTICLEREF_CRAFT(Int32).html

---

Trade of part reference # 20913.

Syntax

**C#**



public PropertyValue PROJ_ARTICLEREF_CRAFT( 

   int index

) {get; set;}

public:

property PropertyValue^ PROJ_ARTICLEREF_CRAFT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Trade of the associated part reference. A max. of 50 definitions can be defined using the index.
