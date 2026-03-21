# FUNC_MOUNTINGPLATE_FORMEVALUATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_MOUNTINGPLATE_FORMEVALUATION().html

---

Suppress generation of the enclosure legend # 20441.

Syntax

**C#**



public PropertyValue FUNC_MOUNTINGPLATE_FORMEVALUATION {get; set;}

public:

property PropertyValue^ FUNC_MOUNTINGPLATE_FORMEVALUATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Suppresses the generation of an enclosure legend for the model view. The model view is also not taken into consideration during the output of the labeling for the report type "Enclosure legend".
