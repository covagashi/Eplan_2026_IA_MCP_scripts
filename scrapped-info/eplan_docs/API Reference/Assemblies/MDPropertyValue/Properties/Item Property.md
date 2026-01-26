# Item Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Item.html

---

Returns [MDPropertyValue](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue.html) object at specified index.

Syntax

**C#**



public MDPropertyValue this[ 

   int index

]; {get; set;}

public:

property MDPropertyValue^ default [int] {

   MDPropertyValue^ get(int index);

   void set (int index, MDPropertyValue^ value);

}


#### Parameters

*index*

Exceptions

| Exception | Description |
| --- | --- |
| [MDInvalidIndexException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDInvalidIndexException.html) | MDInvalidIndexException |
| [MDNotIndexedPropertyException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDNotIndexedPropertyException.html) | MDNotIndexedPropertyException |
| [MDIndexedPropertyException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDIndexedPropertyException.html) | MDIndexedPropertyException |
| [System.InvalidOperationException](#) | Thrown when setter is used on offline property. |

Example

**C#**

```
MDPropertyValue oProperty = m_MDPartsDatabase.Parts[0].Properties[Eplan.EplApi.MasterData.Properties.MDPartsDatabaseItem.ARTICLE_HEIGHT];

if (oProperty.Definition.IsIndexed && oProperty.Definition.MaxIndex > 2)

{                    

	MDPropertyValue oPv = oProperty[1]; // now oPv points to first index of property FUNC_INDEXED_PROPERTY

	string str = oPv.ToString();

	if (oProperty.Definition.MaxIndex < 100)

	{

		string str1 = oProperty[100]; // throws MDInvalidIndexException exception

		string str2 = oProperty[0]; // also throws MDInvalidIndexException exception

	}

	string str3 = oProperty; // throws MDInvalidIndexException exception, because valid index was not specified

}
```
