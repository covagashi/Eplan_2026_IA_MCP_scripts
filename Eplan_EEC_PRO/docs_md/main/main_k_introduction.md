---
title: "EPLAN Engineering Configuration"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/main_k_introduction.htm"
file: "main_k_introduction"
category: "main"
---

# EPLAN Engineering Configuration

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  EPLAN Engineering Configuration EPLAN Engineering Configuration is an object-oriented development system for configurations of machines and plants. The following figure is interactive. Click on the items in it to find out more about the possibilities of EEC. #### [Start](javascript:void\(0\);)
    1. Create a decomposition
    2. Identify properties
    3. [Identify common parts/variants](javascript:void\(0\);)
      1. Identify common parts
      2. Identify variants
    4. Specify component structure
    5. Specify the top-level component
    6. Create Modular system
    7. Create configuration
    8. Automate processes (optional)
#### [Create Modular system](javascript:void\(0\);)
    1. [Create architecture library](javascript:void\(0\);)
      1. Create library
      2. Import library 'Engineering'
      3. Create level components
      4. Specify level configuration
      5. Specify top-level component
    2. [Create mechatronic library](javascript:void\(0\);)
      1. Create library
      2. Import architecture library
      3. Create units for mechatronic components
      4. Create unit for parameters
      5. Create parameters
      6. [Create components](javascript:void\(0\);)
        1. Create variants by disabler
        2. Add parameters to components
        3. Assign values and formulas to parameters
      7. Install components
      8. [Optional](javascript:void\(0\);)
        1. Create extension points
        2. Create placeholders
    3. [Create disciplin library](javascript:void\(0\);)
      1. Create library
      2. Import discipline library
      3. Create architecture library
      4. Import interfaces library
      5. Create units
      6. Create parameters
      7. [Create discipline components](javascript:void\(0\);)
        1. Import resource file
        2. Add parameters to components
        3. Assign values and formulas to parameters
      8. [Enclosing discipline components](javascript:void\(0\);)
        1. Extend component with interface
        2. Install discipline component
        3. Create interface parameters
    4. [Create interface library](javascript:void\(0\);)
      1. Create library
      2. Import 'Engineering' library
      3. Create interfaces
#### [Create configuration](javascript:void\(0\);)
    1. [Interactive via drag & drop](javascript:void\(0\);)
      1. Create project
      2. Select libraries
      3. Select top-level component
      4. Drag component from modular system into project
      5. Execute actions
    2. [Interactive via Form-UI](javascript:void\(0\);)
      1. Create project
      2. Select library
      3. Select top-level component
      4. [Start Form-UI](javascript:void\(0\);)
        1. Enter/select values
        2. Instantiate components
        3. Import discipline library
        4. Update extension points
        5. Generate documents
    3. [Interactive via Graph2D](javascript:void\(0\);)
      1. Create project
      2. Select library
      3. Select top-level component
      4. [Start Graph2D diagram](javascript:void\(0\);)
        1. Drag graphic items into diagram
        2. Enter values via Form-UI
        3. Import discipline libraries
        4. Update extension points
        5. Generate documents
    4. [Partially automated via import](javascript:void\(0\);)
      1. Create project
      2. Select library
      3. Select top-level component
      4. [Start Form-UI](javascript:void\(0\);)
        1. Enter/select values
        2. Execute actions
        3. Instantiate components
        4. Import discipline libraries
        5. Import partial configurations
        6. Update extension points
        7. Generate documents
      5. Execute actions
#### [Automation](javascript:void\(0\);)
    1. Install Job Server
    2. Install Job Server Worker
    3. Create basic project
    4. Create import files
    5. Create job definitions
    6. [Deliver job definitions to Job Server](javascript:void\(0\);)
      1. Generate documents by Worker
      2. Provide download links
    7. Create methods to trigger jobs
All relevant components of a machine or plant are therefore modeled as mechatronic and discipline-specific components and organized in libraries. The discipline-specific components save references to contents from third-party systems or the contents themselves, for example macros from EPLAN Electric P8. With the help of parameters and methods, rules can be created to influence the type and compilation of the components during the configuration. For this configuration different user interfaces can be created. Depending on the requirements the interface is designed as a Gantt diagram, as a graphic diagram or similar to a website. The configuration of a machine or plant is subsequently compiled by using the user interface. Then discipline-specific documents are created from this, for example schematics.
