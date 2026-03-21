# FUNC_TERMINAL_JUMPER_INTERN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_TERMINAL_JUMPER_INTERN(Int32).html

---

Manual saddle jumpers (internal) # 20350.

Syntax

**C#**



public PropertyValue FUNC_TERMINAL_JUMPER_INTERN( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_TERMINAL_JUMPER_INTERN {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1.

The property is stored at the terminal that represents the jumper beginning of a manual saddle jumper between internal saddle jumper connection points. The "jumper crest" is defined in this property. To this purpose the increment to the next jumpered terminals is specified as well as the increment to the associated level starting from the jumper start.

Example: The value "2/0;1/-1" means that a saddle jumper exists to the terminal two away on the same level and from there to the next terminal one level lower.
