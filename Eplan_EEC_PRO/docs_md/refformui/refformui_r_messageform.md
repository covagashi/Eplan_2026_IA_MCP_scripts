---
title: "messageForm"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_messageform.htm"
file: "refformui_r_messageform"
category: "refformui"
---

# messageForm

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  messageForm A <messageForm> is a message window that is displayed as a pop-up. The message window is defined by the title (1), the icon (2), the message text (3) and the buttons (4). The popupForm is called by means of the [open](refformui_r_open.htm) element from within another Form-UI or from a Graph2D diagram. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
id | required | any |  | Unique ID, which is referred to as reference  
title | required | any |  | Name of the Form-UI  
Allowed sub-elements | Quantity  
---|---  
[messageIcon](refformui_r_messageicon.htm) | 0..1  
[messageText](refformui_r_messagetext.htm) | 0..1  
[formButtonArea](refformui_r_formbuttonarea.htm) | 0..1
