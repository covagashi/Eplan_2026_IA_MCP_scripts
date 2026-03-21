---
title: "\u003cxsl:attribute\u003e with value"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refxml_r_xsl_attribute_with_value.htm"
file: "refxml_r_xsl_attribute_with_value"
category: "refxml"
---

# \u003cxsl:attribute\u003e with value

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  <xsl:attribute> with value The following rule creates an attribute name in the target document with the value of the attribute NAME in the original document. [Example code](javascript:void\(0\);)
    
        <xsl:attribute name="name">
    	<xsl:value-of select="NAME">
    </xsl:attribute>
