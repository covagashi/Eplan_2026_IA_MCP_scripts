# ArticleReference

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html

---

This class represents a part reference on a project, function, or a connection.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)  
      **Eplan.EplApi.DataModel.ArticleReference**  
         [Eplan.EplApi.DataModel.EObjects.TerminalAccessory](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalAccessory.html)

Syntax

**C#**



public class ArticleReference : StorableObject

public ref class ArticleReference : public StorableObject


Remarks

For further information, see [WorkingWithParts](WorkingWithParts.html). Some part reference properties are taken from the part if they are set to empty on the reference. Mind that ArticleReference is offline object and if you change a property from ArticleReference.Properties, you need to call the [StoreToObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~StoreToObject.html) method in order to write data to corresponding properties of parent object (Project/Function/Connection).

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [ArticleReference Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~_ctor(String,String,UInt32).html) | Constructor used to create transient article reference object. That object can be passed as a parameter to ConnectionDefinitionPoint() function. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~Article.html) | Returns the article of this articlereference. This is the Article stored in the Project, can be NULL if the article is not found in Project. |
| Public Property | [BelongsToArticlePlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~BelongsToArticlePlacement.html) | Returns true, if the article reference contains to an article placement |
| Public Property | [Count](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~Count.html) | Sets and gets count |
| Public Property | [CrossReferencedObjectsAll](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~CrossReferencedObjectsAll.html) | Returns an array of objects cross-referenced with this object (i.e. having the same name - in case of functions - or otherwise associated) (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [DatabaseIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~DatabaseIdentifier.html) | Returns the project as number. The number is unique for all open projects in one session. The number changes when the project is closed and opened again. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [FunctionTemplates](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~FunctionTemplates.html) | Returns an array of transient object (of Connection or Function type) that represent function templates associated with the article referenced by this object. |
| Public Property | [IdentifyingName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~IdentifyingName.html) | Gets the identifying device tag of the parent function(property ArticleReferencePropertyList.ARTICLEREF\_IDENTNAME). |
| Public Property | [IsAssembly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~IsAssembly.html) | Represents this reference an assembly |
| Public Property | [IsLocked](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsLocked.html) | Determines if the the StorableObject is locked.  The StorableObject is locked when it was explicitly or implicitly locked. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsReadOnly.html) | Determines if StorableObject is read-only (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsTransient.html) | Determines if the the StorableObject is transient.  The StorableObject is transient when it was created by default constructor and:  it is a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) and it was not assigned a [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html),  it is a [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) or any class derived from it and was not assigned a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsValid](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsValid.html) | Determines if StorableObject is correct database object and is not deleted. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [ObjectIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ObjectIdentifier.html) | Returns the object identifier as number. The number is unique for all objects of this type. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [ParentObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~ParentObject.html) | Returns the Object this ArticleReference belongs to. |
| Public Property | [PartNr](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~PartNr.html) | Returns ArticleReference's part number. |
| Public Property | [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Project.html) | Returns the project to which the StorableObject belongs. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Properties](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~Properties.html) | Represents ArticleReference properties |
| Public Property | [ReferencePos](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~ReferencePos.html) | Returns the index of the ArticleReference reference for the given article if it is referenced by a [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html). This number is useful when reading values of article reference properties (indexed properties on function, e.g. FUNC\_ARTICLE\_COUNT). It is not equal to the 0-based position of element in the table of articles which is returned by Function.Articles/> |
| Public Property | [TypeIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~TypeIdentifier.html) | Returns the type of the object as number. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [VariantNr](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~VariantNr.html) | Sets and gets ArticleReference's variant number. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Dispose().html) | Destructor for deterministic finalization of ArticleReference object. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Equals.html) | Operator of comparison implementation. Checks if two StorableObjects refer to the same object in the project. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetHashCode.html) | Serves as the default hash function. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetTypeName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetTypeName.html) | Returns object type name. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [LockObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~LockObject().html) | Tries to lock current object in database for exclusive access. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [RemoveArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~RemoveArticleReference.html) | Removes the ArticleReference from the Object. |
| Public Method | [SmartLock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~SmartLock.html) | Tries to lock current object. If object is [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) - it's page will be locked as well; [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) locks it's installation space; [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) locks all it's connections and connection definition points; [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) locks all placements from this page. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [StoreToObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~StoreToObject.html) | Commits all changes of the ArticleReference to the matching properties of a parent object (Project/Function/Connection). |
| Public Method | [ToStringIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ToStringIdentifier.html) | Returns this object as string identifier. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |


