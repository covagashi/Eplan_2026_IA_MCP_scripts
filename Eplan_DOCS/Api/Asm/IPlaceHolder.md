# IPlaceHolder

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder.html

---

TODO

Syntax

**C#**



public interface IPlaceHolder

public interface class IPlaceHolder

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [AssignedObjects](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~AssignedObjects.html) | Gets/Sets a list of StorableObject references to a PlaceHolder object. The originally assigned references are replaced. |
| Property | [IsDocumentReferenceActive](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~IsDocumentReferenceActive.html) | Activates the properties of the page/installation space for the place holder object. |
| Property | [Name](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~Name.html) | Gets/Sets the name of the Placeholder3D. |
| Property | [NameOfRecord](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~NameOfRecord.html) | Gets/Sets the name of a record, specified by its index. |
| Property | [NumberOfRecords](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~NumberOfRecords.html) | Count of records. |
| Property | [NumberOfReferences](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~NumberOfReferences.html) | Count of objects referenced by the Placeholder3D. |
| Property | [NumberOfVariables](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~NumberOfVariables.html) | Count of Variables. |
| Property | [Value](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~Value.html) | Gets/Sets the value of a variable for a record. |
| Property | [VariableNames](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~VariableNames.html) | Names of all variables in the Placeholder3D. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AddRecord](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~AddRecord.html) | Adds a new record with the specified name to the Placeholder3D object. |
| Method | [AddVariable](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~AddVariable.html) | Adds a new variable to the Placeholder3D object. |
| Method | [ApplyRecord](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~ApplyRecord.html) | Overloaded. Applies a record of values on a PlaceHolder object. |
| Method | [DeleteRecord](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~DeleteRecord.html) | Overloaded. Deletes a record. |
| Method | [DeleteUnusedVariables](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~DeleteUnusedVariables.html) | Deletes all unused variables. |
| Method | [DeleteVariable](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~DeleteVariable.html) | Deletes a variable. |
| Method | [FindRecord](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~FindRecord.html) | Finds a record by name. |
| Method | [FindVariable](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~FindVariable.html) | Finds a variable, specified by its name. |
| Method | [GetAllCurrentValues](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~GetAllCurrentValues.html) | Gets a list of all current values in Placeholder. |
| Method | [GetCurrentValue](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~GetCurrentValue.html) | Gets current value for given object, property and index. |
| Method | [GetProjectPropertyEntry](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~GetProjectPropertyEntry.html) | Gets a value or variable of Placeholder project property. |
| Method | [GetRecordNames](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~GetRecordNames.html) | \Returns the names of all records in the nIndex-th PlaceHolder of a Macro. |
| Method | [GetValue](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~GetValue.html) | Gets the value of a variable for a record. |
| Method | [GetValues](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~GetValues.html) | \Returns the values of all variables in the nIndex-th PlaceHolder of a Macro variant for a given record. |
| Method | [GetVariableNames](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~GetVariableNames.html) | \Returns the names of all variables in the nIndex-th PlaceHolder of a Macro variant. |
| Method | [IsVariableValid](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~IsVariableValid.html) | Verifies the correctness if a variable name of a placeholder. If a variable name contains invalid characters, this method \returns false. |
| Method | [RemoveInvalidObjectReferences](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~RemoveInvalidObjectReferences.html) | Removes invalid (e.g. deleted) object references from a PlaceHolder. |
| Method | [RemoveObjectReferences](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~RemoveObjectReferences.html) | Removes object references from a PlaceHolder. |
| Method | [SetProjectPropertyEntry](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~SetProjectPropertyEntry.html) | Sets a value or variable on Placeholder project property. The reference of the object will be added to the Placeholder if necessary. |
| Method | [SetValue](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~SetValue.html) | Sets the value of a variable for a record. |


