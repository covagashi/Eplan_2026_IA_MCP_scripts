---
title: "Nesting elements and attributes"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refxml_r_nesting_elements_and_attributes.htm"
file: "refxml_r_nesting_elements_and_attributes"
category: "refxml"
---

# Nesting elements and attributes

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Nesting elements and attributes XSLT The following rule creates two elements, one with a name attribute with the value ' Hello_World'in the target document. [Example code](javascript:void\(0\);)
    
        <xsl:element name="mo">
    	<xsl:element name="mo2">
    		<xsl:attribute name="name">
    			<xsl:value-of select="'Hello_World'" />
    		</xsl:attribute>
    	</xsl:element>
    </xsl:element>

Result of example code in IMX format:
    
        <mo>
    	<mo2 name='Hello_World' />
    </mo>
