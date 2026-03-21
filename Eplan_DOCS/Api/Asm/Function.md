# Function

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html

---

A class that represents logical devices (or device sub-components) of [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html)'s [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html).

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)  
      [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)  
         [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)  
            [Eplan.EplApi.DataModel.FunctionBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase.html)  
               **Eplan.EplApi.DataModel.Function**  
                  [Eplan.EplApi.DataModel.BoxedDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BoxedDevice.html)  
                  [Eplan.EplApi.DataModel.ConnectionDefinitionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint.html)  
                  [Eplan.EplApi.DataModel.EObjects.Cable](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Cable.html)  
                  [Eplan.EplApi.DataModel.EObjects.CableUnit](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.CableUnit.html)  
                  [Eplan.EplApi.DataModel.EObjects.Harness](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Harness.html)  
                  [Eplan.EplApi.DataModel.EObjects.PLC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PLC.html)  
                  [Eplan.EplApi.DataModel.EObjects.Plug](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Plug.html)  
                  [Eplan.EplApi.DataModel.EObjects.PlugStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip.html)  
                  [Eplan.EplApi.DataModel.EObjects.Shield](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Shield.html)  
                  [Eplan.EplApi.DataModel.EObjects.Terminal](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal.html)  
                  [Eplan.EplApi.DataModel.EObjects.TerminalStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip.html)  
                  [Eplan.EplApi.DataModel.Topology.Segment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Topology.Segment.html)

Syntax

**C#**



public class Function : FunctionBase, IArticleUser, IFunctionBase, IPropertyPlacementsContainer, IWriteProtection

public ref class Function : public FunctionBase, IArticleUser, IFunctionBase, IPropertyPlacementsContainer, IWriteProtection


Remarks

Some properties of Data model classes are not linked with their owners even if from the syntax it may seem otherwise. Like in this line: oRectangle.Pen.ColorId = 5, the ColorId of the Pen is changed but oRectangle object doesn't know about it since the Pen property is a stand alone value not aware of oRectangle object existence. This remark applies to the following Function properties: Articles, Connections.

Example

The following example shows how to create and place Function on page. Next example shows how to build connection between two functions.

**C#**

```


string strSymbolLibName = "IEC_symbol";

string strSymbolName = "M2W";

int nVariant = 0;

//at first initialize SymbolVariant

SymbolLibrary oSymbolLibrary = new SymbolLibrary(m_eplanDemo, strSymbolLibName);

Symbol oSymbol = new Symbol(oSymbolLibrary, strSymbolName);

SymbolVariant oSymbolVariant = new SymbolVariant();

oSymbolVariant.Initialize(oSymbol, nVariant);

//create function

Function oNewFunction = new Function();

oNewFunction.Create(page, oSymbolVariant);

//set function name

oNewFunction.Name = "=AP+ST1-M1";

oNewFunction.VisibleName = "M1";

//set pins descriptions

oNewFunction.Properties.FUNC_CONNECTIONDESIGNATION[1] = "1";

oNewFunction.Properties.FUNC_CONNECTIONDESIGNATION[2] = "2";

oNewFunction.Properties.FUNC_CONNECTIONDESIGNATION[3] = "PE";

//set location

oNewFunction.Location = new PointD(120.0, 215.0);

//adjust representation type

oNewFunction.ManualPlacementType = page.PageType;

```

**C#**

