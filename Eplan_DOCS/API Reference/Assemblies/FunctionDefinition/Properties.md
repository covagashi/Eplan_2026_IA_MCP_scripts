# Properties

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition_properties.html

---

For a list of all members of this type, see [FunctionDefinition members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition_members.html).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [BaseSymbol](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition~BaseSymbol.html) | Gets the best fitting SymbolVariant for this FunctionDefinition. This SymbolVariant can be used to insert SymbolReferences with not yet any SymbolVariant assigned onto pages. This is useful e.g. for InsertInteractions in GED |
| Public Property | [CategoryName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition~CategoryName.html) | Name of FunctionDefinition's Category. |
| Public Property | [CategoryRegion](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition~CategoryRegion.html) | Name of FunctionDefinition's region category. It is 'Area' level in function definitions tree. |
| Public Property | [ConnectionPoints](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition~ConnectionPoints.html) | Array of function definition's connection points. |
| Public Property | [CrossReferencedObjectsAll](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~CrossReferencedObjectsAll.html) | Returns an array of objects cross-referenced with this object (i.e. having the same name - in case of functions - or otherwise associated) (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [DatabaseIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~DatabaseIdentifier.html) | Returns the project as number. The number is unique for all open projects in one session. The number changes when the project is closed and opened again. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Description](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition~Description.html) | Get function definition description |
| Public Property | [FunctionCategory](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition~FunctionCategory.html) |  |
| Public Property | [FunctionDefinitionLibrary](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition~FunctionDefinitionLibrary.html) | Gets FunctionDefinitionLibrary. |
| Public Property | [Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition~Group.html) | Group of FunctionDefinition. |
| Public Property | [GroupName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition~GroupName.html) | Name of the FunctionDefinition's Group. |
| Public Property | [Id](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition~Id.html) | FunctionDefinition's ID. |
| Public Property | [Identifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition~Identifier.html) | Overloaded. Get identifier |
| Public Property | [Identifiers](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition~Identifiers.html) | Gets/sets all identifiers (i.e. for all available standards) |
| Public Property | [IsCPsCountVariable](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition~IsCPsCountVariable.html) | Returns whether the count of connection points is specified as variable. |
| Public Property | [IsLocked](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsLocked.html) | Determines if the the StorableObject is locked.  The StorableObject is locked when it was explicitly or implicitly locked. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsMainFunction](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition~IsMainFunction.html) | Gets flag which identifies a main function. |
| Public Property | [IsNetConnecting](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition~IsNetConnecting.html) | Get flag whether a function is net-connecting |
| Public Property | [IsReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsReadOnly.html) | Determines if StorableObject is read-only (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsSafetyRelevant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition~IsSafetyRelevant.html) | Get flag whether a function is a safety function |
| Public Property | [IsSignalSeparated](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition~IsSignalSeparated.html) | Get flag whether signal is separated |
| Public Property | [IsTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsTransient.html) | Determines if the the StorableObject is transient.  The StorableObject is transient when it was created by default constructor and:  it is a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) and it was not assigned a [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html),  it is a [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) or any class derived from it and was not assigned a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsValid](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsValid.html) | Determines if StorableObject is correct database object and is not deleted. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [MainGroup](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition~MainGroup.html) | Name of FunctionDefinition's main group. It is 'Trade' level in function definitions tree. |
| Public Property | [Name](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition~Name.html) | Name of the FunctionDefinition. |
| Public Property | [ObjectIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ObjectIdentifier.html) | Returns the object identifier as number. The number is unique for all objects of this type. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition~Project.html) | Overridden. Returns the project to which the StorableObject belongs. |
| Public Property | [Properties](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition~Properties.html) | .NET Property enabling access to P8 properties of the FunctionDefinition object. |
| Public Property | [TypeIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~TypeIdentifier.html) | Returns the type of the object as number. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |


