---
title: "\u003cimportFragment/\u003e"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refimx_r_importfragment.htm"
file: "refimx_r_importfragment"
category: "refimx"
---

# \u003cimportFragment/\u003e

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  <importFragment/> The <importFragment/> tag inserts an IMX fragment at this point. This tag is only used in a template file. The tag is replaced by the content of the IMX fragment during importing, for example by using the[Engineering.ImportIMXWithTemplateCommand](refcommands_r_engineering_importimxwithtemplatecommand.htm) command. By this means template files can be created that have a fixed content and can be supplemented by fragments that have variable contents. The IMX fragment to be inserted must be well-formed and form a valid XML file together with the template. An IMX fragment can contain all the tags of a template file, with the exception of the <importFragment> tag and only in certain cases the <parameter> tag. The <parameter> tag can only be used under this condition:
     * The import has to be effected through a command that passes an object for the parameter, for example ImportIMXWithTemplateCommand(String pathTemplate, Object projectOrMo, String pathToImx).
The <importFragment/> tag does not have any attributes and any sub-elements. [Example of an IMX file that uses <importFragment/>](javascript:void\(0\);)
    
        <?xml version="1.0" encoding="utf-8"?>
    <!-- Template ImX Import -->
    <imx version="1.0">					
    	<project name="Feeder" save="true" >
    		<libraries>
    			<add type="String" value="T_Mechatronic_ModularSystem"/>
    		</libraries>
    		<mo name="Feeder" typeClass="Feeder" >
    			<importFragment/>
    		</mo>
    	</project>
    </imx>
