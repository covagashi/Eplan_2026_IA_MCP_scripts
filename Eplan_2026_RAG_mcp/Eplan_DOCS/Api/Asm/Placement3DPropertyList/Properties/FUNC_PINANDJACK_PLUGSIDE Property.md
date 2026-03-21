# FUNC_PINANDJACK_PLUGSIDE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PINANDJACK_PLUGSIDE().html

---

Plugs: Assignment to male pin / female pin end # 20052.

Syntax

**C#**



public PropertyValue FUNC_PINANDJACK_PLUGSIDE {get; set;}

public:

property PropertyValue^ FUNC_PINANDJACK_PLUGSIDE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

In the case of the separate management of male and female pins, this specifies whether the pin is assigned to the male or female pin end of the plug.

0 = Automatic (i.e. the assignment is made via the DT and the function definition)

1 = Male pin end

2 = Female pin end.
