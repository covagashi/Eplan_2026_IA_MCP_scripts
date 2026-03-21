# FUNC_ARTICLE_CABLE_PIPE_TRANSMITTER_CONNECTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic430.html

---

Measuring transducer: Line connection (cable / pipe) # 26203.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_CABLE_PIPE_TRANSMITTER_CONNECTION( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_CABLE_PIPE_TRANSMITTER_CONNECTION {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

The way in which a measuring transducer is connected to cables or pipes (e.g., "plugged" or "cast" for a pressure measuring transducer during a submersion / well measurement).
