---
title: "propertyNames(String sqlStatement)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_datasourceobjects_propertynames.htm"
file: "refformulas_r_datasourceobjects_propertynames"
category: "refformulas"
---

# propertyNames(String sqlStatement)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  propertyNames(String sqlStatement) Data source objects Returns the names of the properties which are contained in a data source object query. **propertyNames(String sqlStatement)**  
---  
Argument | String | sqlStatement | SQL query to the data source  
Return value | String |   
[Example code](javascript:void\(0\);) Creating a map where the keys are the property names and the values are the column content:
    
        =type('Pfuderer-Baukasten.StÃ¼ckliste.ArtikelDB').content().intoInject
    (
    	record,map | record.propertyNames.intoInject
    	(
    		propertyName,innerMap | 
    		if not innerMap.containsKey(propertyName)
    		then innerMap.add(propertyName,List {record.property(propertyName)})
    		else innerMap.add(propertyName,innerMap.value(propertyName).append
    		(record.property(propertyName)))
    		endif,map
    	) , Map{}
    )
