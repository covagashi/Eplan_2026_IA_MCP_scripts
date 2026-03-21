# PROJ_BLOCKPROPERTY_REPLACETEXT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKPROPERTY_REPLACETEXT(Int32).html

---

Block property: Replacement text # 10660.

Syntax

**C#**



public PropertyValue PROJ_BLOCKPROPERTY_REPLACETEXT( 

   int index

) {get; set;}

public:

property PropertyValue^ PROJ_BLOCKPROPERTY_REPLACETEXT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 100.

Using this project property, you can define up to 100 tables for replacement texts (via the index). You can use these tables to replace the values of block properties: When editing block properties you can use the dialog Format: Block property to select the table with the replacement texts to be used for a property. The values of the selected property are then compared to the texts defined in the table and replaced accordingly.
