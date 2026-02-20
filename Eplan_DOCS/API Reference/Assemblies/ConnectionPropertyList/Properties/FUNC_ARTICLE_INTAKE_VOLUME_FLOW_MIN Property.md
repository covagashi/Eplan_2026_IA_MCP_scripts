# FUNC_ARTICLE_INTAKE_VOLUME_FLOW_MIN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_INTAKE_VOLUME_FLOW_MIN(Int32).html

---

Intake flow rate, min. # 26201.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_INTAKE_VOLUME_FLOW_MIN( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_INTAKE_VOLUME_FLOW_MIN {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Minimum flow rate within the working range of the conveyed gas at the outlet point of a fluid machine in relation to the conditions prevailing at the inlet point for the total temperature, the total pressure and the gas composition (e.g. humidity).
