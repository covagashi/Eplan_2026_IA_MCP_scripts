# WindowMacro

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro.html

---

This class represents a window macro

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.MasterData.Macro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro.html)  
      **Eplan.EplApi.DataModel.MasterData.WindowMacro**  
         [Eplan.EplApi.DataModel.MasterData.SymbolMacro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolMacro.html)

Syntax

**C#**



public class WindowMacro : Macro

public ref class WindowMacro : public Macro


Remarks

For variant of macro which contains 3d objects local coordinate system is created. Origin of this coordinate system is in the origin of first object from macro.

If user does not point the location of handle then it is automatically calculated in origin of first object or its top parent.

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [WindowMacro Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~_ctor.html) | Constructor. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [CountOfPages](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro~CountOfPages.html) | Get the count of Pages in this macro (Inherited from [Eplan.EplApi.DataModel.MasterData.Macro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro.html)) |
| Public Property | [CustomLayerTable](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro~CustomLayerTable.html) | Gets layer table of custom layers (Inherited from [Eplan.EplApi.DataModel.MasterData.Macro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro.html)) |
| Public Property | [Description](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro~Description.html) | Gets description in multiple languages (Inherited from [Eplan.EplApi.DataModel.MasterData.Macro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro.html)) |
| Public Property | [HasReferencePoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~HasReferencePoint.html) | Returns true if a reference point has been defined for this macro. |
| Public Property | [Location](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~Location.html) | The position of lower left corner of the macro defined by the user when storing it. |
| Public Property | [Objects](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~Objects.html) | Returns all Eplan.EplApi.DataModel.Placement contained in the macro. |
| Public Property | [Objects3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~Objects3D.html) | Returns all Eplan.EplApi.DataModel.Placement3D contained in the macro. |
| Public Property | [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~Page.html) | Returns the [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) on which the macro was created. |
| Public Property | [PageProperty](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro~PageProperty.html) | Gets the property of the n-th page in this macro (Inherited from [Eplan.EplApi.DataModel.MasterData.Macro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro.html)) |
| Public Property | [PlaceHolders](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~PlaceHolders.html) | Returns all Eplan.EplApi.DataModel.Graphics.PlaceHolder contained in the macro. |
| Public Property | [PlaceHolders3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~PlaceHolders3D.html) | Returns all [Eplan.EplApi.DataModel.E3D.PlaceHolder3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlaceHolder3D.html) contained in the macro. |
| Public Property | [PlacementAreaTransformation](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~PlacementAreaTransformation.html) | Returns the transformation of macro placement area. |
| Public Property | [ReferencePoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~ReferencePoint.html) | The reference point of the macro defined by the user when storing it. |
| Public Property | [ReferencePoint3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~ReferencePoint3D.html) | The position of user defined handle. |
| Public Property | [RepresentationType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~RepresentationType.html) | the used variant |
| Public Property | [RepresentationTypes](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~RepresentationTypes.html) | macro Representation Types. |
| Public Property | [Size](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~Size.html) | Returns the size of the macro. When available it is the size of the macro box, otherwise the graphical size (selection). If no selection was made when macro was created (for example via P8-API), it is a minimal size needed to contain all placements. If macro doesn't contain any placements, returned size is equal to (0,0). |
| Public Property | [TopLevelObjects](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~TopLevelObjects.html) | Returns all Eplan.EplApi.DataModel.Placements, with no parent. |
| Public Property | [TopLevelObjects3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~TopLevelObjects3D.html) | Returns all Eplan.EplApi.DataModel.Placement3D, with no parent. |
| Public Property | [Variant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~Variant.html) | The used variant. |



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


