---
title: "Writing key-value parts into parameters by importing a CSV file"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutimp_h_t3_params_map_csv.htm"
file: "tutimp_h_t3_params_map_csv"
category: "tutimp"
---

# Writing key-value parts into parameters by importing a CSV file

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Writing key-value parts into parameters by importing a CSV file Requirements:
     * The preparatory steps on the file level have been carried out.
     * EEC is started.
     * In addition to the system libraries, the Library catalog contains the architecture T_Mechatronic_Architecture and the modular system T_Mechatronic_ModularSystem.
     * The **Feeder** project contains the Project catalog.
     * The [Writing values into individual parameters by importing a CSV file](tutimp_h_t3_params_values_csv.htm) ssection has been carried out.
The CSV file ParameterMap.csv is imported in order to fill the ParameterMap parameter with key-value pairs in the existing configuration. To this purpose the template file Template_CSV.imx is additionally required. [Contents of the ParameterMap.csv](javascript:void\(0\);) Description of the CSV file: The CSV file consists of 9 rows and 3 columns. The columns do not have any headers. An area for header data is introduced via the data to be evaluated with a cell that contains the text Header. The header data end in the row that contains a cell with the text LineEndHeader. The data to be evaluated are distributed across 3 columns: A = Name of the parameter B = Value of the parameter C = Type of the parameter These specifications are converted internally into a fragment in IMX format by means of the XSL file KeyValue.xsl. The fragment is inserted into the template file Template_CSV.imx instead of the <importFragment/> tag. Content of the Template_CSV.imx:
    
        <?xml version="1.0" encoding="utf-8"?>
    <imx xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xi="http://www.w3.org/2001/XInclude" version="1.0">
    	<project name="Feeder" save="true">
    		<libraries>
    			<add type="String" value="T_Mechatronic_ModularSystem"/>
    		</libraries>
    		<mo name="Feeder" typeClass="T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder" >
    			<importFragment/>
    		</mo>
    	</project>
    </imx>

Proceed as follows to fill a Map with key-value pairs:
    1. Select the menu item File > Import....
The import wizard opens with the Select page.
    1. Navigate to Project > Import.
    2. Confirm via [Next >].
The import wizard opens the page Import file.
    1. Specify the file ParameterMap.csv in the Source file name field.
The file is located in the following directory:
    
        <EEC installation path>\resources\Import\CSV

Use [Browse...] to navigate to the file. If applicable, select the file filter CSV files (*.csv).
    1. From the Customer scheme drop-down list, select the entry Default:KeyValue.xsl. This grays out the input field.
    2. Enter the file Template_CSV.imx in the Template file name field.
The file is located in the following directory:
    
        <EEC installation path>\resources\Import\IMX

Use [Browse...] to navigate to the file. If applicable, select the file filter IMX files (*.imx).
    1. Remove the Create new project option and mark the Feeder project in the list below it.
    2. Confirm with [Finish].
Result: The configuration called Feeder is displayed in the project catalog:
    1. Open the Feeder component.
    2. Select the Parameters editor.
The Value column shows that the values from the columns A and B of the CSV file have been written as a key-value pair in the ParameterMap parameter.
