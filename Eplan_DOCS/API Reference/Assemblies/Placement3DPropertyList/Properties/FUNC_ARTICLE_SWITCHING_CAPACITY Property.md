# FUNC_ARTICLE_SWITCHING_CAPACITY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_ARTICLE_SWITCHING_CAPACITY(Int32).html

---

Switching capacity # 26546.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_SWITCHING_CAPACITY( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_SWITCHING_CAPACITY {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Maximum electrical load that a switching device can switch reliably without damage or malfunctions occurring. Example: A switch has a switching capacity of 10 amperes at 250 volts AC. This means that the switch can reliably switch a current of up to 10 amperes at a voltage of 250 volts AC.
