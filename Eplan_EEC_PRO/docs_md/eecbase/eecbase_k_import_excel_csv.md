---
title: "Importing CSV or Excel files with default schemes"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_import_excel_csv.htm"
file: "eecbase_k_import_excel_csv"
category: "eecbase"
---

# Importing CSV or Excel files with default schemes

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Importing CSV or Excel files with default schemes

The standard scheme files KeyValue.xsl and Parameter.xsl are provided for importing a CSV or Excel file.

The KeyValue.xsl scheme file is used to store the rows of a CSV or Excel file as a map in the ParameterMap parameter.

Through the Parameter.xsl scheme file the rows of a CSV or Excel file are interpreted as a Parameter name and Parameter value.

In both cases a parameter is not created. Rather a parameter of the same name has to exist in the project that has the value from the import file assigned to it!

Import with KeyValue.xsl scheme file:

### [Example CSV file for the import](javascript:void\(0\);)
    
        GripperA;1
    GripperB;2
    GripperC;;

This file is first converted to:
    
        <?xml version="1.0"?>
    <xmlTable>
    	<row number="1">
    		<col number="1">GripperA</col>
    		<col number="2">1</col>
    	</row>
    	<row number="2">
    		<col number="1">GripperB</col>
    		<col number="2">2</col>
    	</row>
    	<row number="3">
    		<col number="1">GripperC</col>
    		<col number="2"></col>
    	</row>
    </xmlTable>

Result in the project:
    
        ParameterMap=Map{Pair{'GripperA','1'},Pair{'GripperB','2'},Pair{'GripperC',''}}

### [Example Excel file for the import](javascript:void\(0\);)

| A | B  
---|---|---  
1 | GripperA | 1  
2 | GripperB | 2  
3 | GripperC |   
  
This file is first converted to:
    
        <?xml version="1.0"?>
    <xmlTable>
    	<sheet name="Table1">
    		<row number="1">
    			<col number="1">GripperA</col>
    			<col number="2">1</col>
    		</row>
    		<row number="2">
    			<col number="1">GripperB</col>
    			<col number="2">2</col>
    		</row>
    		<row number="3">
    			<col number="1">GripperC</col>
    			<col number="2"></col>
    		</row>
    	</sheet>
    </xmlTable>

Result in the project:
    
        ParameterMap=Map{Pair{'GripperA','1'},Pair{'GripperB','2'},Pair{'GripperC',''}}

Import with Parameter.xsl scheme file:

### [Example CSV file for the import](javascript:void\(0\);)
    
        GripperA;1
    GripperB;2
    GripperC;;

This file is first converted to:
    
        <?xml version="1.0"?>
    <xmlTable>
    	<row number="1">
    		<col number="1">GripperA</col>
    		<col number="2">1</col>
    	</row>
    	<row number="2">
    		<col number="1">GripperB</col>
    		<col number="2">2</col>
    	</row>
    	<row number="3">
    		<col number="1">GripperC</col>
    		<col number="2"></col>
    	</row>
    </xmlTable>

Result in the project:

Name | Result | Value | Type  
---|---|---|---  
GripperA | 1 | ='1' | String  
GripperB | 2 | ='2' | String  
GripperC |  | ='' | String  
  
### [Example Excel file for the import](javascript:void\(0\);)

| A | B  
---|---|---  
1 | GripperA | 1  
2 | GripperB | 2  
3 | GripperC |   
  
This file is first converted to:
    
        <?xml version="1.0"?>
    <xmlTable>
    	<sheet name="Table1">
    		<row number="1">
    			<col number="1">GripperA</col>
    			<col number="2">1</col>
    		</row>
    		<row number="2">
    			<col number="1">GripperB</col>
    			<col number="2">2</col>
    		</row>
    		<row number="3">
    			<col number="1">GripperC</col>
    			<col number="2"></col>
    		</row>
    	</sheet>
    </xmlTable>

Result in the project:

Name | Result | Value | Type  
---|---|---|---  
GripperA | 1 | ='1' | String  
GripperB | 2 | ='2' | String  
GripperC |  | ='' | String
