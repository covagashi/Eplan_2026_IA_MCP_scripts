# Methods

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D_methods.html

---

For a list of all members of this type, see [Placement3D members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D_members.html).

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddConnectionPointPosition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~AddConnectionPointPosition.html) | Creates new connection point position. |
| Public Method | [AddMatePersistent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~AddMatePersistent.html) | Add copy of a mate to a Placement3D. |
| Public Methodstatic (Shared in Visual Basic) | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~CopyTo.html) | Overloaded. Copy 3D Placement Placement3D and its children will be copied into the same Project as newParent Then parent of the copy will be set to newParent new parent of copy |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Dispose().html) | Destructor for deterministic finalization of Placement3D object. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Equals.html) | Operator of comparison implementation. Checks if two StorableObjects refer to the same object in the project. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [FindSourceMate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~FindSourceMate.html) | Overloaded. Find source mate by name. Mate namePlacement optionsConsider child mounting surfaces |
| Public Method | [FindTargetMate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~FindTargetMate.html) | Overloaded. Find target mate by name. Mate nameConsider mounting clearanceConsider child mounting surfaces |
| Public Method | [GetBoundingBox](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~GetBoundingBox.html) | Returns bounding box of a Placement3D. |
| Public Method | [GetBoundingBoxRelative](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~GetBoundingBoxRelative.html) | Returns relative bounding box of a Placement3D. |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetHashCode.html) | Serves as the default hash function. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetSourceMates](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~GetSourceMates.html) | Overloaded. Get array of all source mates from this object. Placement optionsConsider child mounting surfaces |
| Public Method | [GetTargetMates](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~GetTargetMates.html) | Overloaded. Get array of all target mates from this object. Consider mounting clearanceConsider child mounting surfaces |
| Public Method | [GetTypeName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetTypeName.html) | Returns object type name. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [LockObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~LockObject().html) | Tries to lock current object in database for exclusive access. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Move](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~Move.html) | Move this object. |
| Public Method | [MoveRelative](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~MoveRelative.html) | Move this object relative to its parent. |
| Public Method | [Remove](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~Remove.html) | Removes object from project and all its children. |
| Public Method | [RemoveConnectionPointPosition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~RemoveConnectionPointPosition.html) | Removes connection point data stored under given index. |
| Public Method | [RemovePlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~RemovePlacement.html) | Removes object and all its children only from layout space. |
| Public Method | [SetParent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~SetParent.html) | Sets parent placement. Sets parent placement. |
| Public Method | [SmartLock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~SmartLock.html) | Tries to lock current object. If object is [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) - it's page will be locked as well; [Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) locks it's installation space; [Eplan.EplApi.DataModel.Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) locks all it's connections and connection definition points; [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) locks all placements from this page. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [StoreConnectionPointPosition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~StoreConnectionPointPosition.html) | Stores data from connection point position in function under given index. |
| Public Method | [SwitchLocalPropertyPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~SwitchLocalPropertyPlacements.html) | Copies or removes all local ProperyPlacemnets and sets flag |
| Public Method | [ToStringIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ToStringIdentifier.html) | Returns this object as string identifier. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |


