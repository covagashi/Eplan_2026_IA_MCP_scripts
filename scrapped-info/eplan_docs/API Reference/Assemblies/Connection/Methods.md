# Methods

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection_methods.html

---

For a list of all members of this type, see [Connection members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection_members.html).

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~AddArticleReference.html) | Overloaded. Adds a new [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html) to the Connection. Returns the added [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html). |
| Public Method | [Assign](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~Assign.html) | Assigns this connection to another, which means that values of this connection's properties are copied to the target connection and the source connection itself is removed from the project. |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Dispose().html) | Destructor for deterministic finalization of Connection object. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Equals.html) | Operator of comparison implementation. Checks if two StorableObjects refer to the same object in the project. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetHashCode.html) | Serves as the default hash function. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetTypeName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetTypeName.html) | Returns object type name. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetWriteProtectionFlagSet](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~GetWriteProtectionFlagSet.html) | Checks if a specific write protection kind was set. |
| Public Method | [LockObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~LockObject().html) | Tries to lock current object in database for exclusive access. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [MakePersistent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~MakePersistent.html) | Allows to create non-placed connection from a connection template. In effect connection template becomes covered template. |
| Public Method | [PauseWriteProtection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~PauseWriteProtection.html) | Temporarily disables write protection. Note that current write protection flags are not cleared. |
| Public Method | [PlaceAsConnectionDefinitionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~PlaceAsConnectionDefinitionPoint.html) | Places this connection as a connection def. point on the given schematic page and in the given location. If this is an uncovered connection template and the location points to a connection line on schematic page, the template automatically becomes covered (i.e. connection is created in the project) Note: When uncovered connection template becomes covered, connections on the page are updated which may affect performance. If this method needs to be called repeatedly, use the [DisableConnectionUpdateStep](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DisableConnectionUpdateStep.html) object to make the performance better. |
| Public Method | [Remove](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~Remove.html) | Removes the connection from the [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html). |
| Public Method | [RemoveArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~RemoveArticleReference.html) | Removes the ArticleReference from the Connecttion |
| Public Method | [SmartLock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~SmartLock.html) | Tries to lock current object. If object is [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) - it's page will be locked as well; [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) locks it's installation space; [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) locks all it's connections and connection definition points; [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) locks all placements from this page. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [ToStringIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ToStringIdentifier.html) | Returns this object as string identifier. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |


