# EPLAN Action Validation Report

Checked **86** unique EPLAN actions against the official docs RAG (`https://rag2026.covaga.xyz/search`).

- OK: 47
- Action found but some parameter names not in the doc page: 37
- Action NOT found in docs: 2
- Request errors: 0

| Status | Action | Wrapper(s) | Detail |
|--------|--------|------------|--------|
| NOT FOUND | `ProjectOpen` | `project.open_project` | no doc page mentions this action (undocumented internal action or index gap) |
| NOT FOUND | `XPrjActionProjectClose` | `project.close_project` | no doc page mentions this action (undocumented internal action or index gap) |
| WARN | `ExportNCData` | `production.export_nc_data` | params not seen in docs: ['EXPORTFILE'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/ExportNCData.html) |
| WARN | `ExportProductionWiring` | `production.export_production_wiring` | params not seen in docs: ['EXPORTFILE'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/ExportProductionWiring.html) |
| WARN | `ExportSegmentsTemplate` | `cabinet.export_segments_template` | params not seen in docs: ['EXPORTFILE'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/ExportSegmentsTemplate.html) |
| WARN | `ImportPrePlanningData` | `cabinet.import_preplanning_data` | params not seen in docs: ['IMPORTFILE'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/ImportPrePlanningData.html) |
| WARN | `ImportSegmentsTemplate` | `cabinet.import_segments_template` | params not seen in docs: ['IMPORTFILE'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/ImportSegmentsTemplate.html) |
| WARN | `SetProjectLanguage` | `project.set_project_language` | params not seen in docs: ['READWRITE'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/SetProjectLanguage.html) |
| WARN | `XEsUserPropertiesExportAction` | `properties.export_user_properties` | params not seen in docs: ['EXPORTFILE', 'PROJECTNAME'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XEsUserPropertiesExportAction.html) |
| WARN | `XEsUserPropertiesImportAction` | `properties.import_user_properties` | params not seen in docs: ['IMPORTFILE', 'PROJECTNAME'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XEsUserPropertiesImportAction.html) |
| WARN | `XMActionDCCommonExport` | `data_exchange.dc_export` | params not seen in docs: ['DESTINATION', 'EXECUTIONMODE', 'IMMEDIATEIMPORT'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XMActionDCCommonExport.html) |
| WARN | `XMDeleteReprTypeAction` | `data_exchange.delete_representation_type` | params not seen in docs: ['PROJECTNAME'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XMDeleteReprTypeAction.html) |
| WARN | `XMExportConnectionsAction` | `data_exchange.export_connections` | params not seen in docs: ['Destination', 'ExecutionMode', 'ImmediateImport', 'IncludeGraphicalConnections'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XMExportConnectionsAction.html) |
| WARN | `XMExportFunctionAction` | `data_exchange.export_functions` | params not seen in docs: ['Destination', 'ExecutionMode', 'ImmediateImport'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XMExportFunctionAction.html) |
| WARN | `XMExportLocationBoxesAction` | `data_exchange.export_location_boxes` | params not seen in docs: ['Destination', 'ExecutionMode', 'ImmediateImport'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XMExportLocationBoxesAction.html) |
| WARN | `XMExportPagesAction` | `data_exchange.export_pages` | params not seen in docs: ['Destination', 'ExecutionMode', 'ImmediateImport'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XMExportPagesAction.html) |
| WARN | `XMExportPipeLineDefsAction` | `data_exchange.export_pipeline_definitions` | params not seen in docs: ['Destination', 'ExecutionMode', 'ImmediateImport'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XMExportPipeLineDefsAction.html) |
| WARN | `XMExportPotentialDefsAction` | `data_exchange.export_potential_definitions` | params not seen in docs: ['Destination', 'ExecutionMode', 'ImmediateImport'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XMExportPotentialDefsAction.html) |
| WARN | `XMImportDCArticleDataAction` | `data_exchange.import_dc_article_data` | params not seen in docs: ['IMPORTFILE', 'PROJECTNAME'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XMImportDCArticleDataAction.html) |
| WARN | `XPartsSetDataSourceAction` | `parts.set_parts_data_source` | params not seen in docs: ['DATASOURCE'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XPartsSetDataSourceAction.html) |
| WARN | `backup` | `backup.backup_project, backup.backup_masterdata` | params not seen in docs: ['AUTOCOPYREFDATA', 'INCLEXTDOCS', 'INCLIMAGES'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/backup.html) |
| WARN | `check` | `verify.check_project, verify.check_pages, verify.check_parts` | params not seen in docs: ['VERIFYCOMPLETEDONLY'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/check.html) |
| WARN | `devicelist` | `devicelist.export_device_list, devicelist.import_device_list, devicelist.delete_device_list` | params not seen in docs: ['FORMAT'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/devicelist.html) |
| WARN | `edit` | `navigation.edit_open_page, navigation.edit_goto_device, navigation.edit_open_layout_space` | params not seen in docs: ['INSTALLATIONSPACE'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/edit.html) |
| WARN | `export` | `export_.export_pdf_project, export_.export_pdf_pages, export_.export_dxf_project, export_.export_dxf_pages, export_.export_dwg_project, export_.export_dwg_pages, export_.export_dxfdwg_project_scheme, export_.export_dxfdwg_pages_scheme, export_.export_graphics_project, export_.export_graphics_pages, export_.export_pxf_project` | params not seen in docs: ['BLACKWHITE', 'COLORDEPTH', 'DESTINATIONPATH', 'EXPORTSCHEME', 'IMAGECOMPRESSION', 'IMAGEWIDTH', 'TARGET'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/API) |
| WARN | `export3d` | `export_.export_3d` | params not seen in docs: ['INSTALLATIONSPACE'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/export3d.html) |
| WARN | `generate` | `generate.generate_connections, generate.generate_cables` | params not seen in docs: ['AUTOSELECTSCHEME', 'KEEPOLDNAMES', 'STARTVALUE', 'STEPVALUE'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/generate.html) |
| WARN | `generatemacros` | `macros.generate_macros` | params not seen in docs: ['DESTINATIONPATH', 'SCHEME'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/generatemacros.html) |
| WARN | `import` | `import_.import_pxf_project, import_.import_dwg_page, import_.import_dxf_page, import_.import_dxfdwg_files, import_.import_pdf_comments` | params not seen in docs: ['BALANCEARTICLES', 'CODEPAGE', 'DESTINATIONPATH', 'GENERATEAUTOMATICCABLES', 'IMPORTSCHEME', 'MACROPROJECT', 'ONLYMACROPROJECT', 'PAGENAME', 'SOURCEPATH', 'VERIFY', 'XOFFSET', 'XSCALE', 'YOFFSET', 'YSCALE'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService3D~Import.html) |
| WARN | `import3d` | `import_.import_3d` | params not seen in docs: ['IMPORTSCHEME'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/import3d.html) |
| WARN | `masterdata` | `data_exchange.masterdata_operation` | params not seen in docs: ['DESTINATIONPATH', 'SOURCEPATH'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/masterdata.html) |
| WARN | `partslist` | `parts.export_parts_list, parts.import_parts_list` | params not seen in docs: ['EXPORTFILE', 'FORMAT', 'IMPORTFILE'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/partslist.html) |
| WARN | `plcservice` | `plc.plc_export, plc.plc_import` | params not seen in docs: ['DESTINATIONFILE', 'OVERWRITE', 'SOURCEFILE'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/plcservice.html) |
| WARN | `print` | `print_.print_project, print_.print_pages` | params not seen in docs: ['PRINTCHANGEDPAGES'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/print.html) |
| WARN | `projectmanagement` | `project.project_management` | params not seen in docs: ['FILENAME', 'OVERWRITE', 'SCHEME'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/projectmanagement.html) |
| WARN | `renumber` | `renumber.renumber_devices, renumber.renumber_pages, renumber.renumber_cables, renumber.renumber_terminals, renumber.renumber_connections` | params not seen in docs: ['EXTENT', 'FILLGAPS', 'FILTERSCHEME', 'PERMITSORTCHANGE'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/renumber.html) |
| WARN | `search` | `search.search_devices, search.search_text, search.search_all_properties, search.search_page_data, search.search_project_data` | params not seen in docs: ['EVALUATIONPAGES', 'FILTERSCHEME', 'GRAPHICPAGES', 'LOGICPAGES', 'NOTPLACEDFUNCTIONS', 'WHOLETEXT'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/search.html) |
| WARN | `subprojects` | `data_exchange.export_subproject, data_exchange.import_subproject` | params not seen in docs: ['SUBPROJECTDIR'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/subprojects.html) |
| WARN | `translate` | `translate.translate_project, translate.export_missing_translations, translate.remove_language` | params not seen in docs: ['EXPORTFILE'] [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/translate.html) |
| OK | `CleanWorkspaceAction` | `workspace.clean_workspace` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/CleanWorkspaceAction.html) |
| OK | `EplApiModuleAction` | `addons.load_api_module` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/EplApiModuleAction.html) |
| OK | `EsCorrectConnections` | `data_exchange.correct_connections` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/EsCorrectConnections.html) |
| OK | `ExecuteScript` | `scripts.execute_script` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/ExecuteScript.html) |
| OK | `MfExportRibbonBarAction` | `ribbon.export_ribbon_bar` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/MfExportRibbonBarAction.html) |
| OK | `MfImportRibbonBarAction` | `ribbon.import_ribbon_bar` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/MfImportRibbonBarAction.html) |
| OK | `OpenWorkspaceAction` | `workspace.open_workspace` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/OpenWorkspaceAction.html) |
| OK | `RegisterScript` | `scripts.register_script` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/RegisterScript.html) |
| OK | `SaveWorkspaceAction` | `workspace.save_workspace` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/SaveWorkspaceAction.html) |
| OK | `SwitchProjectType` | `project.switch_project_type` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/SwitchProjectType.html) |
| OK | `Topology` | `cabinet.topology_operation` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/Topology.html) |
| OK | `UnregisterScript` | `scripts.unregister_script` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/UnregisterScript.html) |
| OK | `UpdateSegmentsFilling` | `cabinet.update_segments_filling` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/UpdateSegmentsFilling.html) |
| OK | `XAfActionSetting` | `settings.set_setting` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XAfActionSetting.html) |
| OK | `XAfActionSettingProject` | `settings.set_project_setting` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XAfActionSettingProject.html) |
| OK | `XCMRemoveUnnecessaryNDPsAction` | `data_exchange.remove_unnecessary_ndps` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XCMRemoveUnnecessaryNDPsAction.html) |
| OK | `XCMUniteNetDefinitionPointsAction` | `data_exchange.unite_net_definition_points` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XCMUniteNetDefinitionPointsAction.html) |
| OK | `XCabCalculateEnclosureTotalWeightAction` | `cabinet.calculate_cabinet_weight` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XCabCalculateEnclosureTotalWeightAction.html) |
| OK | `XEsGetPagePropertyAction` | `properties.get_page_property` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XEsGetPagePropertyAction.html) |
| OK | `XEsGetProjectPropertyAction` | `properties.get_project_property` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XEsGetProjectPropertyAction.html) |
| OK | `XEsGetPropertyAction` | `properties.get_property` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XEsGetPropertyAction.html) |
| OK | `XEsSetPagePropertyAction` | `properties.set_page_property` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XEsSetPagePropertyAction.html) |
| OK | `XEsSetProjectPropertyAction` | `properties.set_project_property` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XEsSetProjectPropertyAction.html) |
| OK | `XEsSetPropertyAction` | `properties.set_property` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XEsSetPropertyAction.html) |
| OK | `XGedClosePage` | `navigation.close_pages` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XGedClosePage.html) |
| OK | `XGedUpdateMacroAction` | `macros.update_macros` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XGedUpdateMacroAction.html) |
| OK | `XMActionDCImport` | `data_exchange.dc_import` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XMActionDCImport.html) |
| OK | `XMExportDCArticleDataAction` | `data_exchange.export_dc_article_data` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XMExportDCArticleDataAction.html) |
| OK | `XPamSelectPart` | `parts.select_part` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XPamSelectPart.html) |
| OK | `XPrjActionUpgradeProjects` | `project.upgrade_projects` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XPrjActionUpgradeProjects.html) |
| OK | `XSDPreviewAction` | `navigation.preview_page` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XSDPreviewAction.html) |
| OK | `XSettingsExport` | `settings.export_settings` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XSettingsExport.html) |
| OK | `XSettingsImport` | `settings.import_settings` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XSettingsImport.html) |
| OK | `XSettingsRegisterAction` | `addons.register_addon` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/API) |
| OK | `XSettingsUnregisterAction` | `addons.unregister_addon` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/XSettingsUnregisterAction.html) |
| OK | `changelayer` | `layers.change_layer` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/changelayer.html) |
| OK | `compress` | `project.compress_project` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/compress.html) |
| OK | `gedRedraw` | `navigation.redraw_ged` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/gedRedraw.html) |
| OK | `graphicallayertable` | `layers.export_graphical_layer_table, layers.import_graphical_layer_table` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/graphicallayertable.html) |
| OK | `label` | `labels.create_labels` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/label.html) |
| OK | `navigateToEEC` | `navigation.navigate_to_eec` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/navigateToEEC.html) |
| OK | `partsmanagementapi` | `partsmanagement.partsmanagement_export, partsmanagement.partsmanagement_import, partsmanagement.partsmanagement_export_by_properties, partsmanagement.partsmanagement_export_all` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/partsmanagementapi.html) |
| OK | `preparemacros` | `macros.prepare_macros` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/preparemacros.html) |
| OK | `reports` | `reports.update_reports, reports.update_model_view_pages, reports.create_model_views, reports.create_copper_unfolds, reports.create_drilling_views` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/reports.html) |
| OK | `restore` | `backup.restore_project, backup.restore_masterdata` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/restore.html) |
| OK | `selectionset` | `navigation.get_selected_pages, project.get_current_project` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/selectionset.html) |
| OK | `synchronize` | `project.synchronize_project` | [doc](https://www.eplan.help/en-us/Infoportal/Content/api/2026/synchronize.html) |
