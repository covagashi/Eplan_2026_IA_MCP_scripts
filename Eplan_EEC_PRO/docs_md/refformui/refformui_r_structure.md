---
title: "Structure"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_structure.htm"
file: "refformui_r_structure"
category: "refformui"
---

# Structure

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Structure Form-UIs are created in the XML language. The language consists of elements (tags) with nesting rules and of attributes with permitted value assignments. These are described in the following sections. Each tag is enclosed in angle brackets < >. There must be an opening tag, for example <table> and a closing tag, for example </table>, except for elements that do not enclose a content or a sub-element. For elements with no content, resp. without sub-element is the opening tag also the closing, such as <input/>. Attributes control the appearance and behavior of the element. They are listed within the tag, for example <input type="combo" receiver="this"/>. The nesting rules are stored in the schema file (see chapter XML-Schema for Form-UI). This determines the hierarchy of the elements and which sub-elements are allowed for an element.
