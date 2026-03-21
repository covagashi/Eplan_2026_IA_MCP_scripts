# ARTICLE_SWITCHING_CAPACITY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~ARTICLE_SWITCHING_CAPACITY().html

---

Switching capacity # 26545.

Syntax

**C#**



public PropertyValue ARTICLE_SWITCHING_CAPACITY {get; set;}

public:

property PropertyValue^ ARTICLE_SWITCHING_CAPACITY {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Maximum electrical load that a switching device can switch reliably without damage or malfunctions occurring. Example: A switch has a switching capacity of 10 amperes at 250 volts AC. This means that the switch can reliably switch a current of up to 10 amperes at a voltage of 250 volts AC.
