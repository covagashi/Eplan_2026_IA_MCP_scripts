---
title: "CSV Transformation"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcsv_r_csv_transformation.htm"
file: "refcsv_r_csv_transformation"
category: "refcsv"
---

# CSV Transformation

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  CSV Transformation The purpose of the CSV import is to create projects based on a modular system. The CSV files are converted during importing into the XML format, which in turn is converted using a schema file into the IMX format that can be interpreted by EEC (also refer to [IMX import]()). Importing of the CSV files is effected tthrough the command [Engineering.ImportIMXCommand](refcommands_r_engineering_importimxcommand.htm). The schema file for the conversion to the IMX format is created in XML format and must comply with the typical requirements for XML files. The following section describe how a schema file is structured for the import of Excel files. For importing an Excel file, one schema file and one mapping file are always required. The mapping file is always the same for the examples in the following sections and therefore is only listed once here. [Example code of the mapping file](javascript:void\(0\);)  
      
        <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <mapping>
    	<!-- MyMechatronic.Plant -->
    	<moTypeClass alias="Plant" realName="MyMechatronic.Plant"/>
    </mapping>
