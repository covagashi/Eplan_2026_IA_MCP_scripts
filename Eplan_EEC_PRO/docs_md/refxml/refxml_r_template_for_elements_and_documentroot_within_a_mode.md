---
title: "Template for elements and document root within a mode"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refxml_r_template_for_elements_and_documentroot_within_a_mode.htm"
file: "refxml_r_template_for_elements_and_documentroot_within_a_mode"
category: "refxml"
---

# Template for elements and document root within a mode

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Template for elements and document root within a mode The following rule has a mode designated with the mode attribute. With xsl:apply-templates, only the template whose mode is equivalent to the indicated name can be applied by means of the mode attribute. The rule in the example code has the effect that all child notes of the current element are called up. If the style sheet is empty, this causes the source document to be traversed from the root to the leaves. [Example code](javascript:void\(0\);)
    
        <xsl:template match="*|/" mode="m">
    	<!-- Content -->
    </xsl:template>
