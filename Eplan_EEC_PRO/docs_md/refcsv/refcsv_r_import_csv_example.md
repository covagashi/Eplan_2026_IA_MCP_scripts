---
title: "Example for the import into a map"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcsv_r_import_csv_example.htm"
file: "refcsv_r_import_csv_example"
category: "refcsv"
---

# Example for the import into a map

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Example for the import into a map Importing of CSV files is often used to fill a map with key value pairs whose values in turn contain maps. Either a CSV file is imported to also create a new project and in the process store the matching configuration values in a map, or a CSV file is imported during the configuration that stores values in a map consistently with the current configuration step. The following scenario describes the case that a new project is created during the import of the CSV file and a map is filled with values. A type of construction is queried by means of a Form-UI so that an individual value, which in turn is a map, is determined from the map. The individual values are queried from this map and are displayed in the Form-UI. The tutorial model Feeder (see [Tutorial](tutorial_k_tutorial.htm)) serves as the basis for this scenario. Create the following extensions to this purpose: [Creating parameters](javascript:void\(0\);) Parameter name | Type  
---|---  
ParameterMap | Map  
ParameterMap1 | Map  
ParameterBag | Bag  
Make | String  
Power | String  
Relay | String  
Drive | String  
Cable | String  
MotorProtectiveCircuitBreaker | String  
[Inserting and parameterizing parameters into the Feeder component](javascript:void\(0\);) Parameter name | Value  
---|---  
ParameterMap | =$ParameterMap1.select(x|x.key=$Make)  
ParameterMap1 | After the import, the value of this map consists of the values of the CSV file.  
ParameterBag | =$ParameterMap.select(x|x.key=$Make).values  
Make | The value of this parameter is determined through the selection in Form-UI.  
Power | =$ParameterBag.value('Power').asList.first  
Relay | =$ParameterBag.value('Relay').asList.first  
Drive | =$ParameterBag.value('Drive').asList.first  
Cable | =$ParameterBag.value('Cable').asList.first  
MotorProtectiveCircuitBreaker | =$ParameterBag.value('MotorProtectiveCircuitBreaker').asList.first  
[Create Form-UI in the Feeder component](javascript:void\(0\);)
    
        <?xml version="1.0" encoding="UTF-8"?>
    <uis xmlns="http://www.mind8.com/FormUI"
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
     
    	<form title="Import" id="import">
     
    		<group id="ConveyorSelection" title="Conveyor Selection">
     
    			<label>Size</label>
    			<input receiver="=parameter('Make')"    type="radio" values="=List{Pair{'Short Belt','C1'},Pair{'Medium Belt','C2'},Pair{'Large Belt','C3'}}"></input>
     
    			<label>Drive</label>
    			<input type="text" receiver="=parameter('Drive')" editable="false" ></input>
     
    			<label>Power</label>
    			<input type="text" receiver="=parameter('Power')" editable="false"></input>
     
    			<label>Relay</label>
    			<input type="text" receiver="=parameter('Relay')" editable="false"></input>
     
    			<label>Motor Protective Circuit Breaker</label>
    			<input type="text" receiver="=parameter('MotorProtectiveCircuitBreaker')" editable="false"></input>
     
    			<label>Cable</label>
    			<input type="text" receiver="=parameter('Cable')" editable="false"></input>
    		</group>
    	</form>
    </uis>

[Example CSV file for the import (ConveyorData.csv)](javascript:void\(0\);)
    
        Make;Drive;MotorProtectiveCircuitBreaker;Relay;Cable;Power
    C1;K21R63K4;PKZM0-063;DILM7;MC4G1,5;0.12kW
    C2;K21R71K4;PKZM0-1;DILM7;MC4G1,5;0.25kW
    C3;IE3-W41R90SY4;PKZM0-4;DILM7;MC4G2,5;1.1kW

