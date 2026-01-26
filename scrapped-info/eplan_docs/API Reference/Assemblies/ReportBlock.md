# ReportBlock

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock.html

---

This class represents a set of data which is used for report generation or update.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)  
      **Eplan.EplApi.DataModel.ReportBlock**

Syntax

**C#**



public class ReportBlock : StorableObject

public ref class ReportBlock : public StorableObject

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [ReportBlock Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~_ctor().html) | Default constructor. To use object created by this constructor function `Create()` is need to be called after that. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Action](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~Action.html) | Gets/Sets a name of an action which may be used for customizing the report through API. |
| Public Property | [CreateDate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~CreateDate.html) | Gets creation date |
| Public Property | [CrossReferencedObjectsAll](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~CrossReferencedObjectsAll.html) | Returns an array of objects cross-referenced with this object (i.e. having the same name - in case of functions - or otherwise associated) (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [DatabaseIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~DatabaseIdentifier.html) | Returns the project as number. The number is unique for all open projects in one session. The number changes when the project is closed and opened again. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [DeviceTag](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~DeviceTag.html) | Names of devices assign to this report separated by a semicolon. |
| Public Property | [DeviceTagNameParts](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~DeviceTagNameParts.html) | Array of names of devices assign to this report stored in property lists. |
| Public Property | [FilterSchemaData](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~FilterSchemaData.html) | Property data represents filter scheme settings for report generation. |
| Public Property | [FilterSchemaName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~FilterSchemaName.html) | Name of filter scheme. |
| Public Property | [FormName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~FormName.html) | Name of the form without file extension. |
| Public Property | [FunctionFilterSchemaData](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~FunctionFilterSchemaData.html) | Property data represents function filter scheme settings for report generation. |
| Public Property | [FunctionFilterSchemaName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~FunctionFilterSchemaName.html) | Name of function filter scheme. |
| Public Property | [Functions](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~Functions.html) | Evaluated functions. |
| Public Property | [FunctionSortSchemaData](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~FunctionSortSchemaData.html) | Property data represents function sort scheme settings for report generation. |
| Public Property | [FunctionSortSchemaName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~FunctionSortSchemaName.html) | Name of function sort scheme. |
| Public Property | [IsAutomaticPageDescription](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~IsAutomaticPageDescription.html) | Determines if page description is generated automatically. |
| Public Property | [IsLocked](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsLocked.html) | Determines if the the StorableObject is locked.  The StorableObject is locked when it was explicitly or implicitly locked. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsReadOnly.html) | Determines if StorableObject is read-only (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsTransient.html) | Determines if the the StorableObject is transient.  The StorableObject is transient when it was created by default constructor and:  it is a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) and it was not assigned a [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html),  it is a [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) or any class derived from it and was not assigned a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsValid](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsValid.html) | Determines if StorableObject is correct database object and is not deleted. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [ManualPageDescription](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~ManualPageDescription.html) | Text used for describing page, if automatic page description if switched off. |
| Public Property | [ObjectIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ObjectIdentifier.html) | Returns the object identifier as number. The number is unique for all objects of this type. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Project.html) | Returns the project to which the StorableObject belongs. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Properties](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~Properties.html) | EPLAN properties of the ReportBlock object. |
| Public Property | [SortSchemaData](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~SortSchemaData.html) | Property data represents sort scheme settings for report generation. |
| Public Property | [SortSchemaName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~SortSchemaName.html) | Name of sort scheme. |
| Public Property | [Type](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~Type.html) | Type of evaluation. |
| Public Property | [TypeIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~TypeIdentifier.html) | Returns the type of the object as number. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Create](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~Create.html) | Create a new transient ReportBlock object. |
| Public Method | [Delete](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~Delete.html) | Deletes all report pages belonging to a report block. |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Dispose().html) | Destructor for deterministic finalization of ReportBlock object. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Equals.html) | Operator of comparison implementation. Checks if two StorableObjects refer to the same object in the project. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Freeze](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~Freeze.html) | Removes the selected report block. The associated report pages remain as they are and are no longer updated. |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetHashCode.html) | Serves as the default hash function. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetTypeName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetTypeName.html) | Returns object type name. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [LockObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~LockObject().html) | Tries to lock current object in database for exclusive access. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [SmartLock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~SmartLock.html) | Tries to lock current object. If object is [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) - it's page will be locked as well; [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) locks it's installation space; [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) locks all it's connections and connection definition points; [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) locks all placements from this page. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [ToStringIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ToStringIdentifier.html) | Returns this object as string identifier. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |


