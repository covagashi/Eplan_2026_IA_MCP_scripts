# Methods

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3D_methods.html

---

For a list of all members of this type, see [Group3D members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3D_members.html).

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddMate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3D~AddMate.html) | Overloaded. Adds a mate to a group |
| Public Method | [Create](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3D~Create.html) | Creates a new Group3D object. |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Dispose().html) | Destructor for deterministic finalization of the Group3D object. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Equals.html) | Operator of comparison implementation. Checks if two StorableObjects refer to the same object in the project. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetHashCode.html) | Serves as the default hash function. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetMates](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3D~GetMates.html) | Gets group mates |
| Public Method | [GetTypeName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetTypeName.html) | Returns object type name. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [InsertSubPlacement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3D~InsertSubPlacement3D.html) | Inserts [Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) to the 3D group. |
| Public Method | [InsertSubPlacement3Ds](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3D~InsertSubPlacement3Ds.html) | Inserts [Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)s to the 3D group. |
| Public Method | [LockObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~LockObject().html) | Tries to lock current object in database for exclusive access. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Move](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3D~Move.html) | Moves the Group3D object relative to absolute axis origin. |
| Public Method | [Remove](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3D~Remove.html) | Removes the 3D group and all grouped [Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)s. |
| Public Method | [RemoveSubPlacement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3D~RemoveSubPlacement3D.html) | Overloaded. Removes [Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) from the 3D group and from the project. The Placement3D object passed into this method is no longer valid. |
| Public Method | [RemoveSubPlacement3Ds](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3D~RemoveSubPlacement3Ds.html) | Overloaded. Removes [Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)s from the 3D group and from the project. The Placement3D objects passed into this method are no longer valid. |
| Public Method | [SmartLock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~SmartLock.html) | Tries to lock current object. If object is [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) - it's page will be locked as well; [Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) locks it's installation space; [Eplan.EplApi.DataModel.Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) locks all it's connections and connection definition points; [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) locks all placements from this page. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [ToStringIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ToStringIdentifier.html) | Returns this object as string identifier. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [UnGroup](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3D~UnGroup.html) | Overloaded. Removes [Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)s only from the 3D group. |


