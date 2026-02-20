# Project

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html

---

Class representing P8 project.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)  
      **Eplan.EplApi.DataModel.Project**

Syntax

**C#**



public class Project : StorableObject, IArticleUser

public ref class Project : public StorableObject, IArticleUser


Remarks

Some properties of Data model classes are not linked with their owners even if from the syntax it may seem otherwise. Like in this line: oRectangle.Pen.ColorId = 5, the ColorId of the Pen is changed but oRectangle object doesn't know about it since the Pen property is a stand alone value not aware of oRectangle object existence. This remark applies to the following Project properties: Articles, LayerTable, Pages.

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Project Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~_ctor().html) | Default constructor. Should never be used. Always throws NotImplementedException. It was designed only for COM compatibility. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ArticleReferences](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~ArticleReferences.html) | Returns [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)s that are referenced by Project. |
| Public Property | [Articles](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~Articles.html) | Returns [Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)s of the Project. |
| Public Property | [CanHaveArticleData](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~CanHaveArticleData.html) | Check if the Project can have [Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)s. |
| Public Property | [Comparisons](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~Comparisons.html) | Returns results of comparisons of projects. |
| Public Property | [CrossReferencedObjectsAll](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~CrossReferencedObjectsAll.html) | Returns an array of objects cross-referenced with this object (i.e. having the same name - in case of functions - or otherwise associated) (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [CurrentUsers](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~CurrentUsers.html) | Returns the current users working at this project. |
| Public Property | [DatabaseIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~DatabaseIdentifier.html) | Returns the project as number. The number is unique for all open projects in one session. The number changes when the project is closed and opened again. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [DeviceTagConfig](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~DeviceTagConfig.html) | Predefined property for accessing following project settings: EnableSyntaxCheck, UserCharacters, AllowUserCharacters, AllowedLetters, AllowSpecialCharacters, PlantDesignationNumbersOnly. |
| Public Property | [DocumentDirectory](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~DocumentDirectory.html) | Project's property which return full project documents' directory name |
| Public Property | [Filter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~Filter.html) | Enables access to pages filter. |
| Public Property | [FunctionDefinitionLibrary](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~FunctionDefinitionLibrary.html) | Returns standard [Eplan.EplApi.DataModel.MasterData.FunctionDefinitionLibrary](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.FunctionDefinitionLibrary.html) of project. |
| Public Property | [ImageDirectory](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~ImageDirectory.html) | Project's property which return full project images' directory name. |
| Public Property | [InstallationSpaces](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~InstallationSpaces.html) | Returns array of all [Eplan.EplApi.DataModel.E3D.InstallationSpace](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.InstallationSpace.html) from this Project. |
| Public Property | [IsExclusive](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~IsExclusive.html) | Project's property which gives information if the project is opened exclusive |
| Public Property | [IsLocked](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~IsLocked.html) | Overridden. Determines if the the StorableObject is locked.  The StorableObject is locked when it was explicitly or implicitly locked. |
| Public Property | [IsOpen](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~IsOpen.html) | Project's property which gives information if the project is opened or is not. |
| Public Property | [IsReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~IsReadOnly.html) | Overridden. Determines if StorableObject is read-only |
| Public Property | [IsTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsTransient.html) | Determines if the the StorableObject is transient.  The StorableObject is transient when it was created by default constructor and:  it is a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) and it was not assigned a [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html),  it is a [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) or any class derived from it and was not assigned a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsValid](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsValid.html) | Determines if StorableObject is correct database object and is not deleted. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [LayerTable](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~LayerTable.html) | Returns layer table of the project. |
| Public Property | [ObjectIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ObjectIdentifier.html) | Returns the object identifier as number. The number is unique for all objects of this type. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [OptionGroups](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~OptionGroups.html) | Returns array of [OptionGroup](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionGroup.html)s assigned to the `Project`. |
| Public Property | [Options](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~Options.html) | Returns array of [Option](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Option.html)s assigned to the `Project` but not those that are assigned to OptionGroups. |
| Public Property | [Pages](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~Pages.html) | Project's property which return array of Pages placed in project. When the project's PagesFilter was set-up, pages matching the filter are returned. |
| Public Property | [PlanningSegments](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~PlanningSegments.html) | Returns array of all [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html) from this Project. |
| Public Property | [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Project.html) | Returns the project to which the StorableObject belongs. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [ProjectDirectoryPath](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~ProjectDirectoryPath.html) | Project's property which return full project's directory name. |
| Public Property | [ProjectFullName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~ProjectFullName.html) | Project's property which return full project name, without an extension. |
| Public Property | [ProjectLinkFilePath](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~ProjectLinkFilePath.html) | Project's property which return full project-link file name. |
| Public Property | [ProjectName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~ProjectName.html) | Project's property which return Name of Project - project name only without path. |
| Public Property | [Properties](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~Properties.html) | Enables access to P8 properties of the project. |
| Public Property | [PropertyPlacementsSchemaId](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~PropertyPlacementsSchemaId.html) | Gets currently used scheme Id that was selected in the GUI in ribbon Tools / Property Arrangements ribbon. |
| Public Property | [Sections](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~Sections.html) | Returns an object used to manage project sections. |
| Public Property | [SegmentDefinitions](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~SegmentDefinitions.html) | Returns array of all [Eplan.EplApi.DataModel.Planning.SegmentDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinition.html) from this Project. |
| Public Property | [SegmentTemplates](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~SegmentTemplates.html) | Returns array of all [Eplan.EplApi.DataModel.Planning.SegmentTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplate.html) from this Project. |
| Public Property | [Settings](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~Settings.html) | Project settings |
| Public Property | [SymbolLibraries](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~SymbolLibraries.html) | Gets the symbol libraries used by the project. |
| Public Property | [TypeIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~TypeIdentifier.html) | Returns the type of the object as number. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [TypeOfProject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~TypeOfProject.html) | Type of project To change this property project will be reopened temporarily in exclusive mode. If project cannot be reopened in exclusive mode BaseException will be thrown. |
| Public Property | [UserDefinedPropertyDefinitions](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~UserDefinedPropertyDefinitions.html) | Returns array of all [UserDefinedPropertyDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UserDefinedPropertyDefinition.html) from this project. |



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


