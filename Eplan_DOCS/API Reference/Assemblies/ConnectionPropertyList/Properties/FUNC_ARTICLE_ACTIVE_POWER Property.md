# FUNC_ARTICLE_ACTIVE_POWER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ACTIVE_POWER(Int32).html

---

Active power # 26642.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_ACTIVE_POWER( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_ACTIVE_POWER {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Electrical power in watt (W), which is actually converted into other forms of energy such as mechanical, thermal or chemical energy. The active power is a measure of how efficiently the electric energy is used.
