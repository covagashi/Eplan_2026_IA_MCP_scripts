---
title: "Writing values into individual parameters by importing a CSV file"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutimp_h_t3_params_values_csv.htm"
file: "tutimp_h_t3_params_values_csv"
category: "tutimp"
---

# Writing values into individual parameters by importing a CSV file

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Writing values into individual parameters by importing a CSV file Requirements:
     * The preparatory steps on the file level have been carried out.
     * EEC is started.
     * In addition to the system libraries, the Library catalog contains the architecture T_Mechatronic_Architecture and the modular system T_Mechatronic_ModularSystem.
     * The **Feeder** project contains the Project catalog.
     * Section [Creating a configuration by importing an IMX file](tutimp_h_t1_create_project_imx.htm) is carried out.
In the existing configuration the Feeder component already contains parameters which do not, however, contain values as the following representation shows. The CSV file Parameter.csv is imported in order to set parameter values in the existing configuration. To this purpose the template file Template_CSV.imx is additionally required. Note Identically structured Excel files can be imported with the identical template and scheme files. [Contents of the Parameters.csv](javascript:void\(0\);) Description of the CSV file: The CSV file consists of 8 rows and 3 columns. The columns do not have any headers. An area for header data is introduced via the data to be evaluated with a cell that contains the "Header" text. The header data end in the row that contains a cell with the "LineEndHeader" text. The data to be evaluated are distributed across 3 columns: A = Name of the parameter B = Value of the parameter C = Type of the parameter These specifications are converted internally into a fragment in IMX format by means of the XSL file Parameter.xsl. The fragment is inserted into the template file Template_CSV.imx instead of the <importFragment/> tag. [Contents of the Template_CSV.imx](javascript:void\(0\);)
    
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

Proceed as follows to set parameter values:
    1. Select the menu item File > Import....
The import wizard opens with the Select page.
    1. Navigate to Project > Import.
    2. Confirm via [Next >].
The import wizard opens the page Import file.
    1. Specify the file Parameter.csv in the Source file name field.
The file is located in the following directory:
    
        <EEC installation path>\resources\Import\CSV

Use [Browse...] to navigate to the file. If appropriate, select the filter Excel workbooks (*.xls, *.xlsx, *.xlsm).
    1. From the Customer scheme drop-down list, select the entry Default:Parameter.xsl. This grays out the input field.
    2. Enter the file Template_CSV.imx in the Template file name field.
The file is located in the following directory:
    
        <EEC installation path>\resources\Import\IMX

Use [Browse...] to navigate to the file. If applicable, select the file filter IMX files (*.imx).
    1. Remove the Create new project option and mark the Feeder project in the list below it.
    2. Confirm with [Finish].
Result: The configuration called Feeder is displayed in the project catalog:
    1. Open the Feeder component.
    2. Select the Parameters editor.
The Value column shows that all the values are enclosed with apostrophes (') and thus were imported as strings. The ParameterBoolean parameter is filled with the value ='true'. Since this is not a valid Boolean value, false is entered as the result. Formula errors are displayed for the parameters ParameterDouble and ParameterInteger because the imported values cannot be interpreted as Double or Integer respectively. The ParameterMap parameter is not filled by the import and is therefore <<null>>. Solely the ParameterString parameter is set correctly with the value Hello World. In other words: The third column of the CSV file is not detected during the conversion and consequently all the imported values are interpreted as a string. If the parameters are to be imported with the correct type, the scheme file for the transformation of the CSV file has to be customized. Proceed as follows to change the XSL file:
    1. Copy the <EEC installation path>\install\importschemas\Parameter.xsl file into the following folder:
        
                <EEC installation path>\resources\Import\XSL

    2. Rename the file to ParameterWithType.xsl.
    3. Open the file ParameterWithType.xsl with any editor, for example Notepad++.
    4. Navigate to the <xsl:template match="row" > tag in the file.
Appearance before the change:
    
        <xsl:template match="row" >
    	<xsl:choose>
    		<xsl:when test="@number > $LineEndHeader ">
    			<xsl:element name="parameter">
    				<xsl:attribute name="name">
    					<xsl:value-of select="col[@number='1']"/>
    				</xsl:attribute>
    				<xsl:attribute name="value">
    					<xsl:value-of select="col[@number='2']"/>
    				</xsl:attribute>
    			</xsl:element>
    		</xsl:when>
    		<xsl:otherwise>
    		</xsl:otherwise>
    		</xsl:choose>
    </xsl:template>

Insert the following rows at the end of the block of <xsl:element name="parameter">:
    
        <xsl:attribute name="type">
    	<xsl:value-of select="col[@number='3']"/>
    </xsl:attribute>

The result should look as follows:
    
        <xsl:template match="row" >
    	<xsl:choose>
    		<xsl:when test="@number > $LineEndHeader ">
    			<xsl:element name="parameter">
    				<xsl:attribute name="name">
    					<xsl:value-of select="col[@number='1']"/>
    				</xsl:attribute>
    				<xsl:attribute name="value">
    					<xsl:value-of select="col[@number='2']"/>
    				</xsl:attribute>
    				<xsl:attribute name="type">
    					<xsl:value-of select="col[@number='3']"/>
    				</xsl:attribute>
    			</xsl:element>
    		</xsl:when>
    		<xsl:otherwise>
    		</xsl:otherwise>
    		</xsl:choose>
    </xsl:template>

Import with the modified scheme file ParameterWithType.xsl:
    1. Select the menu item File > Import....
The import wizard opens with the Select page.
    1. Navigate to Project > Import.
    2. Confirm via [Next >].
The import wizard opens the page Import file.
    1. Specify the file Parameter.csv in the Source file name field.
The file is located in the following directory:
    
        <EEC installation path>\resources\Import\CSV

Use [Browse...] to navigate to the file. If appropriate, select the filter Excel workbooks (*.xls, *.xlsx, *.xlsm).
    1. From the Customer scheme drop-down list, select the entry Customer scheme.
    2. Specify the modified scheme file.
    
        <EEC installation path>\resources\Import\XSL\ParameterWithType.xsl

Use [Browse...] to navigate to the file. If applicable, select the file filter Scheme XSL files (*.xsl, *.xslt).
    1. Enter the file Template_CSV.imx in the Template file name field.
The file is located in the following directory:
    
        <EEC installation path>\resources\Import\IMX

Use [Browse...] to navigate to the file. If applicable, select the file filter IMX files (*.imx).
    1. Remove the Create new project option and mark the Feeder project in the list below it.
    2. Confirm with [Finish].
Result: The configuration called Feeder is displayed in the project catalog:
    1. Open the Feeder component.
    2. Open the Parameter editor.
The Values column shows that all the values have been imported with their own types. The ParameterMap parameter is not filled by the import and is therefore <<null>>. In the next step this parameter is filled through importing.