[Example schema file for the import (KeyValue_ConveyorData.xsl)](javascript:void\(0\);)
    
        <?xml version="1.0" encoding="utf-8"?>
    <xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    	<!-- STM Stuttgart 01.09.2015-->
    	<!-- (c) Copyright EPLAN GmbH & Co. KG, Stuttgart, 2015. -->  
    	<!-- stylesheet for csv and excel import of keys and values -->
     
    	<!--+++++++++++++++++++++++++++++++++++++++++++++++++++++ Area to customize this xslt ++++++++++++++++++++++++++++++++++++++++++++++++-->
     
    	<!-- name of the parameter used for map ('ParameterMap') --> 
    	<xsl:variable name="ParameterMap1" select="'ParameterMap1'"/> 
    	<!-- to use a specific ExcelSheet please enter the name as String ('first') or get the name by xPath --> 
    	<xsl:variable name="ExcelSheet" select="xmlTable/sheet[1]/@name"/> 
      
    	<!-- the end of the header is either a variable row defined by a string or a fix row --> 
    	<xsl:variable name="KeyWordLineEndHeader" select="'LineEndHeader'"/>
      
    	<!-- there should always be just one of the next two <xsl:variable> entries active (= uncommented) --> 
    	<!-- if the header is a variable row defined by a string then use (and modify) this entry --> 
    	<xsl:variable name="LineEndHeader"> 
    		<xsl:choose> 
    			<xsl:when test="xmlTable/sheet[@name=$ExcelSheet]/row/col[.=$KeyWordLineEndHeader]/../@number"> 
    				<xsl:value-of select="xmlTable/sheet[@name=$ExcelSheet]/row/col[.=$KeyWordLineEndHeader]/../@number"/> 
    			</xsl:when> 
    			<xsl:when test="xmlTable/row/col[.=$KeyWordLineEndHeader]/../@number"> 
    				<xsl:value-of select="xmlTable/row/col[.=$KeyWordLineEndHeader]/../@number"/> 
    			</xsl:when> 
    			<xsl:otherwise> 
    				<xsl:value-of select="1"/> 
    			</xsl:otherwise> 
    		</xsl:choose> 
    	</xsl:variable> 
    	  
    	<!-- if the header is defined by a fix row (e.g. =1 or =0 if no header is used) then use (and modify) this entry --> 
    	<!-- 
    	<xsl:variable name="LineEndHeader"> 
    		<xsl:value-of select="0"/> 
    	</xsl:variable> 
    	-->
     
    	<!--++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++--> 
      
    	<xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes" /> 
      
    	<xsl:template match="/"> 
    		<imx> 
    			<xsl:element name="parameter"> 
    				<xsl:attribute name="name"> 
    					<xsl:value-of select="$ParameterMap1"/> 
    				</xsl:attribute> 
    				<value> 
    					<hashMap> 
    						<xsl:apply-templates select="xmlTable"/> 
    					</hashMap> 
    				</value> 
    			</xsl:element> 
    		</imx> 
    	</xsl:template>
     
    	<xsl:template match="xmlTable"> 
    		<xsl:choose> 
    			<xsl:when test="sheet"> 
    				<xsl:apply-templates select="sheet"/> 
    			</xsl:when> 
    			<xsl:when test="row"> 
    				<xsl:apply-templates select="row"/> 
    			</xsl:when> 
    		</xsl:choose> 
    	</xsl:template>
      
    	<xsl:template match="sheet"> 
    		<xsl:if test="@name=$ExcelSheet"> 
    			<xsl:apply-templates select="row"/> 
    		</xsl:if> 
    	</xsl:template>
      
    	<xsl:template match="row" > 
    		<xsl:choose> 
    			<xsl:when test="@number > $LineEndHeader "> 
    				<put> 
    					<xsl:element name="key"> 
    						<xsl:attribute name="value"> 
    							<xsl:value-of select="col[@number='1']"/> 
    						</xsl:attribute> 
    					</xsl:element> 
      
    					<xsl:element name="value"> 
    						<!-- <put> 
    							<value> --> 
    								<hashMap> 
    								<!-- <xsl:value-of select="''"/> --> 
    									<put> 
    										<xsl:attribute name="key"> 
    											<xsl:value-of select="'Make'"/> 
    										</xsl:attribute> 
    									<xsl:element name="value"> 
    										<xsl:attribute name="value"> 
    											<xsl:value-of select="col[@number='1']"/> 
    										</xsl:attribute> 
    									</xsl:element> 
    									</put> 
      
    									<put> 
    										<xsl:attribute name="key"> 
    											<xsl:value-of select="'Drive'"/> 
    										</xsl:attribute> 
    									<xsl:element name="value"> 
    										<xsl:attribute name="value"> 
    											<xsl:value-of select="col[@number='2']"/> 
    										</xsl:attribute> 
    									</xsl:element> 
    									</put> 
      
    									<put> 
    										<xsl:attribute name="key"> 
    											<xsl:value-of select="'MotorProtectiveCircuitBreaker'"/> 
    										</xsl:attribute> 
    									<xsl:element name="value"> 
    										<xsl:attribute name="value"> 
    											<xsl:value-of select="col[@number='3']"/> 
    										</xsl:attribute> 
    									</xsl:element> 
    									</put> 
      
    									<put> 
    										<xsl:attribute name="key"> 
    											<xsl:value-of select="'Relay'"/> 
    										</xsl:attribute> 
    									<xsl:element name="value"> 
    										<xsl:attribute name="value"> 
    											<xsl:value-of select="col[@number='4']"/> 
    										</xsl:attribute> 
    									</xsl:element> 
    									</put> 
      
    									<put> 
    										<xsl:attribute name="key"> 
    											<xsl:value-of select="'Cable'"/> 
    										</xsl:attribute> 
    									<xsl:element name="value"> 
    										<xsl:attribute name="value"> 
    											<xsl:value-of select="col[@number='5']"/> 
    										</xsl:attribute> 
    									</xsl:element> 
    									</put> 
      
    									<put> 
    										<xsl:attribute name="key"> 
    											<xsl:value-of select="'Power'"/> 
    										</xsl:attribute> 
    									<xsl:element name="value"> 
    										<xsl:attribute name="value"> 
    											<xsl:value-of select="col[@number='6']"/> 
    										</xsl:attribute> 
    									</xsl:element> 
    									</put> 
      
    								</hashMap> 
    							<!-- </value> 
    						</put> --> 
    					</xsl:element>
    				</put> 
    			</xsl:when> 
    			<xsl:otherwise> 
    			</xsl:otherwise> 
    		</xsl:choose> 
    	</xsl:template> 
    </xsl:stylesheet>

