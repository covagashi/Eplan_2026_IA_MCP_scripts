---
title: "XML editor for Form-UIs and diagram definitions"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/gui_k_editors_xml_editor_for_formui_and_diagramdefinitions.htm"
file: "gui_k_editors_xml_editor_for_formui_and_diagramdefinitions"
category: "gui"
---

# XML editor for Form-UIs and diagram definitions

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  XML editor for Form-UIs and diagram definitions An internal XML editor is available for creating Form-UIs and diagram definitions. The editor offers two views Source and Design of the XML document. Source: The source view (see the following figure) corresponds to an XML editor with code highlighting and content assist. Code highlighting: Code highlighting is used to represent text passages of the diagram definition in different colors, for example, command names (tags) green, attribute names purple, attribute values blue, and content black (see above figure). The colors can be chosen freely in the settings under XML > XML files > Editor > Syntax Coloring (see the following figure). Content assist: The content assist function substantially speeds up the input of formulas, tag and attribute names, as well as attribute values, while minimizing the number of typos at the same time. For example, the input of < followed by the key combination [CTRL] + [Space] brings up a selection of possible tag names that are permitted in the current position. If the proposal is adopted via the [Enter] key, the Content Assistant will insert the selected tag and also the closing tag. When inputting formulas, the Content Assistant lists the available methods and parameters after inputting a period using the key combination [CTRL] + [Space]. The names of the parameters available in the superordinate component are listed for integrated components. To list the parameter names of the superordinate component in the Content Assistant for pre-instantiated (integrated) components, .mc$ (1) must be entered before the Content Assistant is called (Ctrl + Space). All available parameters of the superordinate component are listed in here (2). The Content Assistant function behaves the same way when entering attribute values. As soon as the attribute name is entered, the Content Assistant will show a list of permissible attribute values. But this works only if it involves a pre-defined selection of attribute values, for example, for the attribute align a list with center, left and right is displayed (see the following figure). Design: The XML document for the Form-UI (see the following figure) or a diagram definition is displayed in a table in a structured form. The left column shows the elements, attributes, etc. in the hierarchical order, and the right column contains the relevant values and / or contents. Each entry in the left table column can be distinguished easily by the symbol. The following table lists the different symbols: Symbol | Meaning  
---|---  
| Element  
| Attribute  
| Comment  
| Processing instruction  
| PCDATA  
| CDATA  
This editor view is controlled entirely via the popup menu. In line with the respective element highlighted in the left column of the table, the popup menu offers a number of possibilities.
