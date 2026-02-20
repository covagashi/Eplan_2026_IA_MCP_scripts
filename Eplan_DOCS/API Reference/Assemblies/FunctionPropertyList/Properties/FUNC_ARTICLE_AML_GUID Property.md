# FUNC_ARTICLE_AML_GUID Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_ARTICLE_AML_GUID(Int32).html

---

AutomationML GUID (accessories) # 20399.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_AML_GUID( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_AML_GUID {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

In this property the GUIDs for accessory parts are stored in AutomationML AR APC format during the PLC data exchange. All parts that are entered at the positions 2 to 50 on the Parts tab in the property dialog of a main function are considered to be accessories. The GUID is generated automatically and should normally not be modified manually.
