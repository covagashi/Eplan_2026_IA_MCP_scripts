# Methods

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.FunctionDefinitionLibrary_methods.html

---

For a list of all members of this type, see [FunctionDefinitionLibrary members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.FunctionDefinitionLibrary_members.html).

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Close](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.FunctionDefinitionLibrary~Close.html) | For internal use. Closes the library. Note: Should be used only if this object was initialized with Initialize() method and that method returned TRUE. |
| Public Method | [Dispose](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Dispose().html) | Destructor for deterministic finalization of StorableObject object. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Equals.html) | Operator of comparison implementation. Checks if two StorableObjects refer to the same object in the project. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetEnumerator](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.FunctionDefinitionLibrary~GetEnumerator.html) | Returns an enumerator that iterates through the function definitions of this library. |
| Public Method | [GetEnumerator2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.FunctionDefinitionLibrary~GetEnumerator2.html) | Returns an enumerator that iterates through the function definitions of this library. |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetHashCode.html) | Serves as the default hash function. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetTypeName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetTypeName.html) | Returns object type name. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Initialize](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.FunctionDefinitionLibrary~Initialize.html) | Overloaded. For internal use. Opens the standard function definition library from system masterdata. Note: if this method returns true, it means that the library was actually open during the initialization and it is the client responsibility to close it. |
| Public Method | [LockObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~LockObject().html) | Tries to lock current object in database for exclusive access. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [SmartLock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~SmartLock.html) | Tries to lock current object. If object is [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) - it's page will be locked as well; [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) locks it's installation space; [Eplan.EplApi.DataModel.Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) locks all it's connections and connection definition points; [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) locks all placements from this page. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [ToStringIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ToStringIdentifier.html) | Returns this object as string identifier. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |


