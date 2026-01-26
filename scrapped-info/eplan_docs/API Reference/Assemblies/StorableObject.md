# StorableObject

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html

---

The parent of all API classes representing P8 project and its structure.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.DataModel.StorableObject**  
      [Eplan.EplApi.DataModel.Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)  
      [Eplan.EplApi.DataModel.ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)  
      [Eplan.EplApi.DataModel.Connection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html)  
      [Eplan.EplApi.DataModel.ConnectionPointsInfo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfo.html)  
      [Eplan.EplApi.DataModel.DaisyChain](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DaisyChain.html)  
      [Eplan.EplApi.DataModel.DeviceListEntry](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceListEntry.html)  
      [Eplan.EplApi.DataModel.E3D.Group3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3D.html)  
      [Eplan.EplApi.DataModel.E3D.PlaceHolder3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlaceHolder3D.html)  
      [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)  
      [Eplan.EplApi.DataModel.FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition.html)  
      [Eplan.EplApi.DataModel.Location](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Location.html)  
      [Eplan.EplApi.DataModel.MasterData.FunctionDefinitionLibrary](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.FunctionDefinitionLibrary.html)  
      [Eplan.EplApi.DataModel.MasterData.Symbol](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Symbol.html)  
      [Eplan.EplApi.DataModel.MasterData.SymbolLibrary](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibrary.html)  
      [Eplan.EplApi.DataModel.MergedArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReference.html)  
      [Eplan.EplApi.DataModel.MergedConnection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedConnection.html)  
      [Eplan.EplApi.DataModel.MergedFunction](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedFunction.html)  
      [Eplan.EplApi.DataModel.OptionBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionBase.html)  
      [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)  
      [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)  
      [Eplan.EplApi.DataModel.Planning.SegmentDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinition.html)  
      [Eplan.EplApi.DataModel.Planning.SegmentTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplate.html)  
      [Eplan.EplApi.DataModel.PlcIO](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlcIO.html)  
      [Eplan.EplApi.DataModel.Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html)  
      [Eplan.EplApi.DataModel.ReportBlock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock.html)  
      [Eplan.EplApi.DataModel.Revisions.Comparison](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Revisions.Comparison.html)  
      [Eplan.EplApi.DataModel.Revisions.ComparisonEntry](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Revisions.ComparisonEntry.html)  
      [Eplan.EplApi.DataModel.Revisions.ComparisonEntryDetail](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Revisions.ComparisonEntryDetail.html)

Syntax

**C#**



public class StorableObject

public ref class StorableObject

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [CrossReferencedObjectsAll](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~CrossReferencedObjectsAll.html) | Returns an array of objects cross-referenced with this object (i.e. having the same name - in case of functions - or otherwise associated) |
| Public Property | [DatabaseIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~DatabaseIdentifier.html) | Returns the project as number. The number is unique for all open projects in one session. The number changes when the project is closed and opened again. |
| Public Property | [IsLocked](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsLocked.html) | Determines if the the StorableObject is locked.  The StorableObject is locked when it was explicitly or implicitly locked. |
| Public Property | [IsReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsReadOnly.html) | Determines if StorableObject is read-only |
| Public Property | [IsTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsTransient.html) | Determines if the the StorableObject is transient.  The StorableObject is transient when it was created by default constructor and:  it is a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) and it was not assigned a [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html),  it is a [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) or any class derived from it and was not assigned a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). |
| Public Property | [IsValid](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsValid.html) | Determines if StorableObject is correct database object and is not deleted. |
| Public Property | [ObjectIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ObjectIdentifier.html) | Returns the object identifier as number. The number is unique for all objects of this type. |
| Public Property | [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Project.html) | Returns the project to which the StorableObject belongs. |
| Public Property | [Properties](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Properties.html) | .NET Property enabling access to P8 properties of the StorableObject object. |
| Public Property | [TypeIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~TypeIdentifier.html) | Returns the type of the object as number. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Dispose().html) | Destructor for deterministic finalization of StorableObject object. |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Equals.html) | Operator of comparison implementation. Checks if two StorableObjects refer to the same object in the project. |
| Public Methodstatic (Shared in Visual Basic) | [FromStringIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~FromStringIdentifier.html) | Overloaded. Returns this object created from the string identifier |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetHashCode.html) | Serves as the default hash function. |
| Public Method | [GetTypeName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetTypeName.html) | Returns object type name. |
| Public Method | [LockObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~LockObject().html) | Tries to lock current object in database for exclusive access. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. |
| Public Method | [SmartLock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~SmartLock.html) | Tries to lock current object. If object is [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) - it's page will be locked as well; [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) locks it's installation space; [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) locks all it's connections and connection definition points; [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) locks all placements from this page. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. |
| Public Method | [ToStringIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ToStringIdentifier.html) | Returns this object as string identifier. |
| Public Methodstatic (Shared in Visual Basic) | [TryParseIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~TryParseIdentifier.html) | Overloaded. Returns this object created from the string identifier for the databaseid newDbId. |



Public Operators

|  |  |
| --- | --- |
| public Operator [Equality](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~op_Equality.html) | Operator of comparison implementation. Checks if two StorableObjects refer to the same object in the project. |
| public Operator [Inequality](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~op_Inequality.html) | Operator of comparison implementation. Checks if two StorableObjects refer to different object in the project. |


