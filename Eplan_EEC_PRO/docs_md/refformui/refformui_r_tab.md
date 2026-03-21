---
title: "tab"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_tab.htm"
file: "refformui_r_tab"
category: "refformui"
---

# tab

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  tab A <tab> element corresponds to a tab in which a Form-UI is displayed. Each tab displays a title in its title bar to distinguish it from other tabs. A tab can be inserted statically under the <tabbedPane> element or generically via the <loop> element at runtime. In order for an action to be performed when a tab is clicked, the <tabNotifications> element must be inserted (see [tabNotifications](refformui_r_tabnotifications.htm)). The attributes can be calculated using a formula. The formulas are only calculated the first time the Form-UI that contains the <tabbedPane> element is called. If, for example, the value of a tabâs title attribute changes while the tab is being displayed, the title of the tab is not updated. Note Too many UI components and nesting of Form-UIs which is too deep can result in the error message "No more handles". Remedy:
     * Reduce the number of UI components <group>, <line>, <tab> and their child elements.
     * Reduce the nesting depth.
Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
title | required | any |  | Name of the tab  
readonly | optional | true, false |  | true = Tab is read-only.  
false = Input fields on the tab can also be written to.  
Allowed sub-elements | Quantity  
---|---  
[action](refformui_r_action.htm) | any  
[browser](refformui_r_browser.htm) | any  
[group](refformui_r_group.htm) | any  
[img](refformui_r_img.htm) | any  
[include](refformui_r_include.htm) | any  
[input](refformui_r_input.htm) | any  
[instantiation](refformui_r_instantiation.htm) | any  
[label](refformui_r_label.htm) | any  
[line](refformui_r_line.htm) | any  
[loop](refformui_r_loop.htm) | any  
[mailto](refformui_r_mailto.htm) | any  
[open](refformui_r_open.htm) | any  
[progressBar](refformui_r_progressbar.htm) | any  
[pureTable](refformui_r_puretable.htm) | any  
[switch](refformui_r_switch.htm) | any  
[tabbedPane](refformui_r_tabbedpane.htm) | any  
[table](refformui_r_table.htm) | any  
[tabNotifications](refformui_r_tabnotifications.htm) | any  
[td](refformui_r_td.htm) | any
