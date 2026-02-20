# PropertyDefinition

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition.html

---

This class provides information about properties.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.DataModel.PropertyDefinition**  
      [Eplan.EplApi.DataModel.UserDefinedPropertyDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UserDefinedPropertyDefinition.html)

Syntax

**C#**



public class PropertyDefinition

public ref class PropertyDefinition

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [PropertyDefinition Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~_ctor(AnyPropertyId).html) | Constructor |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Id](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~Id.html) | Returns AnyPropertyId. |
| Public Property | [IsDeprecated](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~IsDeprecated.html) | Allows to check if a given property is marked as deprecated. |
| Public Property | [IsIndexed](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~IsIndexed.html) | Allows to check if a given property is indexed. |
| Public Property | [IsInternal](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~IsInternal.html) | Allows to check if a given property is marked as internal. Don't use this property. |
| Public Property | [IsNamePart](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~IsNamePart.html) | Allows to check if a given property is name part. |
| Public Property | [IsPropertyLicensed](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~IsPropertyLicensed.html) | Allows to check if a given property is licensed. |
| Public Property | [IsReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~IsReadOnly.html) | Allows to check if a given property is read-only. |
| Public Property | [LowerBound](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~LowerBound.html) | Returns the minimum value of a property specified in the property definition. |
| Public Property | [MaxIndex](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~MaxIndex.html) | Allows to check the maximum index of a given property. |
| Public Property | [Name](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~Name.html) | Name of property. |
| Public Property | [Type](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~Type.html) | Returns information about the type of the property. |
| Public Property | [UpperBound](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~UpperBound.html) | Returns the maximum value of a property specified in the property definition. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~Dispose().html) | Destructor for deterministic finalization of PropertyDefinition object. |
| Public Method | [ValidateValue](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~ValidateValue.html) | Returns the display string used for a given property value. Validates whether the value meets the requirements of the property definition. |


