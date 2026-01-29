# Actions

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/API Actions.md

---

This is the list of all official Eplan API actions available for the user

| Name | Description |
| --- | --- |
| [backup](backup.md) | Action class for backup functions. Backs up a project and master data (forms, symbols, ...) to disk |
| [changelayer](changelayer.md) | Changes graphical layer properties. |
| [check](check.md) | Action class for checking functions: check a project and check pages. |
| [CleanWorkspaceAction](CleanWorkspaceAction.md) | Cleans an existing workspace. |
| [compress](compress.md) | Action class to compress projects. |
| [devicelist](devicelist.md) | Action class for device list functions: import, export, and delete device lists. |
| [edit](edit.md) | Action class for edit functions: Opens a project, opens a specific page (identified by the page name), opens a page with a specific device (identified by the device name) or opens a specific page (identified by the page name) and sets the cursor at the X and Y coordinates. |
| [EplApiModuleAction](EplApiModuleAction.md) | Loads and registers an API Add-in. |
| [EsCorrectConnections](EsCorrectConnections.md) | Merges graphical properties (color, line type, layer...) of connection definition points into one signal definition point for each signal, if these graphical properties are equal on the whole signal. |
| [ExecuteScript](ExecuteScript.md) | Runs the given script. |
| [export](export.md) | Action to export pages and projects in graphical, DXF, DWG, PXF format. |
| [export3d](export3d.md) | Action to export installation spaces into 3D formats. |
| [ExportNCData](ExportNCData.md) | Action exports NC Data for machines. |
| [ExportProductionWiring](ExportProductionWiring.md) | Action to export Production Wiring Data for machines according to calling parameters. |
| [ExportSegmentsTemplate](ExportSegmentsTemplate.md) | Action to export segment templates to file. |
| [exportToGraphics](exportToGraphics.md) | Action to export pages and projects to graphical (TIF, GIF, PNG, JPG) format. |
| [gedRedraw](gedRedraw.md) | Action class for GED redraw. |
| [generate](generate.md) | Action class for generate functions: generate connections and generate cables. |
| [generatemacros](generatemacros.md) | Action for generating macros from project. |
| [graphicallayertable](graphicallayertable.md) | Action class for graphical layer table functions: import, export. |
| [import](import.md) | Action for importing projects, macros, and drawings. |
| [import3d](import3d.md) | Action for importing 3d data. |
| [ImportPrePlanningData](ImportPrePlanningData.md) | Action to import pre-planning data. |
| [ImportSegmentsTemplate](ImportSegmentsTemplate.md) | Action to import segment templates from file to project. |
| [InsertModelViewAction](InsertModelViewAction.md) | Action to insert model view object on a page. |
| [label](label.md) | Action class to create labels for projects. |
| [masterdata](masterdata.md) | Action class for operations related to EPLAN master data. |
| [MfExportRibbonBarAction](MfExportRibbonBarAction.md) | Exports main ribbon bar customizing to XML file. |
| [MfImportRibbonBarAction](MfImportRibbonBarAction.md) | Imports main ribbon bar customizing from XML file. |
| [navigateToEEC](navigateToEEC.md) | Action class to navigate to an object in the EPLAN Engineering Configuration. |
| [OpenWorkspaceAction](OpenWorkspaceAction.md) | Opens an existing workspace. |
| [partslist](partslist.md) | Action class for exporting and importing parts and other parts management items like addresses, constructions, terminals, accessory lists and accessory placements. Allows also to delete stored properties. |
| [partsmanagementapi](partsmanagementapi.md) | Action class for exporting and importing parts and other parts management items like addresses, constructions, terminals, accessory lists and accessory placements. |
| [plcservice](plcservice.md) | Exports/imports PLC data using the specified converter. |
| [preparemacros](preparemacros.md) | Action for preparing project for macro generation. |
| [print](print.md) | Action class to print projects and pages. |
| [ProjectAction](ProjectAction.md) | Runs an action upon a given project and closes project afterwards. |
| [projectmanagement](projectmanagement.md) | Action class for project management. |
| [ProjectOpen](ProjectOpen.md) | Opens given project. |
| [RegisterCustomPropertyEditorAction](RegisterCustomPropertyEditorAction.md) | Registers/Unregisters a custom editor dialog for a property ID or identifying name of a user-defined property. |
| [RegisterScript](RegisterScript.md) | Register a script. |
| [renumber](renumber.md) | Action corresponds to numbering functionality. |
| [reports](reports.md) | Action class to update all project evaluations. |
| [restore](restore.md) | Action class for restore functions: restore projects and restore master data (forms, symbols, ...) |
| [SaveWorkspaceAction](SaveWorkspaceAction.md) | Saves the specified workspace. If the workspace already exists, changes are saved. If the workspace does not yet exist, it is created and saved. |
| [search](search.md) | Action class for search operations. Searchs items in a project. |
| [selectionset](selectionset.md) | Action class for selection set functions: get current project, get selected projects, get selected pages. |
| [SetProjectLanguage](SetProjectLanguage.md) | Sets project languages for read-write and read-only projects. |
| [subprojects](subprojects.md) | Action class to export and import subprojects. |
| [SwitchProjectType](SwitchProjectType.md) | Action to change type of project. |
| [synchronize](synchronize.md) | Action class to synchronize project data. |
| [Topology](Topology.md) | Action for topology-related operations. |
| [translate](translate.md) | Action class for translate functions: translate a project, export missing translation list, and remove languages from a project. |
| [UnregisterScript](UnregisterScript.md) | Unregisters a script. |
| [UpdateSegmentsFilling](UpdateSegmentsFilling.md) | Calculates and sets value of property CABLINGSEGMENT\_FILLING for all segments in project. |
| [XAfActionSetting](XAfActionSetting.md) | Sets the value of a setting. |
| [XAfActionSettingProject](XAfActionSettingProject.md) | Sets the value of a project setting. |
| [XAMlExportProductionData2RASCenterAction](XAMlExportProductionData2RASCenterAction.md) | Export of the construction spaces of the selected project in AutomationML format. The generated AutomationML file is intended for import into the Rittal - RiPanel Processing Center, which controls the machines for creating the openings or cutting the mounting rails and wiring channels. |
| [XAMlExportProductionData2SmartMountingAction](XAMlExportProductionData2SmartMountingAction.md) | Export of the construction spaces of the selected project in AutomationML format. The generated AutomationML file is intended for import into the Rittal - RiPanel Processing Center, which controls the machines for creating the openings or cutting the mounting rails and wiring channels. |
| [XCabCalculateEnclosureTotalWeightAction](XCabCalculateEnclosureTotalWeightAction.md) | Calculates the total weight of a cabinet and writes it to the "Total weight" property (#36108 - FUNCTION3D\_CABINET\_TOTALWEIGHT) |
| [XCCreateGravingtextAction](XCCreateGravingtextAction.md) | Generates an engraving text from the DTs of the source and target of the cable. By default, the designation is abbreviated in accordance with the VASS standard (Volkswagen Audi Seat Skoda), i.e., structure identifiers having the same name of source and target are removed - starting from the left. |
| [XCMRemoveUnnecessaryNDPsAction](XCMRemoveUnnecessaryNDPsAction.md) | Removes unnecessary net definition points of active project. |
| [XCMUniteNetDefinitionPointsAction](XCMUniteNetDefinitionPointsAction.md) | Unites net definition points placed on the same net in active project. |
| [XDLInsertDeviceAction](XDLInsertDeviceAction.md) | Starts interaction for inserting a device. |
| [XEGActionInsertSymRef](XEGActionInsertSymRef.md) | Standard action to find symbol references for inserting. |
| [XEsGetPagePropertyAction](XEsGetPagePropertyAction.md) | Gets a special property of first selected page. |
| [XEsGetProjectPropertyAction](XEsGetProjectPropertyAction.md) | Gets a special property of the current project. |
| [XEsGetPropertyAction](XEsGetPropertyAction.md) | Gets selected objects and gets the property. |
| [XEsSetPagePropertyAction](XEsSetPagePropertyAction.md) | Sets a special property of selected pages. |
| [XEsSetProjectPropertyAction](XEsSetProjectPropertyAction.md) | Sets a special property of a current project. |
| [XEsSetPropertyAction](XEsSetPropertyAction.md) | Gets selected objects and sets the property. |
| [XEsUserPropertiesExportAction](XEsUserPropertiesExportAction.md) | Exports user properties to file. |
| [XEsUserPropertiesImportAction](XEsUserPropertiesImportAction.md) | Imports user properties to project from file. |
| [XGedClosePage](XGedClosePage.md) | Closes all selected pages. |
| [XGedStartInteractionAction](XGedStartInteractionAction.md) | Starts an interaction of the graphical editor. |
| [XGedUpdateMacroAction](XGedUpdateMacroAction.md) | Updates macros. It can be passed the full path of a project. When project is not opened, this action opens it and closes it automatically. |
| [XMActionDCCommonExport](XMActionDCCommonExport.md) | Starts the export for the external editing. |
| [XMActionDCImport](XMActionDCImport.md) | Imports a data configuration file into an existing EPLAN project. |
| [XMDeleteReprTypeAction](XMDeleteReprTypeAction.md) | Removes a representation type from selected macros and what is stored in a selected directory. |
| [XMExportConnectionsAction](XMExportConnectionsAction.md) | Action class to export connections of a project. |
| [XMExportDCArticleDataAction](XMExportDCArticleDataAction.md) | Starts the export for the external editing. |
| [XMExportFunctionAction](XMExportFunctionAction.md) | Action class to export functions of a project. |
| [XMExportLocationBoxesAction](XMExportLocationBoxesAction.md) | Action class to export location boxes of a project. |
| [XMExportPagesAction](XMExportPagesAction.md) | Action class to export pages of a project. |
| [XMExportPipeLineDefsAction](XMExportPipeLineDefsAction.md) | Action class to export pipeline definitions of a project. |
| [XMExportPotentialDefsAction](XMExportPotentialDefsAction.md) | Action class to export potential definitions of a project. |
| [XMImportDCArticleDataAction](XMImportDCArticleDataAction.md) | Imports a data configuration file into an existing EPLAN article database. |
| [XPamConvertPartDatabaseToArticleDatabaseAction](XPamConvertPartDatabaseToArticleDatabaseAction.md) | Converts parts databases from EPLAN Version V2.9 to Version V2022. |
| [XPamsDeviceSelectionAction](XPamsDeviceSelectionAction.md) | Selects device or updates device information. This object can be a project/function/connection. |
| [XPamSelectPart](XPamSelectPart.md) | Starts the part selection (using the configured database). |
| [XPartsSetDataSourceAction](XPartsSetDataSourceAction.md) | Changes the setting responsible for parts management database type. |
| [XPlaUpdateDetailAction](XPlaUpdateDetailAction.md) | The detail engineering is updated for the selected planning objects |
| [XPrjActionUpgradeProjects](XPrjActionUpgradeProjects.md) | This action upgrades one ore more projects to the actual database scheme version. |
| [XPrjConvertBaseProjectsAction](XPrjConvertBaseProjectsAction.md) | This action converts one ore more old basic projects (\*.ept and \*.epb files) to new basic projects (\*.zw9). All basic projects in a folder are upgraded (recursively). |
| [XSDPreviewAction](XSDPreviewAction.md) | Opens or closes the preview of a project page or macro |
| [XSettingsExport](XSettingsExport.md) | Exports settings to an XML file. |
| [XSettingsImport](XSettingsImport.md) | Imports project-, station-, company- or user settings from an XML file. |
| [XSettingsRegisterAction](XSettingsRegisterAction.md) | Registers Add-ons. |
| [XSettingsUnregisterAction](XSettingsUnregisterAction.md) | Unregistration of Add-ons. |