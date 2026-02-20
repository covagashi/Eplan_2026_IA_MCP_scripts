# DMPLAOBJECT_SAFETY_RELEVANT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~DMPLAOBJECT_SAFETY_RELEVANT().html

---

Relevant to safety # 44060.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_SAFETY_RELEVANT {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_SAFETY_RELEVANT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

The property can be displayed in the P&I diagram at the placed measuring points or consumers and serves to represent PCT tasks in accordance with the standard DIN EN 62424. This property is additionally available at planning objects and containers. On the basis of the symbols displayed in the graphical editor you can recognize whether a placed measuring point or consumer is relevant to safety, or GMP- or quality-relevant. The property can be output in the reports, during the manufacturing data export and it can also be output in the block properties for the planning objects. In the navigators for pre-planning you can use the property as a filter criterion or display it in the list view as a column.
