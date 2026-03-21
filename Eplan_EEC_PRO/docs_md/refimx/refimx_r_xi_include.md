---
title: "\u003cxi:include\u003e"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refimx_r_xi_include.htm"
file: "refimx_r_xi_include"
category: "refimx"
---

# \u003cxi:include\u003e

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  <xi:include> IMX The <xi:include> tag inserts the IMX file at this location. The IMX file can be specified by different methods:
     * A relative URI, for example href="Excel_Mapping.imx" or href="test/Excel_Mapping.imx " or href="../output/test/Excel_Mapping.imx ".
A relative URI always references the path of the IMX file.
     * An absolute URI, for example href="file:///c:/Users/test/Excel_Mapping.imx".
In this case the correct notation file:/// with three flashes must be observed. The IMX file to be inserted must be well-formed. The tag has no sub-elements. Attribute | Usage | Values | Default value | Description  
---|---|---|---|---  
href | required |  |  | IMX file to be inserted  
xmlns:xi | required if not specified in the <jobdefinition> tag | http://www.w3.org/2001/XInclude |  | Namespace extension to facilitate use of xi:include  
[Example of an IMX file that uses xi:include:](javascript:void\(0\);)
    
        <?xml version="1.0" encoding="utf-8"?>
    <!-- VollstÃ¤ndiger ImX Import -->
    <imx xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xi="http://www.w3.org/2001/XInclude" version="1.0">
    						
    	<xi:include xmlns:xi="http://www.w3.org/2001/XInclude" href="file:///C:/temp/Mapping.imx"/>
    						
    	<project name="Feeder" save="true" >
    		<libraries>
    			<add type="String" value="T_Mechatronic_ModularSystem"/>
    		</libraries>
    		<mo name="Feeder" typeClass="Feeder" >
    			<mo name="Insert" typeClass="Insert" >
    				<mo name="Separator" typeClass="Separator" />
    			</mo>
    		</mo>
    	</project>
    </imx>

[Example of a mapping file to be inserted:](javascript:void\(0\);)
    
        <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <mapping>
    	<!-- T_Mechatronic_ModularSystem.Mechatronic.Functiongroups -->
    	<moTypeClass alias="Insert" realName="T_Mechatronic_ModularSystem.Mechatronic.Functiongroups.Insert"/>
    	
    	<!-- T_Mechatronic_ModularSystem.Mechatronic.Functionunits -->
    	<moTypeClass alias="Separator" realName="T_Mechatronic_ModularSystem.Mechatronic.Functionunits.Separator"/>
    	
    	<!-- T_Mechatronic_ModularSystem.Mechatronic.Stations -->
    	<moTypeClass alias="Feeder" realName="T_Mechatronic_ModularSystem.Mechatronic.Stations.Feeder"/>
    </mapping>
