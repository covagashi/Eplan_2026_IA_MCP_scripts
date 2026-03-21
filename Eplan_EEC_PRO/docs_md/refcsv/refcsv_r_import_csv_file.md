---
title: "Importing of the CSV file"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcsv_r_import_csv_file.htm"
file: "refcsv_r_import_csv_file"
category: "refcsv"
---

# Importing of the CSV file

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Importing of the CSV file Before a transformation can take place the CSV file sis converted into a defined XML structure. In the process it is read in row-by-row and a <row> tag inserted for each row and a <col> tag inserted for each value separated by a separator. This structure is enveloped by an <xmlTable> tag. [Example CSV file for the import](javascript:void\(0\);)
    
        Part name;Value
    A;1
    B;2
    C;;

This file is first converted to:
    
        <?xml version="1.0"?>
    <xmlTable>
    	<row number="1">
    		<col number="1">Part name</col>
    		<col number="2">Value</col>
    	</row>
    	<row number="2">
    		<col number="1">A</col>
    		<col number="2">1</col>
    	</row>
    	<row number="3">
    		<col number="1">C</col>
    		<col number="2"></col>
    	</row>
    </xmlTable>

The resulting XML structure be processed further as described in the section [XML Transformation](refxml_r_xml_transformation.htm).
