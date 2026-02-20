# FUNC_ARTICLE_FREQUENCY_SIGNAL_PROCESSING_SET Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1167.html

---

Function in rest position # 26349.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_FUNKTION_IN_RUHESTELLUNG( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_FUNKTION_IN_RUHESTELLUNG {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Information on the flow paths in the non-actuated state of a pneumatic directional control valve.
