---
title: "\u003cxsl:apply-templates\u003e"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refxml_r_xsl_apply_templates.htm"
file: "refxml_r_xsl_apply_templates"
category: "refxml"
---

# \u003cxsl:apply-templates\u003e

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  <xsl:apply-templates> XSLT The code <xsl:apply-templates> is used to apply templates. In the select attribute, an XPath expression is indicated that selects the node to be processed starting from the current node. The result is a list of nodes (Node Set). The node set is processed element by element and an appropriate template rule is sought for each. Here, the current element in the node set becomes the current node of the process. If there is no template rule, implicit rules are applied. If the select attribute is not indicated, the node set includes all child nodes. This is equivalent to the expression select='child::*' or select='*'. The mode attribute is used to select additional template rules to be applied. [Example code](javascript:void\(0\);)
    
        <xsl:apply-templates select="node-set-expression" mode="node-set-expression">
