# UserDefinedPropertyDefinition

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UserDefinedPropertyDefinition.html

---

This class provides information about user-defined properties and makes it possible to create them.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.PropertyDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition.html)  
      **Eplan.EplApi.DataModel.UserDefinedPropertyDefinition**

Syntax

**C#**



public class UserDefinedPropertyDefinition : PropertyDefinition

public ref class UserDefinedPropertyDefinition : public PropertyDefinition


Remarks

After creating a new UserDefinedPropertyDefinition, you assign it to a property list by the UniversalPropertyList.AddUserPropertyDef(oUserDefinedPropertyDefinition) method

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [UserDefinedPropertyDefinition Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UserDefinedPropertyDefinition~_ctor().html) | Default constructor. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Category](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UserDefinedPropertyDefinition~Category.html) | Category of this property definition. |
| Public Property | [DefaultValuesSelectionList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UserDefinedPropertyDefinition~DefaultValuesSelectionList.html) | Gets/Sets list of default values for selection list. |
| Public Property | [DisplayedName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UserDefinedPropertyDefinition~DisplayedName.html) | Name displayed in GUI for this property definition. |
| Public Property | [DoNotUse](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UserDefinedPropertyDefinition~DoNotUse.html) | Gets/Sets a flag which indicates if property will not be longer displayed in project. |
| Public Property | [GUIReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UserDefinedPropertyDefinition~GUIReadOnly.html) | Gets/Sets a flag which indicates if property is read only in GUI in the project. |
| Public Property | [Id](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UserDefinedPropertyDefinition~Id.html) | Overridden. Returns AnyPropertyId. |
| Public Property | [IdentifyingName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UserDefinedPropertyDefinition~IdentifyingName.html) | Identifying name of this property definition. |
| Public Property | [InputAid](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UserDefinedPropertyDefinition~InputAid.html) | Input aid of this property definition. |
| Public Property | [IsAssigned](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UserDefinedPropertyDefinition~IsAssigned.html) | Returns true, if the property is assigned to at least one property list |
| Public Property | [IsDeprecated](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UserDefinedPropertyDefinition~IsDeprecated.html) | Overridden. Allows to check if a given property is marked as deprecated. |
| Public Property | [IsIndexed](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~IsIndexed.html) | Allows to check if a given property is indexed. (Inherited from [Eplan.EplApi.DataModel.PropertyDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition.html)) |
| Public Property | [IsInternal](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~IsInternal.html) | Allows to check if a given property is marked as internal. Don't use this property. (Inherited from [Eplan.EplApi.DataModel.PropertyDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition.html)) |
| Public Property | [IsNamePart](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~IsNamePart.html) | Allows to check if a given property is name part. (Inherited from [Eplan.EplApi.DataModel.PropertyDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition.html)) |
| Public Property | [IsPropertyLicensed](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~IsPropertyLicensed.html) | Allows to check if a given property is licensed. (Inherited from [Eplan.EplApi.DataModel.PropertyDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition.html)) |
| Public Property | [IsReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~IsReadOnly.html) | Allows to check if a given property is read-only. (Inherited from [Eplan.EplApi.DataModel.PropertyDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition.html)) |
| Public Property | [LowerBound](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~LowerBound.html) | Returns the minimum value of a property specified in the property definition. (Inherited from [Eplan.EplApi.DataModel.PropertyDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition.html)) |
| Public Property | [MaxIndex](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~MaxIndex.html) | Allows to check the maximum index of a given property. (Inherited from [Eplan.EplApi.DataModel.PropertyDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition.html)) |
| Public Property | [Name](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~Name.html) | Name of property. (Inherited from [Eplan.EplApi.DataModel.PropertyDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition.html)) |
| Public Property | [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UserDefinedPropertyDefinition~Project.html) | Returns the project in which this property definition exists. |
| Public Property | [Type](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~Type.html) | Returns information about the type of the property. (Inherited from [Eplan.EplApi.DataModel.PropertyDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition.html)) |
| Public Property | [UnitGroup](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UserDefinedPropertyDefinition~UnitGroup.html) | UnitGroup of this property definition. |
| Public Property | [UpperBound](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~UpperBound.html) | Returns the maximum value of a property specified in the property definition. (Inherited from [Eplan.EplApi.DataModel.PropertyDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition.html)) |
| Public Property | [Usages](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UserDefinedPropertyDefinition~Usages.html) | Usages of this property definition. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Methodstatic (Shared in Visual Basic) | [Create](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UserDefinedPropertyDefinition~Create.html) | Overloaded. Creates new property definition. |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~Dispose().html) | Destructor for deterministic finalization of UserDefinedPropertyDefinition object. (Inherited from [Eplan.EplApi.DataModel.PropertyDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition.html)) |
| Public Method | [ValidateValue](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~ValidateValue.html) | Returns the display string used for a given property value. Validates whether the value meets the requirements of the property definition. (Inherited from [Eplan.EplApi.DataModel.PropertyDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition.html)) |


