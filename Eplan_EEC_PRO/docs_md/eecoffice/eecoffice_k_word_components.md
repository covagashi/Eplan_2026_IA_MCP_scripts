---
title: "Word components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecoffice_k_word_components.htm"
file: "eecoffice_k_word_components"
category: "eecoffice"
---

# Word components

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

Fragment MainDocument

## Word components

Word support has two types of components at its disposal:

     * MainDocument
     * Fragment

Documents are created on the basis of these two objects. Both objects are stored in the Word system library, which must be imported into the current library before the objects can be used (see the following screenshot).

A main document serves as the basis for the desired target document. It defines the underlying structure and contains the basic part of the target document.

Fragments, by contrast, contain individual sentences, paragraphs or sections. In the discipline structure, fragments are attached under the main document. However, they can also be attached to other fragments. This makes it possible to create deeper structures and to dynamically specify document contents.

In order to coordinate a fragment to a position in the discipline structure unambiguously, the structure generator requires guidelines in the form of plug and  socket parameters. These guidelines are described in the section on [Plug-Socket concept](concept_k_plug_socket_concept.htm). Use of the Office discipline assumes familiarity with them.
