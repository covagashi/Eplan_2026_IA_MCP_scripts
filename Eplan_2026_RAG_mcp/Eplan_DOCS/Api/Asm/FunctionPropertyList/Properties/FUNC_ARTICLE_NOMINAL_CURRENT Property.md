# FUNC_ARTICLE_NOMINAL_CURRENT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_ARTICLE_NOMINAL_CURRENT(Int32).html

---

Nominal current # 26312.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_NOMINAL_CURRENT( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_NOMINAL_CURRENT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Nominal current of electrical consumers. Current that flows through an electric device when it is operated with the nominal voltage and emits its nominal power.
