# Methods

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro_methods.html

---

For a list of all members of this type, see [WindowMacro members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro_members.html).

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CalculateReferencePoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~CalculateReferencePoint.html) | Calculates the reference point of the macro Used to calculate reference point if reference point has not been defined by the user, when creating a macro. When reference point has been defined for then given macro, then output parameter is equal to ReferencePoint property. |
| Public Method | [CalculateReferencePoint3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~CalculateReferencePoint3D.html) | Calculates the reference point of the macro Used to calculate reference point if reference point has not been defined by the user, when creating a macro. When reference point has been defined for then given macro, then output parameter is equal to ReferencePoint property. |
| Public Method | [ChangeCurrentVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~ChangeCurrentVariant.html) | Change current representation type and variant of macro This function is more efficient as changing the Properties RepresentationType and Variant separately besides, this function throws an exception, if the variant does not exist |
| Public Method | [Create](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~Create.html) | Overloaded. Writes a window macro file from the pPlacements If at least one given Placement object is valid, created macro is opened. |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro~Dispose().html) | Destructor for deterministic finalization of WindowMacro object. (Inherited from [Eplan.EplApi.DataModel.MasterData.Macro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro.html)) |
| Public Method | [ExistVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~ExistVariant.html) | Overloaded. checks, if the variant exists inside the window macro |
| Public Method | [GetBoundingBox](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~GetBoundingBox.html) | Returns the bounding box of the macro. This is the size and position of the macrobox. |
| Public Method | [GetBoundingBox3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~GetBoundingBox3D.html) | Returns the least bounding box containing all 3d elements of macro in current variant. |
| Public Method | [GetVariants](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~GetVariants.html) | Macro variants by representation type "nRepresentationType". |
| Public Method | [GetWindowMacroInterface](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~GetWindowMacroInterface.html) |  |
| Public Methodstatic (Shared in Visual Basic) | [MacroRepresentationTypeNameFromId](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~MacroRepresentationTypeNameFromId.html) | Converts macro representation type to a displayed name. |
| Public Method | [Open](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~Open.html) | Overloaded. Opens a macro file and reads the information. |
| Public Method | [ResetPositions3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~ResetPositions3D.html) | Overloaded. Resets positions of items of a 3d macro according to one of its objects. |
| Public Method | [Source](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~Source.html) | Get name of the source from current representation type |
| Public Method | [SourceProject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~SourceProject.html) | Get name of the source project from current representation type |
| Public Method | [StoreExternalFilesOfCurrentVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro~StoreExternalFilesOfCurrentVariant.html) | Copies external files into project images directory (Inherited from [Eplan.EplApi.DataModel.MasterData.Macro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro.html)) |
| Public Method | [Version](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~Version.html) | Get version from current representation type |


