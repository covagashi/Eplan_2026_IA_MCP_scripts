# Methods

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedFunction_methods.html

---

For a list of all members of this type, see [MergedFunction members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedFunction_members.html).

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Create](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedFunction~Create.html) | Overloaded. Initializes the MergedFunction object to cover the functions passed in the array parameter. If the functions cannot be merged together into one merged function an exception is thrown. Functions, generally, cannot be merged together if they belong to different devices or they are of different categories. To be merged, they have to represent the same functional part of the device. |
| Public Methodstatic (Shared in Visual Basic) | [CreateMergedFunctions](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedFunction~CreateMergedFunctions.html) | Returns an array of MergedFunction objects created from the functions passed in the array parameter. Functions that belong to the same device and represent one functional part of the device are merged together into one merged function in the output vector. |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Dispose().html) | Destructor (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Equals.html) | Operator of comparison implementation. Checks if two StorableObjects refer to the same object in the project. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetHashCode.html) | Serves as the default hash function. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetMainPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedFunction~GetMainPlacement.html) | Returns main placement this MergedFunction by parameters. |
| Public Method | [GetMergedProperty](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedFunction~GetMergedProperty.html) | Returns value of merged property having given property id. |
| Public Method | [GetTypeName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetTypeName.html) | Returns object type name. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [IsCovered](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedFunction~IsCovered.html) | Returns if the objects is a function or a connection covered by this merged function. |
| Public Method | [LockObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~LockObject().html) | Tries to lock current object in database for exclusive access. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [SmartLock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~SmartLock.html) | Tries to lock current object. If object is [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) - it's page will be locked as well; [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) locks it's installation space; [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) locks all it's connections and connection definition points; [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) locks all placements from this page. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [ToStringIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ToStringIdentifier.html) | Returns this object as string identifier. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |


