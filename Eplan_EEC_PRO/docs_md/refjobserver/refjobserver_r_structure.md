---
title: "Structure"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refjobserver_r_structure.htm"
file: "refjobserver_r_structure"
category: "refjobserver"
---

# Structure

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Structure Structure Job definitions are created in XML. The language consists of elements (tags) with nesting rules and of attributes with permitted value assignments. These are described in the following sections. Each tag is enclosed in angle brackets < >. There must be an opening tag, for example <jobdefinition> and a closing tag, for example </jobdefinition>, except for elements that do not enclose content or a sub-element. For elements without content, i.e. without sub-elements, the opening tag also functions as the closing tag, for example <action/>. Attributes control the appearance and behavior of the tag. They are listed within the element, for example <jobdefinition name="'testJob_' + trigger.fileName" model="C:\Users\Public\EPLAN\Models\MyModel.eox"/>. The rules of nesting are stored in the schema file (see [XML transformation]()).. This determines the hierarchy of the tags and which sub-elements are allowed for each element.
