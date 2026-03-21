# ARTICLEREF_AML_GUID Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~ARTICLEREF_AML_GUID().html

---

AutomationML GUID (accessories) # 40348.

Syntax

**C#**



public PropertyValue ARTICLEREF_AML_GUID {get; set;}

public:

property PropertyValue^ ARTICLEREF_AML_GUID {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

In this property the GUIDs for accessory parts are stored in AutomationML AR APC format during the PLC data exchange. All parts that are entered at the positions 2 to 50 on the Parts tab in the property dialog of a main function are considered to be accessories. The GUID is generated automatically and should normally not be modified manually.
