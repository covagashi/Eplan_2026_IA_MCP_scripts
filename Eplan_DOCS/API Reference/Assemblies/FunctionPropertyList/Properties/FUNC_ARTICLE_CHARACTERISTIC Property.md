# FUNC_ARTICLE_CHARACTERISTIC Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_ARTICLE_CHARACTERISTIC(Int32).html

---

Characteristic curve # 26404.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_CHARACTERISTIC( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_CHARACTERISTIC {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Graphical representation of the relationship between two or more physical quantities of a product or item. Example: For a diode, the I-U characteristic curve shows the relation between the current (I) and the voltage (U) at the diode.
