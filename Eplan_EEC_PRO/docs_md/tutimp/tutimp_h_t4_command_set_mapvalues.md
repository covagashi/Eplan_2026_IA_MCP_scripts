---
title: "Importing a CSV file via an action"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutimp_h_t4_command_set_mapvalues.htm"
file: "tutimp_h_t4_command_set_mapvalues"
category: "tutimp"
---

# Importing a CSV file via an action

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Importing a CSV file via an action Requirements:
     * The preparatory steps on the file level have been carried out.
     * EEC is started.
     * In addition to the system libraries, the Library catalog contains the architecture T_Mechatronic_Architecture and the modular system T_Mechatronic_ModularSystem.
     * The **Feeder** project contains the Project catalog.
     * Section [Creating a configuration by importing an IMX file](tutimp_h_t1_create_project_imx.htm) is carried out.
The CSV file ParameterMap.csv is imported by means of an action in order to fill the ParameterMap parameter with key-value pairs in the existing configuration. To this purpose the template file Template_CSV.imx and the scheme file KeyValue.xsl are required. With the same action the CSV file Parameter.csv is imported in order to set the values of the parameters ParameterBoolean, ParameterInteger, ParameterDouble and ParamterString. To this purpose the template file Template_CSV.imx and the scheme file ParameterWithType.xsl are required. [Contents of the ParameterMap.csv](javascript:void\(0\);) Description of the CSV file: The CSV file consists of 9 rows and 3 columns. The columns do not have any headers. An area for header data is introduced via the data to be evaluated with a cell that contains the text Header. The header data end in the row that contains a cell with the text LineEndHeader. The data to be evaluated are distributed across 3 columns: A = Name of the parameter B = Value of the parameter C = Type of the parameter These specifications are converted internally into a fragment in IMX format by means of the XSL file KeyValue.xsl. The fragment is inserted into the template file Template_CSV.imx instead of the <importFragment/> tag. [Contents of the Template_CSV.imx](javascript:void\(0\);)
    
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

[Contents of the Parameters.csv](javascript:void\(0\);) Description of the CSV file: The CSV file consists of 8 rows and 3 columns. The columns do not have any headers. An area for header data is introduced via the data to be evaluated with a cell that contains the "Header" text. The header data end in the row that contains a cell with the "LineEndHeader" text. The data to be evaluated are distributed across 3 columns: A = Name of the parameter B = Value of the parameter C = Type of the parameter These specifications are converted internally into a fragment in IMX format by means of the XSL file Parameter.xsl. The fragment is inserted into the template file Template_CSV.imx instead of the <importFragment/> tag. To execute an action a link is inserted in a Form-UI of the Feeder component. The action starts the Engineering.ImportCsvCommand command. Create a unit for actions:
    1. Mark the T_Mechatronic_ModularSystem library in the Library catalog.
    2. Select New > Unit in the shortcut menu.
    3. Enter Actions in the Name field.
Create the action ImportCsvAction:
    1. Mark the Actions unit in the T_Mechatronic_ModularSystem library in the Library catalog.
    2. Select New > Object... from the popup menu.
    3. Select Object > Action.
    4. Confirm with [Finish].
    5. Enter ImportCsvAction in the Name field.
    6. Open the Methods editor.
    7. Click the symbol  (Add method).
    8. Add run in the Name field.
    9. If applicable, mark the Class method option.
    10. If applicable, select the language Sequence.
    11. Click the symbol  (Add Single Argument).
    12. Enter the name xslt for the new argument.
    13. Specify the Engineering String type for the new argument.
    14. Repeat Steps 11 and 13 with the following specifications:  

Name | Type  
---|---  
template | Engineering.String  
project | Engineering.Object  
csv | Engineering.String  
delimiter | Engineering.String  
    15. Click the symbol  (Add called method).
    16. Select Object > Command > FrameworkCommand > ImportCSVCommand.
    17. In the Matching methods list select the method with the arguments String pathToXslt, String pathtoTemplate, Object projectOrMo, String pathToCsv, String delimiter.
    18. Confirm with [Finish].
The result should have this appearance: Create a Form-UI for the Feeder component:
    1. Open the Feeder component in the T_Mechatronic_ModularSystem library in the Library catalog.
    2. Open the UI configuration editor.
    3. If required, open the Source tab.
    4. Enter the following UI configuration.
[Contents of the UI configuration](javascript:void\(0\);)
        
                <?xml version="1.0" encoding="UTF-8"?>
        <uis xmlns="http://www.mind8.com/FormUI"
        	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        	<form title="Import" id="import">
        		<action type="link" name="T_Mechatronic_ModularSystem.Actions.ImportCsvAction"
        			arguments="=List{
        			'install\\importschemas\\KeyValue.xsl',
        			'resources\\Import\\IMX\\Template_CSV.imx',
        			'resources\\Import\\CSV\\ParameterMap.csv',
        			';',
        			this}">
        			Import CSV Data as key-value pairs
        		</action>
        		
        		<action type="link" name="T_Mechatronic_ModularSystem.Actions.ImportCsvAction"
        			arguments="=List{
        			'resources\\Import\\XSL\\ParameterWithType.xsl',
        			'resources\\Import\\IMX\\Template_CSV.imx',
        			'resources\\Import\\CSV\\Parameter.csv',
        			';',
        			this}">
        			Import CSV Data as single parameter values
        		</action>
        	</form>
        </uis>

Execute the action "Import CSV Data as key-value pairs" in Form-UI: The created Form-UI is available directly after saving in the Feeder project component under the name Import.
    1. Open the Feeder component in the Project catalog.
    2. Open the Import editor.
    3. Click the link Import CSV Data as key-value pairs.
Result: The result can be checked directly in the Feeder project component.
    1. Open the Parameter editor.
The Value column shows that the values from the columns A and B of the CSV file have been written as a key-value pair in the ParameterMap parameter. Execute the action "Import CSV data as single parameter values" in Form-UI:
    1. Open the Import editor.
    2. Click the link Import CSV data as single parameter values.
Result: The result can be checked directly in the Feeder project component.
    1. Open the Parameter editor.
The Value column shows that all the values from the CSV file have been imported with their own types.