[Example template file for the import (Template_CSV.imx)](javascript:void\(0\);)
    
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

The CSV file has to be imported to create a new project:
    1. Open the import wizard via File > Import....
    2. Select Project > Import.
    3. Click [Next >].
    4. Enter the name of the CSV file in the Source file name field (Example: ConveyorData.csv).
    5. Select the Custom schema entry for the type of the scheme.
    6. Enter the name of the scheme file in the Custom schema field (Example: KeyValue_ConveyorData.xsl).
    7. Enter the name of the template file in the Template file name field (Example: Template_CSV.imx).
    8. In the Create new project field, enter another name for the new project, if appropriate.
    9. Click [Finish].
The new project then has to be entered in the Project catalog. The Feeder component has to be opened in the new project to check the result:
    1. Open the Feeder component in the Project catalog.
    2. Open the Parameters editor page.
As a result of the import the ParameterMap1 parameter is filled with a map:
    
        [
    C1Â»[CableÂ»MC4G1,5,MotorProtectiveCircuitBreakerÂ»PKZM0-063,RelayÂ»DILM7,DriveÂ»K21R63K4,MakeÂ»C1,PowerÂ»0.12kW],
    C2Â»[CableÂ»MC4G1,5,MotorProtectiveCircuitBreakerÂ»PKZM0-1,RelayÂ»DILM7,DriveÂ»K21R71K4,MakeÂ»C2,PowerÂ»0.25kW],
    C3Â»[CableÂ»MC4G2,5,MotorProtectiveCircuitBreakerÂ»PKZM0-4,RelayÂ»DILM7,DriveÂ»IE3-W41R90SY4,MakeÂ»C3,PowerÂ»1.1kW]
    ]

All other parameter values can only be determined after a selection has been made in the Form-UI. Make a selection in the Form-UI:
    1. Open the Import editor page.
    2. Select an option for Size.
The values for the fields arranged below are calculated and displayed. The following figure shows the results next to each other for all options:
