---
title: "Modularization of text-based documents"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/concept_k_modularization_of_text_based_documents.htm"
file: "concept_k_modularization_of_text_based_documents"
category: "concept"
---

# Modularization of text-based documents

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Modularization of text-based documents

Most of the project documents that are required for constructing machines or facilities are saved in a text-based format (software sources, CAD exchange formats, XML formats from Word, Excel, error text files, BOMs, configuration files, etc.).

Text documents generally consist of a basic document with fixed components and variable text blocks that can be nested in turn. The following diagram provides an example:

[](../Pictures/2006102068.png)

The above example concerns an HTML-based user manual. The HTML document is dissected into text fragments for body, table, and row and transferred to the modular systems. These modular-system components can now be assembled into a project that further illustrates the logical structure of the objects. A table can contain multiple rowsâin this example, row 1 and row 2. The body of the document, in turn, can contain multiple tables. Because a row has ânumberâ and âtextâ parameters, a table can be configured based on components, e.g. for maintenance instructions. Should changes need to be made to the layout of the table, for example, this can be accomplished centrally by correcting the resources of the modular system (HTML fragments).

The mechanism illustrated above makes it possible create project documents, e.g. Word-based documentation, on a modular basis in accordance with company-specific requirements and boundary conditions.

Project documents often have to be created in conformity to highly detailed guidelines and requests (type of table border, cell color, etc.). The advantage of this âfederalâ approach is that detailed structuring of project documents can be accomplished using existing tools (e.g. Word). EEC then uses the existing, often proprietary formats of the original system and restricts itself to modularization.
