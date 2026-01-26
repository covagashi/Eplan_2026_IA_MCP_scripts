# DMObjectsFinder

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder.html

---

This class allows you to search the [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html). It defines a set of methods for retrieving different API objects. If you want the result objects to match one or more conditions, you should use filters.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.DataModel.DMObjectsFinder**

Syntax

**C#**



public class DMObjectsFinder

public ref class DMObjectsFinder


Remarks

List of Function3D classes with their corresponding FunctionCategories:  
[Area](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Area.html) - AreaDefinition  
[BusBar](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.BusBar.html) - CabMechBusBar  
[Duct](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Duct.html) - CabMechConduit  
[MountingRail](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.MountingRail.html) - CabMechBodyAccessoryInside  
[BusBarSystem](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.BusBarSystem.html) - CabVirtBusbarsystem  
[Cabinet](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Cabinet.html) - CabMechCabinet  
[Component](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Component.html) - ArticlePlacement, CabMechHousing, CabMechSystemAccessory  
[CopperBundle](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.CopperBundle.html) - CabVirtCopperbundle  
[Drilling](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling.html) - CabVirtNC  
[InstallationSpace](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.InstallationSpace.html) - AreaDefinition  
[MountingPanel](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.MountingPanel.html) - CabMechHousing  
[RoutingAccessory](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.RoutingAccessory.html) - CabMechRoutingAccessory  
[RoutingSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.RoutingSegment.html) - Routing  
[RoutingSpline](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.RoutingSpline.html) - Routing

Example

The following example shows how to search a project using the DMObjectsFinder class and how to filter your search results:

**C#**

