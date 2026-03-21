---
title: "-perspective"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_eclipse_args_perspective.htm"
file: "admin_r_eclipse_args_perspective"
category: "admin"
---

# -perspective

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

## -perspective

Eclipse argument |  Values |  Usage  
---|---|---  
-perspective |  perspective identifier |  Optional  
**Annotation**  
At the launch the perspective is opened by default that was open the last time the EEC was closed. Using the argument -perspective, EEC can be controlled in such a way that always a specific perspective is opened, regardless of the last state. Example:
    
        -perspective
    com.mind8.mechatronic.ui.formperspective

For EEC, the following perspectives have been pre-defined: |  Perspective |  ID  
---|---  
Engineering |  com.mind8.mechatronic.ui.engineering.EngineeringPerspektiveFactory  
Project |  com.mind8.mechatronic.ui.project.ProjectPerspectiveFactory  
FormUI |  com.mind8.mechatronic.ui.formperspective
