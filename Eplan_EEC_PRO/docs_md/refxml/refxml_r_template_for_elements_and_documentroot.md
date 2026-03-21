---
title: "Template for elements and the document root"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refxml_r_template_for_elements_and_documentroot.htm"
file: "refxml_r_template_for_elements_and_documentroot"
category: "refxml"
---

# Template for elements and the document root

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Template for elements and the document root The following rule has the effect that all child notes of the current element are called up. If the style sheet is empty, this causes the source document to be traversed from the root to the leaves. [Example code](javascript:void\(0\);)
    
        <xsl:template match="*|/">
    	<!-- Content -->
    </xsl:template>
