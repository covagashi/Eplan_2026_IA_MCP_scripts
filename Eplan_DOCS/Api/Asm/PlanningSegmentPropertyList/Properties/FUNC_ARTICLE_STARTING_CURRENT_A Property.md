# FUNC_ARTICLE_STARTING_CURRENT_A Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1032.html

---

Storage, transport and packaging (requirement) # 26410.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_STORAGE_TRANSPORT_AND_PACKAGING_REQUIREMENT( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_STORAGE_TRANSPORT_AND_PACKAGING_REQUIREMENT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Requirements for logistic processes.
