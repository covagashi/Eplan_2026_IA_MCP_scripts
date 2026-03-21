# FUNC_ARTICLE_EFFICIENCY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_ARTICLE_EFFICIENCY(Int32).html

---

Efficiency # 26650.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_EFFICIENCY( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_EFFICIENCY {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Ratio of the usable energy to the supplied energy of a system or device. The efficiency is usually expressed as a percentage and shows how efficiently a device or machine works.