```


Project myProject = m_oProject; // A valid project

Page myPage = myProject.Pages[0]; // A valid Page object

DMObjectsFinder objFinder = new DMObjectsFinder(myProject);

// Get all functions in the myProject Project

Function[] functions = objFinder.GetFunctions(null);

// Use a filter to get only functions with category 'Motor'

FunctionsFilter myFunctionsFilter = new FunctionsFilter();

myFunctionsFilter.FunctionCategory = Eplan.EplApi.Base.Enums.FunctionCategory.Motor;

myFunctionsFilter.Page = myPage;

// Place all functions with category 'Motor' on page myPage

functions = objFinder.GetFunctions(myFunctionsFilter);

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [DMObjectsFinder Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~_ctor.html) | Overloaded. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~Dispose().html) | Destructor |
| Public Method | [GetAll<T>](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetAll.html) |  |
| Public Method | [GetArticleReferences](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetArticleReferences.html) | Returns [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)s matching given filter. |
| Public Method | [GetArticleReferencesWithCF](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetArticleReferencesWithCF.html) | Returns [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)s matching given filter. |
| Public Method | [GetArticleReferencesWithFilterScheme](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetArticleReferencesWithFilterScheme.html) | Returns [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)s matching given filter from bill of materials-navigator. |
| Public Method | [GetBoxedDevices](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetBoxedDevices.html) | Returns [BoxedDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BoxedDevice.html)s matching given filter. |
| Public Method | [GetBoxedDevicesWithCF](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetBoxedDevicesWithCF.html) | Returns [BoxedDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BoxedDevice.html)s matching given filter. |
| Public Method | [GetCablesWithFilterScheme](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetCablesWithFilterScheme.html) | Returns [Eplan.EplApi.DataModel.EObjects.Cable](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Cable.html)s and shieldings ([Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s with category Shielding) matching given filter from cables-navigator. |
| Public Method | [GetCableUnits](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetCableUnits.html) | Returns [Eplan.EplApi.DataModel.EObjects.CableUnit](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.CableUnit.html)es matching given filter. |
| Public Method | [GetCableUnitsWithCF](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetCableUnitsWithCF.html) | Returns [Eplan.EplApi.DataModel.EObjects.CableUnit](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.CableUnit.html)es matching given filter. |
| Public Method | [GetCableUnitsWithFilterScheme](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetCableUnitsWithFilterScheme.html) | Returns [Eplan.EplApi.DataModel.EObjects.CableUnit](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.CableUnit.html)es matching given filter from wire harness navigator. |
| Public Method | [GetConnections](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetConnections.html) | Returns [Connection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html)s matching given filter. If null parameter is passed, all the project's connection objects are returned. Note: In case no filter used, number of objects returned may be bigger than the number of connections visible in the GUI's connection navigator. The GUI's connection navigator by default shows connections of the following placement types only: - Circuit - CircuitSingleLine - Overview - PairCrossReference - ProcessAndInstrumentationDiagram - PanelLayout |
| Public Method | [GetConnectionsWithCF](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetConnectionsWithCF.html) | Returns [Connection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html)s matching given filter. |
| Public Method | [GetConnectionsWithFilterScheme](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetConnectionsWithFilterScheme.html) | Returns [Connection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html)s matching given filter from connections-navigator. |
| Public Method | [GetCustomMateEntries](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetCustomMateEntries.html) | Returns user defined [Eplan.EplApi.DataModel.E3D.MateEntry](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.MateEntry.html)s of all project [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)s matching given filter. |
| Public Method | [GetFunctions](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetFunctions.html) | Overloaded. Returns [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s matching given filter. If "bWithConnectionDefinitionPoints" is true, returns [ConnectionDefinitionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint.html)s matching given filter, too. |
| Public Method | [GetFunctions3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetFunctions3D.html) | Returns [Eplan.EplApi.DataModel.E3D.Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)s matching given filter. |
| Public Method | [GetFunctionsWithCF](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetFunctionsWithCF.html) | Returns [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s matching given custom filter. |
| Public Method | [GetFunctionsWithFilterScheme](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetFunctionsWithFilterScheme.html) | Returns [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) matching given filter from devices-navigator. |
| Public Method | [GetHarnesses](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetHarnesses.html) | Returns [Eplan.EplApi.DataModel.EObjects.Harness](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Harness.html)es matching given filter. |
| Public Method | [GetHarnessesWithCF](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetHarnessesWithCF.html) | Returns [Eplan.EplApi.DataModel.EObjects.Harness](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Harness.html)es matching given filter. |
| Public Method | [GetHarnessesWithFilterScheme](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetHarnessesWithFilterScheme.html) | Returns [Eplan.EplApi.DataModel.EObjects.Harness](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Harness.html)es matching given filter from wire harness navigator. |
| Public Method | [GetInterruptionPoints](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetInterruptionPoints.html) | Returns [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s matching given filter. |
| Public Method | [GetInterruptionPointsWithCF](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetInterruptionPointsWithCF.html) | Returns [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s matching given custom filter. |
| Public Method | [GetInterruptionPointsWithFilterScheme](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetInterruptionPointsWithFilterScheme.html) | Returns [InterruptionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPoint.html)s matching given filter from interruptionpoints-navigator. |
| Public Method | [GetNetDefinitionPoints](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetNetDefinitionPoints.html) | This function takes objects of class [NetDefinitionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.NetDefinitionPoint.html) and filters them with the given filter. |
| Public Method | [GetObjectsFromNavigatorList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetObjectsFromNavigatorList.html) | Returns all items from the list tab of a navigator. |
| Public Method | [GetOptionObjectsWithFilterScheme](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetOptionObjectsWithFilterScheme.html) | Returns [Option](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Option.html)s matching given filter from project-options-navigator. |
| Public Method | [GetPages](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPages.html) | Returns [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html)s matching given filter. |
| Public Method | [GetPagesWithCF](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPagesWithCF.html) | Returns [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html)s matching given filter. |
| Public Method | [GetPagesWithFilterScheme](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPagesWithFilterScheme.html) | \Returns [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html)s matching given filter from pages-navigator(user settings) or if such doesn't exist filter with use of project settings is created. There can be different results when using page filter now and in 1.9 version. For further information please look in P8 help chapter concerning page filter. |
| Public Method | [GetPlaceHolders3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPlaceHolders3D.html) | Returns all [Eplan.EplApi.DataModel.E3D.PlaceHolder3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlaceHolder3D.html) from project. |
| Public Method | [GetPlaceholdersWithFilterScheme](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPlaceholdersWithFilterScheme.html) | Returns [Eplan.EplApi.DataModel.Graphics.PlaceHolder](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder.html)s matching given filter from placeholders-navigator. |
| Public Method | [GetPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPlacements.html) | This function takes objects of classes Placement and inherited from Placement except [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) and filters them with the given filter. This method does not return embedded objects (like for example [Eplan.EplApi.DataModel.Graphics.Shielding](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Shielding.html)). This method does not return [Eplan.EplApi.DataModel.Graphics.PropertyPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement.html). |
| Public Method | [GetPlacements3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPlacements3D.html) | Returns [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)s matching given filter. This method does not return [Eplan.EplApi.DataModel.E3D.MateEntry](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.MateEntry.html)s. |
| Public Method | [GetPlacementsWithCF](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPlacementsWithCF.html) | Returns all objects of classes Placement and inherited from Placement, except [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html), which matches to given filter. |
| Public Method | [GetPlanningSegments](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPlanningSegments.html) | Returns [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html) matching the given filter. |
| Public Method | [GetPlanningSegmentsWithFilterScheme](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPlanningSegmentsWithFilterScheme.html) | Returns [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html) matching the given filter. |
| Public Method | [GetPLCs](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPLCs.html) | Returns [Eplan.EplApi.DataModel.EObjects.PLC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PLC.html)s matching given filter. |
| Public Method | [GetPLCsWithCF](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPLCsWithCF.html) | Returns [Eplan.EplApi.DataModel.EObjects.PLC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PLC.html)s matching given filter. |
| Public Method | [GetPLCsWithFilterScheme](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPLCsWithFilterScheme.html) | Returns [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s matching given filter from plc-navigator. |
| Public Method | [GetPLCTerminalsWithFilterScheme](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPLCTerminalsWithFilterScheme.html) | Returns [Eplan.EplApi.DataModel.EObjects.Terminal](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal.html) matching the given filter from PLC navigator. |
| Public Method | [GetPlugs](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPlugs.html) | Returns [Eplan.EplApi.DataModel.EObjects.Plug](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Plug.html)s matching given filter. |
| Public Method | [GetPlugStrips](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPlugStrips.html) | Returns [Eplan.EplApi.DataModel.EObjects.PlugStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip.html)s matching given filter. |
| Public Method | [GetPlugStripsWithCF](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPlugStripsWithCF.html) | Returns [Eplan.EplApi.DataModel.EObjects.PlugStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip.html)s matching given filter. |
| Public Method | [GetPlugStripsWithFilterScheme](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPlugStripsWithFilterScheme.html) | Returns [Eplan.EplApi.DataModel.EObjects.PlugStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip.html)s matching given filter from plugs-navigator. |
| Public Method | [GetPlugsWithCF](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPlugsWithCF.html) | Returns [Eplan.EplApi.DataModel.EObjects.Plug](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Plug.html)s matching given filter. |
| Public Method | [GetPlugsWithFilterScheme](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPlugsWithFilterScheme.html) | Returns [Eplan.EplApi.DataModel.EObjects.Plug](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Plug.html)s matching given filter from plugs-navigator. |
| Public Method | [GetPotentialDefinitionsWithFilterScheme](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPotentialDefinitionsWithFilterScheme.html) | Returns [PotentialDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinition.html)s matching given filter from potentials-navigator. |
| Public Method | [GetSegmentDefinitions](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetSegmentDefinitions.html) | Returns [Eplan.EplApi.DataModel.Planning.SegmentDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinition.html) matching the given filter. |
| Public Method | [GetSegmentPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetSegmentPlacements.html) | Returns [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html) matching the given filter. |
| Public Method | [GetSegmentTemplates](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetSegmentTemplates.html) | Returns [Eplan.EplApi.DataModel.Planning.SegmentTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplate.html) matching the given filter. |
| Public Method | [GetSegmentTemplatesWithFilterScheme](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetSegmentTemplatesWithFilterScheme.html) | Returns [Eplan.EplApi.DataModel.Planning.SegmentTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplate.html) matching the given filter. |
| Public Method | [GetStorableObjects](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetStorableObjects.html) | Overloaded. This function takes all objects of classes StorableObject and inherited from StorableObject except [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) and filters them with the given filter. This method does not return [Eplan.EplApi.DataModel.Graphics.PropertyPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement.html) and [Eplan.EplApi.DataModel.MasterData.Symbol](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Symbol.html). |
| Public Method | [GetStorableObjectsWithCF](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetStorableObjectsWithCF.html) | Returns all objects of classes StorableObject and inherited from StorableObject, except [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html), which matches to given filter. |
| Public Method | [GetSymbolsWithFilterScheme](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetSymbolsWithFilterScheme.html) | Returns [Eplan.EplApi.DataModel.MasterData.Symbol](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Symbol.html)s matching given filter from symbols-navigator. |
| Public Method | [GetTerminals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetTerminals.html) | Returns [Eplan.EplApi.DataModel.EObjects.Terminal](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal.html) matching given filter. |
| Public Method | [GetTerminalStrips](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetTerminalStrips.html) | Returns [Eplan.EplApi.DataModel.EObjects.TerminalStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip.html)s matching given filter. |
| Public Method | [GetTerminalStripsWithCF](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetTerminalStripsWithCF.html) | Returns [Eplan.EplApi.DataModel.EObjects.TerminalStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip.html)s matching given filter. |
| Public Method | [GetTerminalStripsWithFilterScheme](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetTerminalStripsWithFilterScheme.html) | Returns [Eplan.EplApi.DataModel.EObjects.TerminalStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip.html) matching given filter from terminals-navigator. |
| Public Method | [GetTerminalsWithCF](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetTerminalsWithCF.html) | Returns [Eplan.EplApi.DataModel.EObjects.Terminal](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal.html)s matching given filter. |
| Public Method | [GetTerminalsWithFilterScheme](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetTerminalsWithFilterScheme.html) | Returns [Eplan.EplApi.DataModel.EObjects.Terminal](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal.html) matching given filter from the terminals navigator. |
| Public Method | [Initialize](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~Initialize.html) | Sets the project used. The same as project parameter in the constructor. Used when accessing API registered as COM. |


