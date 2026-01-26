# Properties

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project_properties.html

---

For a list of all members of this type, see [Project members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project_members.html).

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


