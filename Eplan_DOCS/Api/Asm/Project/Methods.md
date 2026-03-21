# Methods

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project_methods.html

---

For a list of all members of this type, see [Project members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project_members.html).

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~AddArticleReference.html) | Overloaded. Adds a new [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html) to the Project. Returns the added [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html). |
| Public Method | [AddOption](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~AddOption.html) | Overloaded. Adds [Option](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Option.html) to the `Project`. |
| Public Method | [AddOptionGroup](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~AddOptionGroup.html) | Overloaded. Adds [OptionGroup](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionGroup.html) to the `Project`. The description is set to an empty multilang value. |
| Public Method | [ChangeLocationName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~ChangeLocationName.html) | Changes name of the given location. After that change a location object becomes invalid, to get this object once again, use the GetLocationObjects function. |
| Public Method | [Close](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~Close.html) | Closes the project. Must not be called before Remove() |
| Public Method | [CreateLocation](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~CreateLocation.html) | Overloaded. Creates location in the given hierarchy, and places it in position eRelPos relatively to the existing location strExistingLocation. |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Dispose().html) | Destructor for deterministic finalization of Project object. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Equals.html) | Operator of comparison implementation. Checks if two StorableObjects refer to the same object in the project. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetHashCode.html) | Serves as the default hash function. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetLocationObjects](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~GetLocationObjects.html) | Overloaded. Returns array of all project's location objects. |
| Public Method | [GetLocationPrototype](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~GetLocationPrototype.html) | Creates location prototype using property list pProps. Property identifiers that describe location are written to the list. |
| Public Method | [GetLocations](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~GetLocations.html) | Returns array of names of project's location for given hierarchy type (PLANT, LOCATION etc.) |
| Public Method | [GetNamePrototype](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~GetNamePrototype.html) | Overloaded. Gets the name prototype for a given function group. For given function group two separate lists with properties used in project structure are created. |
| Public Method | [GetOptionByName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~GetOptionByName.html) | Method for finding [Option](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Option.html) assigned to the `Project` with a given name. |
| Public Method | [GetOptionGroupByName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~GetOptionGroupByName.html) | Method for finding [OptionGroup](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionGroup.html) assigned to the `Project` with a given name. |
| Public Method | [GetSegmentDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~GetSegmentDefinition.html) | Returns [Eplan.EplApi.DataModel.Planning.SegmentDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinition.html) from this Project with given name. |
| Public Method | [GetTypeName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetTypeName.html) | Returns object type name. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [LockAllObjects](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~LockAllObjects.html) | Locks all data model objects in the project. |
| Public Method | [LockObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~LockObject().html) | Tries to lock current object in database for exclusive access. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [ParseNameAndProps](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~ParseNameAndProps.html) | Parsing of function name with additional properties. |
| Public Method | [Remove](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~Remove.html) | Removes the project. Must not be called after Close() |
| Public Method | [RemoveAllPages](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~RemoveAllPages.html) | Removes all pages from project. |
| Public Method | [RemoveArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~RemoveArticleReference.html) | Removes the ArticleReference from the Project |
| Public Method | [SetSortedLocations](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~SetSortedLocations.html) | Sets the location order, as in the arrLocations parameter, for given hierarchy type. Locations existing in project and not passed in arrLocations are placed after the passed ones. If arrLocations parameter contains not existing location name, this method returns false and no changes are made to the project |
| Public Method | [SmartLock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~SmartLock.html) | Tries to lock current object. If object is [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) - it's page will be locked as well; [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) locks it's installation space; [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) locks all it's connections and connection definition points; [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) locks all placements from this page. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [ToString](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~ToString.html) | Returns a string that represents the current object. |
| Public Method | [ToStringIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ToStringIdentifier.html) | Returns this object as string identifier. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |


