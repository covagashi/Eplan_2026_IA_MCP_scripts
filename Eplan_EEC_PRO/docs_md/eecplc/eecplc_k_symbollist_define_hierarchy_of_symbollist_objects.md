---
title: "Definition of the hierarchy of the symbol-list objects"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_symbollist_define_hierarchy_of_symbollist_objects.htm"
file: "eecplc_k_symbollist_define_hierarchy_of_symbollist_objects"
category: "eecplc"
---

# Definition of the hierarchy of the symbol-list objects

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Definition of the hierarchy of the symbol-list objects

As with other disciplines, the discipline structure here must be defined first. As already mentioned above, the following hierarchy levels must be defined for the symbol list at a minimum. Body and line. In some cases, an intermediate level may be necessary for block formation, although this task is often realizable without additional levels.

The hierarchy is already predefined for the STEP 7 and CoDeSys platforms, and the corresponding system objects are already available. The text discipline is available for all other platforms, but naturally for STEP 7 and CoDeSys as well. As usual, abstract mechatronic objects are used there to define the structure levels, and the hierarchy is specified in the level configuration editor. The procedure is identical to the one already described for the ECAD discipline.

Independently of the platform, parts of the documents created in the generic system are used as resources for modeling, and must be prepared with this in mind. This work basically consists in analytically dividing the original document into elementary parts. The structuring of the document is crucial here. The tasks are outlined in the following paragraphs, including platform-specific aspects.
