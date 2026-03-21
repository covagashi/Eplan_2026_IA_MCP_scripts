---
title: "content()"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_datasourceobjects_content_1.htm"
file: "refformulas_r_datasourceobjects_content_1"
category: "refformulas"
---

# content()

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  content() Data source objects Delivers a list of all objects of the standard data source table. Each object represents a row of this table. These objects can be accessed by methods that match the column names of the table. For calculated column names the method property(<column name>) is available. For large amounts of data the access with [perform(String sqlStatement)](refformulas_r_datasourceobjects_perform.htm) is to be preferred. **content()**  
---  
Argument |  |  |   
Return value | List |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=type('ModularSystem.PartsList.ArticleDB').content().select(record | record.property('Vendor') = 'Balluff' and record.property('ArticleType') = 'Cam switch') | [[12,432,Cam switch,Balluff,Cam switch Balluff 24V,24.0,0.0], [15,583,Cam switch,Balluff,Cam switch Balluff 48V,48.0,0.0]]
