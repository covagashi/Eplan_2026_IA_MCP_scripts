---
title: "content(String tablename)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_datasourceobjects_content_2.htm"
file: "refformulas_r_datasourceobjects_content_2"
category: "refformulas"
---

# content(String tablename)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  content(String tablename) Data source objects Returns a list of all objects of the table <Table name> of the data source. Each object represents a row of this table. These objects can be accessed by methods that match the column names of the table. For calculated column names the method property(<column name>) is available. For large amounts of data the access with [perform(String sqlStatement)](refformulas_r_datasourceobjects_perform.htm) is to be preferred. **content(String tablename)**  
---  
Argument | String | tablename | Name of the table which serves as data source  
Return value | List |   
[Example](javascript:void\(0\);) The file ProjectList.csv exists with the following content: Projektname |  Kunde |  Kommission |  Zeichnungsnummer  
---|---|---|---  
Antrieb Halle 1 |  Eplan |  KOM-4711 |  EPL-ZEI-1234  
Antriebsschrank Pumpe 123 |  Testkunde1 |  KOM-5050 |  EPL-ZEI-9999  
Antriebsschrank Pumpe 456 |  Testkunde2 |  KOM-8064 |  EPL-ZEI-5791  
The Antrieb Halle 1 value is transferred to the following example formulas with the Eplan_Projektname parameter. Formula | Result  
---|---  
      
        =if
    	type('Schaltschrankkonfigurator_Baukasten.Baukastenkonfiguration.Customizing.Projektliste')
    	.content().select(x|x.Projektname=$Eplan_Projektname)
    	.Kunde.size > 0
    then
    	type('Schaltschrankkonfigurator_Baukasten.Baukastenkonfiguration.Customizing.Projektliste')
    	.content().select(x|x.Projektname=$Eplan_Projektname)
    	.Kunde.first
    else ''
    endif

| Eplan  
      
        =if
    	type('Schaltschrankkonfigurator_Baukasten.Baukastenkonfiguration.Customizing.Projektliste')
    	.content().select(x|x.Projektname=$Eplan_Projektname)
    	.Kommision.size > 0
    then
    	type('Schaltschrankkonfigurator_Baukasten.Baukastenkonfiguration.Customizing.Projektliste')
    	.content().select(x|x.Projektname=$Eplan_Projektname)
    	.Kommision.first
    else ''
    endif

| KOM-4711  
      
        =if
    	type('Schaltschrankkonfigurator_Baukasten.Baukastenkonfiguration.Customizing.Projektliste')
    	.content().select(x|x.Projektname=$Eplan_Projektname)
    	.Zeichnungsnummer.size > 0
    then
    	type('Schaltschrankkonfigurator_Baukasten.Baukastenkonfiguration.Customizing.Projektliste')
    	.content().select(x|x.Projektname=$Eplan_Projektname)
    	.Zeichnungsnummer.first
    else ''
    endif

| EPL-ZEI-1234  
[Example](javascript:void\(0\);) The texts of a Form-UI are to be displayed in German or English, depending on the language selection. In this example the texts are collected in a CSV file with the following contents: key | deDE | enUS  
---|---|---  
FeederConfiguration | Feeder-Konfiguration | Feeder configuration  
AddWorkpieceInspection | WerkstÃ¼ckprÃ¼fung hinzufÃ¼gen | Add workpiece inspection  
ImportP8Discipline | Disziplin ECAD P8 importieren | Import ECAD P8 discipline  
UpdateExtensions | Erweiterungspunkte aktualisieren | Update extensions  
LanguageSelection | Sprachauswahl | Language selection  
ImportP8Discipline | ECAD P8 Disziplin importieren | Import ECAD P8 Discipline  
UpdateExtensions | Erweiterungspunkte aktualisieren |  Update extensions  
The CSV file for the language elements is created as a data source object with the name "languages". The parameter for the language selection with the name "languages" contains the selection values "deDE" and "enUS". The following formula is used to display the text "Feeder-Konfiguration" for the parameter value deDE or the text "Feeder configuration" for the parameter value enUS:
    
        text="=type('T_DataSources.translations').content().select(x|x.property('key')='FeederConfiguration').collect(x|x.value($Language)).first"

Explanation of the formula: With type('T_DataSources.translations').content() you obtain a list with maps of all table rows, for example [[keyÂ»FeederConfiguration,deDEÂ»Feeder-Konfiguration,enUSÂ»Feeder configuration], [keyÂ»AddWorkpieceInspection,deDEÂ»WerkstÃ¼ckprÃ¼fung hinzufÃ¼gen,enUSÂ»Add workpiece inspection],...]. With the term select(x|x.property('key')='FeederConfiguration') you extract from the list of maps a list with the map whose key has the value FeederConfiguration, for example [[keyÂ»FeederConfiguration,deDEÂ»Feeder-Konfiguration,enUSÂ»Feeder configuration]]. Use the collect(x|x.value($Language)) term to extract a list from the extracted list. The only element in the list is the value of the key stored in the $Language parameter. For the parameter $Language select the value deDE, receive as list [Feeder-Konfiguration], select the value enUS, receive as list [Feeder configuration]. With the term first you receive the first element of the list, meaning for deDE the string Feeder-Konfiguration or for enUS the string Feeder configuration.
