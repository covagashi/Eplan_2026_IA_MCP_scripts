# FUNC_ARTICLE_TERMINALSORTCODE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_ARTICLE_TERMINALSORTCODE(Int32).html

---

Sorting of part on terminal strip # 20104.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_TERMINALSORTCODE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_TERMINALSORTCODE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Sort code for the order of the alignable accessories on the terminal strip. The value is assigned in accordance with the order of the accessory parts in the dialog Edit terminal strip. Max. of 50 placements are evaluated and reported.

If you do not use main terminals, this property is displayed at the terminal strip definition ("Part reference data" category). By default the accessory is sorted to the beginning of the terminal strip.

If you use main terminals, this property is displayed at the main terminals and specifies the order of the alignable accessories relative to the associated main terminal. In this case the sort code can also have negative values.
