---
title: "Modules: Overview"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/main_k_modules.htm"
file: "main_k_modules"
category: "main"
---

# Modules: Overview

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Modules: Overview The modular structure makes it possible to determine the scope of service yourself. Module | Submodule | Description  
---|---|---  
BASIC |  |  The BASE module is equivalent to a fully operational EEC that allows you to create object-oriented models. Because the models are object-oriented, it is possible to formally describe complex systems and their versions and configuration rules. Key features of the BASE module:
     * Development.
     * Create libraries.
     * Define architectures (e.g., hierarchical levels of plants).
     * Create library components.
     * Define formulas (rules).
     * Create Form-UIs, i.e., specific user interfaces for different user groups (project engineers, sales employees, etc.).
     * Configuration (for test purposes).
     * Manage projects.
     * Configuration and parameterization of projects using standard editors.  
Configuration with Form-UIs.
See [Terminology](eecbase_k_terminology.htm)  
Note:  
Configuration licenses are required to put the EEC into productive service.  
TEXT |  The TEXT module makes it possible to create any text-based documents on the base of a model. Possible uses include the generation of:
     * Text files (parts lists, ini files, error text files, etc.)
     * HTML files (documentation, etc.)
     * XML files (Word, Excel, or PowerPoint files).
The TEXT module does not have interfaces to existing systems. Rather, it is restricted to generating text documents as well as entire folder structures based on freely defined rules. The TEXT module cannot be deeply integrated into other system; however, it does allow data to be exchanged, something which is fully adequate in many cases, on the basis of exported text documents that can then be imported by a downstream system. See [TEXT](eectext_k_text.htm)  
FORM-UI |  The FORM-UI module is an editor that allows the configuration and the execution of actions on the basis of interactive pages, similar to HTML pages. See [Form-UI](refformui_r_formui.htm)  
GRAPH2D |  The GRAPH2D module is a generic graphic editor used to define form-specific diagrams, e.g., layout diagrams, Gantt diagrams, block diagrams, CFC editors, state graphs, etc. See [ GRAPH2D](eecgraph2d_k_graph2d.htm)  
PLC | STEP 7 |  The PLC.STEP 7 module makes it possible to create PLC software for SIMATIC STEP 7 from Siemens. See [PLC](eecplc_k_plc.htm)  
CODESYS |  The PLC.CODESYS module makes it possible to create PLC software for 3Sâs CoDeSys PLC programming system. See [PLC](eecplc_k_plc.htm)  
AUTOMATIONWORX |  The PLC.AUTOMATIONWORX module makes it possible to create PLC software for Phoenixâs AutomationWorX. See [PLC](eecplc_k_plc.htm)  
ECAD | P8 / Fluid |  The ECAD.P8 module makes it possible to create schematics for Eplan Electric P8. See [ECAD](eececad_k_ecad.htm)  
ECAD3D | Pro Panel |  The ECAD3D.Pro Panel module makes it possible to create three-dimensional mounting layouts. See [Eplan Pro Panel](eecpropanel_k_propanel_requirements.htm)  
OFFICE | WORD |  With WORD support, the OFFICE module makes it possible to create docx files in the Office Open XML format based on ECMA-376 without macros for Word 2007 and Word 2010. See [OFFICE](eecoffice_k_office.htm)  
SCRIPTING |  The SCRIPTING module allows the modular system developer to add scripts to the existing EEC functionality. Scripts are programmed in Groovy on the basis of Java. Typical uses include, among others, data import and special calculations. See [SCRIPTING](eecscripting_k_scripting.htm)  
SAP |  By means of the generic SAP interface data between SAP and EEC are transferred bidirectional. On one hand, the function modules contained in the SAP standard can be activated. On the other hand, however, individually programmed modules can also be used. See [SAP interface](eecsap_k_sap.htm)
