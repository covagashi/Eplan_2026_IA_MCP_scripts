# Methods

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment_methods.html

---

For a list of all members of this type, see [PlanningSegment members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment_members.html).

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~AddArticleReference.html) | Overloaded. Adds a new [Eplan.EplApi.DataModel.ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html) to the PlanningSegment. |
| Public Method | [AddLocalTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~AddLocalTemplate.html) | Add new local template based on function definition. |
| Public Method | [AddPLCAddress](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~AddPLCAddress.html) | Overloaded. Creates copy of existing PLC inputs or outputs for this planning object. |
| Public Method | [CollectStructureProperties](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~CollectStructureProperties.html) | Returns [Eplan.EplApi.DataModel.FunctionBasePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBasePropertyList.html). |
| Public Methodstatic (Shared in Visual Basic) | [Create](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~Create.html) | Creates PlanningSegment object. |
| Public Methodstatic (Shared in Visual Basic) | [CreateLink](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~CreateLink.html) | Overloaded. Creates a link between two given PlanningSegments. |
| Public Methodstatic (Shared in Visual Basic) | [CreateTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~CreateTransient.html) | Creates transient PlanningSegment object. |
| Public Method | [DeleteLink](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~DeleteLink.html) | Deletes a link from this object that links given targetSegment. |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Dispose().html) | Destructor for deterministic finalization of PlanningSegment object. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Equals.html) | Operator of comparison implementation. Checks if two StorableObjects refer to the same object in the project. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetHashCode.html) | Serves as the default hash function. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetTypeName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetTypeName.html) | Returns object type name. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetWriteProtectionFlagSet](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~GetWriteProtectionFlagSet.html) | Checks if a specific write protection kind was set. |
| Public Method | [LockObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~LockObject().html) | Tries to lock current object in database for exclusive access. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [PauseWriteProtection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~PauseWriteProtection.html) | Temporarily disables write protection. Note that current write protection flags are not cleared. |
| Public Method | [PlaceAt](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~PlaceAt.html) | Places the segment onto the given page, in the given location. |
| Public Method | [PlaceMacroAt](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~PlaceMacroAt.html) | Places a macro on a given page. |
| Public Method | [Remove](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~Remove.html) | Removes object from PlanningSegment with all its children. |
| Public Method | [RemoveArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~RemoveArticleReference.html) | Removes the ArticleReference from the PlanningSegment |
| Public Method | [RemoveLocalTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~RemoveLocalTemplate.html) | Removes a local template from this object. |
| Public Method | [RemovePLCAddress](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~RemovePLCAddress.html) | Removes existing PLC input or output from this planning object. |
| Public Method | [RevertToTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~RevertToTemplate.html) | Restores information stored in template to planning object. |
| Public Method | [SmartLock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~SmartLock.html) | Tries to lock current object. If object is [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) - it's page will be locked as well; [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) locks it's installation space; [Eplan.EplApi.DataModel.Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) locks all it's connections and connection definition points; [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) locks all placements from this page. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [ToStringIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ToStringIdentifier.html) | Returns this object as string identifier. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |


