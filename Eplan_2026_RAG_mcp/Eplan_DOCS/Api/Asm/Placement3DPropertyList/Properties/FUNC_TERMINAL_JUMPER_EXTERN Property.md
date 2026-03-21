# FUNC_TERMINAL_JUMPER_EXTERN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_TERMINAL_JUMPER_EXTERN(Int32).html

---

Manual saddle jumpers (external) # 20351.

Syntax

**C#**



public PropertyValue FUNC_TERMINAL_JUMPER_EXTERN( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_TERMINAL_JUMPER_EXTERN {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1.

The property is stored at the terminal that represents the jumper beginning of a manual saddle jumper between external saddle jumper connection points. The "jumper crest" is defined in this property. To this purpose the increment to the next jumpered terminals is specified as well as the increment to the associated level starting from the jumper start.

Example: The value "2/0;1/-1" means that a saddle jumper exists to the terminal two away on the same level and from there to the next terminal one level lower.