```
Page oPage = m_oTestProject.Pages[9];

string strSymbolLibName = "IEC_symbol";

string strSymbolName = "M3";

int nVariant = 0;

SymbolLibrary oSymbolLibrary = new SymbolLibrary(m_oTestProject, strSymbolLibName);

Symbol oSymbol = new Symbol(oSymbolLibrary, strSymbolName);

SymbolVariant oSymbolVariant = new SymbolVariant();

oSymbolVariant.Initialize(oSymbol, nVariant);

Function oFunction = new Function();

oFunction.Create(oPage, oSymbolVariant);

oFunction.Name = "A";

oFunction.Location = new PointD(100, 100);

Function oFunction2 = new Function();

oFunction2.Create(oPage, oSymbolVariant);

oFunction2.Name = "B";

oFunction2.Location = new PointD(100, 50);

new Generate().Connections(m_oTestProject);

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Function Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~_ctor().html) | Constructor. Creates a transient Function. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AllSubFunctions](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~AllSubFunctions.html) | Returns an array of all sub-functions of the given main function. Sub-functions are all functions having the same identifying device tag (property 20005) which are not main (a.k.a. auxiliary functions). |
| Public Property | [AreConnectionPointPositionsLocal](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~AreConnectionPointPositionsLocal.html) | Determines if connection point data are saved locally at the part placement. |
| Public Property | [AreTargetsSpecifed](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~AreTargetsSpecifed.html) | The value determines if target is taken from net-based routing or not. (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Property | [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~ArticleReference.html) | Sets the ArticleReference at the reference position of the ArticleReference. |
| Public Property | [ArticleReferences](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~ArticleReferences.html) | Returns [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)s that are referenced by Function. |
| Public Property | [Articles](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~Articles.html) | Returns [Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)s that are referenced by Function, and only those that are stored in project database. |
| Public Property | [Block](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~Block.html) | Returns a block which this SymbolReference object is part of. If this object is not a part of any block, this property returns NULL. (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Property | [BmkSearchDirection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~BmkSearchDirection.html) | The property gives the search direction of the full device tag, when the visible device tag name is empty. |
| Public Property | [CanGiveConnDesignationsToOtherFunctions](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~CanGiveConnDesignationsToOtherFunctions.html) | Returns flag, if this function can give connection designations to other functions (is meant for the Device-Tag-Editor, where sometimes there can be edited more connection designations than the actual function has) |
| Public Property | [CanHaveArticleData](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~CanHaveArticleData.html) | Check if the Function can have [Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)s. |
| Public Property | [ConnectionPointPositions](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~ConnectionPointPositions.html) | Array of connection points data. |
| Public Property | [Connections](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~Connections.html) | Returns [Connection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html)s that have the Functions as a start function or end function. |
| Public Property | [ContactImage](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~ContactImage.html) | Returns contact image assign to this function or `null`. |
| Public Property | [ContactImageType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~ContactImageType.html) | Gets or sets a value indicating where contact image is displayed for this function. |
| Public Property | [CrossReferencedObjectsAll](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~CrossReferencedObjectsAll.html) | Returns an array of objects cross-referenced with this object (i.e. having the same name - in case of functions - or otherwise associated) (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [DatabaseIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~DatabaseIdentifier.html) | Returns the project as number. The number is unique for all open projects in one session. The number changes when the project is closed and opened again. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [DrawingOrder](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~DrawingOrder.html) | Sets display sequence. The drawing order flag will be used to sort elements according to drawing order within a group. If elements chare the same value the drawing order will result from order of the data model. Default value is 67. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [FunctionCategory](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~FunctionCategory.html) | Returns the category of a Function. |
| Public Property | [FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~FunctionDefinition.html) | Returns the [FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition.html) of the Function. |
| Public Property | [FunctionTemplates](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~FunctionTemplates.html) | If this object is the main function of a device or a cable, this property returns an array of transient object (of Connection or Function type) that represent function templates contained by the device or the cable. |
| Public Property | [GraphicalConnectionPoints](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~GraphicalConnectionPoints.html) | An array of the symbols's connection points (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Property | [GraphicalConnections](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~GraphicalConnections.html) | An array of [SymbolReference.GraphicalConnection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference+GraphicalConnection.html) objects representing all auto-connecting lines connected to the pins of the symbol. This property may be useful to check graphical layout of connections associated with the symbol (including T-nodes, corners, etc.). (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Property | [Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Group.html) | Returns a group that the Placement object belongs to. If the Placement object doesn't belong to any group, NULL is returned. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [HasDefaultGraphicalTerminalsToConnectionPointsMapping](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~HasDefaultGraphicalTerminalsToConnectionPointsMapping.html) | Determines if connection points to graphical terminals mapping is the default mapping, according to the symbol. Please refer to the line "Symbol connection point" in dialog "Connection point logic" in GUI. This property returns ... true, if all Symbol connection points are mapped to the respective connection point of the Function. false, if the mapping on the Function was changed in regard to the Symbol. |
| Public Property | [HasPolylineAsLogicalArea](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~HasPolylineAsLogicalArea.html) | Returns true if the symbol's logical area is a polyline (consisting of segments) rather than just a rectangle. (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Property | [HasPotentialSeparated](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~HasPotentialSeparated.html) | Gets/Sets, if the function separates potentials. |
| Public Property | [IdentifyingNameParts](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase~IdentifyingNameParts.html) | Returns identifying name of the Function. (Inherited from [Eplan.EplApi.DataModel.FunctionBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase.html)) |
| Public Property | [IsCoveredTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~IsCoveredTemplate.html) | Returns true if this is a Function object that covers a function template in a device. |
| Public Property | [IsFixedDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~IsFixedDevice.html) | Set or checks if device of this function is fixed. |
| Public Property | [IsLocked](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsLocked.html) | Determines if the the StorableObject is locked.  The StorableObject is locked when it was explicitly or implicitly locked. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsMainFunction](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~IsMainFunction.html) | Gets/Sets a flag which indicates a main function of the device. |
| Public Property | [IsNameEmpty](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase~IsNameEmpty.html) | Returns true if the list of name's properties is empty (Inherited from [Eplan.EplApi.DataModel.FunctionBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase.html)) |
| Public Property | [IsNetConnecting](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~IsNetConnecting.html) | Returns, if the function is netconnecting. |
| Public Property | [IsPlaced](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~IsPlaced.html) | Returns true if the placement is placed (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [IsReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsReadOnly.html) | Determines if StorableObject is read-only (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsSetAsVisible](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~IsSetAsVisible.html) | Gets/Sets visibility of the object as set in its properties dialog. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [IsTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~IsTemplate.html) | Returns true if this is a transient Function object repesenting an uncovered function template of a device. |
| Public Property | [IsTemplateReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~IsTemplateReadOnly.html) | Determines whether changes made on this template will be stored after UpdateLocalTemplate is called. |
| Public Property | [IsTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsTransient.html) | Determines if the the StorableObject is transient.  The StorableObject is transient when it was created by default constructor and:  it is a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) and it was not assigned a [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html),  it is a [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) or any class derived from it and was not assigned a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsValid](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsValid.html) | Determines if StorableObject is correct database object and is not deleted. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Location](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase~Location.html) | Get or set the placement's location. (Inherited from [Eplan.EplApi.DataModel.FunctionBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase.html)) |
| Public Property | [LogicalAreaSegments](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~LogicalAreaSegments.html) | Gets/Sets an array of segments that the symbol's logical area may consist of. (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Property | [ManualPlacementType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~ManualPlacementType.html) | Gets custom placement type. Placement type express how function will be shown on scheme. |
| Public Property | [Name](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase~Name.html) | Returns the name of the FunctionBase. (Inherited from [Eplan.EplApi.DataModel.FunctionBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase.html)) |
| Public Property | [NameParts](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase~NameParts.html) | Name of the Function. (Inherited from [Eplan.EplApi.DataModel.FunctionBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase.html)) |
| Public Property | [NestedFunctions](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~NestedFunctions.html) | Returns an array of nested functions of the given main function. Nested-functions property returns functions whose identifying device tag contains the device tag of the parent + nested part of device tag. |
| Public Property | [ObjectIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ObjectIdentifier.html) | Returns the object identifier as number. The number is unique for all objects of this type. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Page.html) | Returns the page the Placement is on, or assigns a Page object to the placement. If the placement was previously assigned to another page, it is removed from old one and assigned to the page given as an argument. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [ParentFunction](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~ParentFunction.html) | Gets parent function (a main function having the same identifying name or, in case of sub-terminals, the main terminal of a multi-level terminal). For main functions it returns NULL. |
| Public Property | [Pins](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~Pins.html) | Gets/Sets an array of the function's connection points. |
| Public Property | [PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~PlanningSegment.html) | [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html) assigned to this function. |
| Public Property | [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Project.html) | Returns the project to which the StorableObject belongs. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Properties](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~Properties.html) | EPLAN properties of the Function object. |
| Public Property | [PropertyPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~PropertyPlacements.html) | Returns [Eplan.EplApi.DataModel.Graphics.PropertyPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement.html)s assigned to the SymbolReference. (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Property | [PropertyPlacementsSchemas](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~PropertyPlacementsSchemas.html) | Returns [SymbolReference.PropertyPlacementsSchemas](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~PropertyPlacementsSchemas.html) assigned to this SymbolReference. (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Property | [SubFunctions](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~SubFunctions.html) | Returns an array of sub-functions of the given main function. Sub-functions are all functions having the same identifying device tag (property 20005) which are not main (a.k.a. auxiliary functions). |
| Public Property | [SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~SymbolVariant.html) | Overridden. Specifies [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) assigned to this SymbolReference. |
| Public Property | [SymbolWiringType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~SymbolWiringType.html) | Set configuration type to select different variants for point or destination wiring (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Property | [Tooltip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Tooltip.html) | Gets the tooltips of the object as can be seen in the GED (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [TypeIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~TypeIdentifier.html) | Returns the type of the object as number. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [UseLocalPropertyPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~UseLocalPropertyPlacements.html) | Return true if the instance uses the local property instances, otherwise it uses the ones of the variant. (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Property | [VisibleName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase~VisibleName.html) | Returns the visible name of the FunctionBase. (Inherited from [Eplan.EplApi.DataModel.FunctionBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase.html)) |
| Public Property | [VisibleNameParts](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase~VisibleNameParts.html) | Returns visible name of the Function. (Inherited from [Eplan.EplApi.DataModel.FunctionBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase.html)) |
| Public Property | [WriteProtected](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~WriteProtected.html) | Check if object is currently write protected or sets Manual write protection |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~AddArticleReference.html) | Overloaded. Adds a new [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html) to the Function. |
| Public Method | [AddConnectionPointPosition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~AddConnectionPointPosition.html) | Creates new connection point position. |
| Public Method | [Assign](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~Assign.html) | Assigns this function to another, which means that values of this function's properties are copied to the target object and the function itself is removed from the project. |
| Public Method | [ConvertToGraphics](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~ConvertToGraphics.html) | Converts the symbol representing this object into a group of graphical placements. (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~CopyTo.html) | Overloaded. Copy Placement and insert the Copy into destination group. Copied placement will be inserted into desired project of destination group. If this placement is temporary, the copy will be persistent, if the destination group is also persistent. Group or Page, where the placement will be inserted. Defines whether a layer should be matched by name.Defines whether user-defined property definitions should be matched by identifying name. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Method | [Create](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~Create.html) | Overloaded. Creates a `Function` object placed on a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) given as a parameter and sets it [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) together with `LogicalArea`. |
| Public Method | [CreateTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~CreateTransient.html) | Overloaded. Creates a Function. It is not placed on any [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). Its category is taken from [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html). |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Dispose().html) | Destructor for deterministic finalization of Function object. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Equals.html) | Operator of comparison implementation. Checks if two StorableObjects refer to the same object in the project. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetBoundingBox](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~GetBoundingBox.html) | Placement bounding box. Bounding box is a rectangle which contain this placement. It can be also used to determine placement size. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Method | [GetGraphics](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~GetGraphics.html) | Gets graphical representation of the Function. |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetHashCode.html) | Serves as the default hash function. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetLogicalArea](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~GetLogicalArea.html) | Returns a rectangle which is the logical area of the object derived from SymbolReference. For objects having symbols consisting of segments, this method returns the bounding box of the polyline created by those segments. (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Method | [GetNamePropertyIdsWithSeparators](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase~GetNamePropertyIdsWithSeparators.html) | Gets name prototype properties id with separators. (Inherited from [Eplan.EplApi.DataModel.FunctionBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase.html)) |
| Public Method | [GetNamePrototype](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase~GetNamePrototype.html) | Sets properties which are used for building name of object. (Inherited from [Eplan.EplApi.DataModel.FunctionBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase.html)) |
| Public Method | [GetPropertyPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~GetPropertyPlacements.html) | Gets list of property placements of given type. (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Method | [GetTypeName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetTypeName.html) | Returns object type name. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetWriteProtectionFlagSet](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~GetWriteProtectionFlagSet.html) | Checks if a specific write protection kind was set. |
| Public Method | [IsDeviceLocked](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~IsDeviceLocked.html) | Determines if the the Device (which can refer to several objects, such as all function's representations) is locked.  The LockDevice is locked when it was explicitly or implicitly locked. |
| Public Method | [IsPointInsideLogicalArea](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~IsPointInsideLogicalArea.html) | Overridden. Checks, if the point is inside logical area of the symbol. Returns true, if the symbol has a logical area and the point is inside. The logical area may be a rectangle or a polyline without arcs. |
| Public Method | [LockDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~LockDevice.html) | Tries to lock current device (which can refer to several objects, such as all function's representations) in database for exclusive access. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. If locked device in placed, corresponding page(s) will be locked as well. |
| Public Method | [LockObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~LockObject().html) | Tries to lock current object in database for exclusive access. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [MakePersistent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~MakePersistent.html) | Instantiates the function represented by this object. Primarily used for instantiating an uncovered function template. |
| Public Method | [PauseWriteProtection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~PauseWriteProtection.html) | Temporarily disables write protection. Note that current write protection flags are not cleared. |
| Public Method | [Place](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~Place.html) | Places the function onto the given page, in the given location |
| Public Method | [PlaceAt](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~PlaceAt.html) | Places the function onto the given page, in the given location and with the symbol specified by the placementType and the pSymbolVariant parameters. |
| Public Method | [PlaceFunctionalMacro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~PlaceFunctionalMacro.html) | Places a macro assigned to this function together with a special symbol configured in settings. The symbol placed has 'Functional' representation type and the macro is converted to graphics after insertion. If no macro is assigned to the function in its article data (ARTICLE\_GROUPSYMBOLMACRO property), the macro specified by the third parameter ('strMacroFileName') will be inserted. |
| Public Method | [Remove](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Remove.html) | Removes placement. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Method | [RemoveArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~RemoveArticleReference.html) | Removes the ArticleReference from the Function |
| Public Method | [RemoveConnectionPointPosition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~RemoveConnectionPointPosition.html) | Removes connection point data stored under given index. |
| Public Method | [RemoveFromPage](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~RemoveFromPage.html) | Removes placement from the page. Object becomes not-placed. |
| Public Method | [ReorderPropertyPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~ReorderPropertyPlacements.html) | Reorders property placements of one type, which are assigned to this SymbolReference. (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Method | [ResetGraphicalTerminalsToConnectionPointsMapping](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~ResetGraphicalTerminalsToConnectionPointsMapping.html) | Resets connection points to graphical terminals mapping. |
| Public Method | [Scale](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Scale.html) | Overloaded. Scales the placement (or group of placements) by the specified factors in X and Y axis with scaling origin point specified by the ptOrigin parameter. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Method | [SetLogicalArea](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~SetLogicalArea.html) | Sets rectangular logical area for objects derived from SymbolReference. (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Method | [SetPlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~SetPlanningSegment.html) | Assigns [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html) to this function. |
| Public Method | [SetSymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~SetSymbolVariant.html) | Sets symbol variant for Function. |
| Public Method | [SmartLock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~SmartLock.html) | Tries to lock current object. If object is [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) - it's page will be locked as well; [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) locks it's installation space; [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) locks all it's connections and connection definition points; [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) locks all placements from this page. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [StoreConnectionPointPosition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~StoreConnectionPointPosition.html) | Stores data from connection point position in function under given index. |
| Public Method | [SwitchLocalPropertyPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~SwitchLocalPropertyPlacements.html) | Copies or removes all local ProperyPlacemnets and sets flag (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Method | [ToStringIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ToStringIdentifier.html) | Returns this object as string identifier. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [UpdateLocalTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~UpdateLocalTemplate.html) | Stores changes into object from which template has been taken. |


