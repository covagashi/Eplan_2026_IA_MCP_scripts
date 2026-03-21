---
title: "Importing project data via wizard"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_import_projectdata.htm"
file: "eecbase_k_import_projectdata"
category: "eecbase"
---

# Importing project data via wizard

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Importing project data via wizard

Files in different formats can be imported by using the import wizard.

The following formats are supported:

     * Excel (*.XLS, *.XLSX, *.XLSM)
     * CSV
     * IMX
     * XML

New libraries, components and projects can be added as well as parameter values set through the importing process.

The following figure shows the scheme of the file import and the instantiation of the resulting project:

Depending on the format of the source file, also a scheme file and optionally a preferences file (template) are needed. A file created by the customer, a standard file for key value pairs KeyValue.xsl or a standard file for importing parameter values Parameter.xsl can be selected as the scheme file.

A template file can, for example, contain all the components and parameter values that always exist in a project and the imported file contains all the further components and parameter values for a specific project.

This is how you call the Import wizard:

    1. Select the menu File > Import....

The Select dialog opens.

    2. In the tree structure, select the Project > Import entry.
    3. Click [Next >].

The Import file dialog opens.

    4. Enter the name of the file to be imported in the Source file name field.
    5. Select a standard scheme file from the drop-down list, if appropriate.
    6. If Customer scheme is selected in the drop-down list, specify the name of the scheme file to be used as the basis for importing the source file.
    7. Enter the name of the template file in the Template file name field.
    8. Mark the check box and enter the name of the new project in the Create a new project field, if a new project is to be created with the import of the Excel file. If the name already exists, an index is automatically added to the end of the name (e.g., Project, Project2, Project3, etc.).

The project is now listed in the Project Catalog. Existing projects of the same name are overwritten in the process.

    9. If the check box Create new project is not selected, mark a project into which importing is to be carried out.
    10. Confirm your selection with [Finish].

### Read more

     * [CSV Transformation](refcsv_r_csv_transformation.htm)
     * [Excel-Transformation](refexcel_r_excel_transformation.htm)
     * [XML Transformation](refxml_r_xml_transformation.htm)
