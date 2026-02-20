# ARTICLE_SUBCRAFT_GASTECHNOLOGY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1684.html

---

Subtrade 'Gas engineering' # 22266.

Syntax

**C#**



public MDPropertyValue ARTICLE_SUBCRAFT_GASTECHNOLOGY( 

   int index

) {get; set;}

public:

property MDPropertyValue^ ARTICLE_SUBCRAFT_GASTECHNOLOGY {

   MDPropertyValue^ get(int index);

   void set (int index, MDPropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 20.

This property can be used to create several subtrades for a trade.
