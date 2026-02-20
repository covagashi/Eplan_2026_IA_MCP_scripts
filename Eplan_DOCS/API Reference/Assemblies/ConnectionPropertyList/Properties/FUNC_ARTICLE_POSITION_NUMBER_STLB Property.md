# FUNC_ARTICLE_POSITION_NUMBER_STLB Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_POSITION_NUMBER_STLB(Int32).html

---

Performance description, standardized: Item number (device, utility, service) # 26533.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_POSITION_NUMBER_STLB( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_POSITION_NUMBER_STLB {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Unique identification number for a specific service item in the bill of quantities. Example: A specific number stands for the service "Concrete works: Concrete a foundation".
