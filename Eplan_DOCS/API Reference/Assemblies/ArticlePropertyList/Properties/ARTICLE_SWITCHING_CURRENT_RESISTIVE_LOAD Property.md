# ARTICLE_SWITCHING_CURRENT_RESISTIVE_LOAD Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SWITCHING_CURRENT_RESISTIVE_LOAD().html

---

Switching current (resistive load) # 26138.

Syntax

**C#**



public PropertyValue ARTICLE_SWITCHING_CURRENT_RESISTIVE_LOAD {get; set;}

public:

property PropertyValue^ ARTICLE_SWITCHING_CURRENT_RESISTIVE_LOAD {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Maximum current for which an electrical device is designed and which a switch or relay can reliably switch if the load is purely resistive, i.e. has no inductive or capacitive component. Example: A relay has a switching current capacity of 10 amperes at 250 volts AC for ohmic loads. This means that the relay can safely switch 10 amperes at a voltage of 250 volts AC if the load is purely resistive.
