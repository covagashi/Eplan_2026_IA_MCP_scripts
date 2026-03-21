---
title: "Form-UI elements: Overview"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_o_overview.htm"
file: "refformui_o_overview"
category: "refformui"
---

# Form-UI elements: Overview

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Form-UI elements: Overview Form-UI element | Area | Description  
---|---|---  
[uis](refformui_r_uis.htm) | Structure | The Form-UI element <uis> is the top-level element.  
[form](refformui_r_form.htm) | Structure | Each Form-UI element <form> appears as a separate editor page of the instance editor.  
[tabbedPane](refformui_r_tabbedpane.htm) | Structure | Multiple Form-UIs can be displayed in a single editor as tabs by using the <tabbedPane> element.  
[tab](refformui_r_tab.htm) | Structure | A <tab> element corresponds to a tab in which a Form-UI is displayed.  
[messageForm](refformui_r_messageform.htm) | Structure | A <messageForm> is a message window that is displayed as a pop-up.  
[fileSelectionForm](refformui_r_fileselectionform.htm) | Structure | A <fileSelectionForm> is used for file selection.  
[messageIcon](refformui_r_messageicon.htm) | Structure | The <messageIcon> element defines the type of message window by assigning a specific icon.  
[messageText](refformui_r_messagetext.htm) | Structure | The <messageText> element defines the text displayed in the message window, which is either a normal text or the result of a formula.  
[pathLocation](refformui_r_pathlocation.htm) | Structure | The element <pathLocation> encompasses the definition of the file extensions permissible for the file selection.  
[fileFilters](refformui_r_filefilters.htm) | Structure | The element <fileFilters> encompasses the definition of the file extensions permissible for the file selection.  
[ext](refformui_r_ext.htm) | Structure | The element <ext> defines with the attribute name a permissible file extension for the file selection window.  
[fileButtonArea](refformui_r_filebuttonarea.htm) | Structure | The element <fileButtonArea> encloses the definition of the buttons for a file selection window.  
[formContentArea](refformui_r_formcontentarea.htm) | Structure | The <formContentArea> element encloses the definition of a Form-UI which is displayed in a popup window.  
[cancelButton](refformui_r_cancelbutton.htm) | Structure | Displays the [Cancel] button in the title bar of a messageForm.  
[noButton](refformui_r_nobutton.htm) | Structure | Displays the [No] button in the title bar of a messageForm.  
[okButton](refformui_r_okbutton.htm) | Structure | Displays the [OK] button in the title bar of a messageForm.  
[yesButton](refformui_r_yesbutton.htm) | Structure | Displays the [Yes] button in the title bar of a messageForm.  
[group](refformui_r_group.htm) | Placement and grouping | By means of the Form-UI element <group>, the elements nested by this tag are grouped.  
[line](refformui_r_line.htm) | Placement and grouping | The Form-UI element <line> arranges sub-elements in one line of the Form-UI.  
[gap](refformui_r_gap.htm) | Placement and grouping | The Form-UI element <gap> creates a defined distance with the pixel unit between two Form-UI elements, which are located in one line (element <line>).  
[label](refformui_r_label.htm) | Field types | The element <label> inserts a text.  
[input](refformui_r_input.htm) | Field types | The <input> element inserts a simple input field, a drop-down list box, a radio button, a check box or a button with toggle function, which serves for either entering a value or selecting one.  
[progressBar](refformui_r_progressbar.htm) | Field types | The <progressBar> element inserts a progress bar.  
[table](refformui_r_table.htm) | Tables | The element <table> inserts a table into the Form-UI.  
[colGroup](refformui_r_colgroup.htm) | Tables | The element <colGroup> groups columns, which are superordinate set to the same properties.  
[col](refformui_r_col.htm) | Tables | The <col> element determines the properties for one or more table columns.  
[rowGroup](refformui_r_rowgroup.htm) | Tables | The element <rowGroup> groups rows, which are superordinate set to the same properties.  
[row](refformui_r_row.htm) | Tables | The <row> element determines the properties for one or more table rows.  
[td](refformui_r_td.htm) | Tables | The element <td> inserts a table cell.  
[pureTable](refformui_r_puretable.htm) | Tables | The element <pureTable> is used to display large amounts of data in a table.  
[column](refformui_r_column.htm) | Tables | The <column> element is exclusively used for the configuration of columns within <pureTable>.  
[filters](refformui_r_filters.htm) | Tables | The <filters> element activates the filters for displaying the determined values of the created <pureTable> table.  
[columnFilter](refformui_r_columnfilter.htm) | Tables | The <columnFilter> element configures one filter per table column within <pureTable>.  
[img](refformui_r_img.htm) | Images | The element <img> inserts a picture.  
[tree](refformui_r_tree.htm) | Tree structure |  The <tree> element is used to display project components in a tree structure.  
[treeNode](refformui_r_treenode.htm) | Tree structure | The <treeNode> element defines subordinate project components to be displayed in the tree structure.  
[treeNotifications](refformui_r_treenotifications.htm) | Tree structure | The <treeNotifications> element is only implemented in a tree structure when a trigger event occurs that is supposed to execute an action, e.g. when a user clicks a project component.  
[action](refformui_r_action.htm) | Actions | Clicking the <action> element initiates a defined action or a component method.  
[tabNotifications](refformui_r_tabnotifications.htm) | Actions | Serves as a container for any number of elements declared by trigger events for actions to be executed.  
[onEnter](refformui_r_onenter.htm) | Actions | Declares the trigger event for an action to be performed when opening.  
[onClickEvent](refformui_r_onclickevent.htm) | Actions | Declares the trigger event for an action to be performed when a mouse click occurs.  
[performEvent](refformui_r_performevent.htm) | Actions | Defines the action to be performed.  
[loop](refformui_r_loop.htm) | Loops and conditions | To iterate consecutively multiple times over Form-UI elements, they are enclosed by the loop element <loop>.  
[switch](refformui_r_switch.htm) | Loops and conditions | The element <switch> with at least one sub-element <case> and one sub-element <default> formulates one or more conditions for displaying either input fields or labels in a column of the pureTable.  
[case](refformui_r_case.htm) | Loops and conditions | A condition is formulated with every <case> sub-element.  
[default](refformui_r_default.htm) | Loops and conditions | With the sub-element <default>, a sub-element (<input> or <label>) must be specified, which is displayed in the column of the pureTable if the previous conditions are not satisfied.  
[instantiation](refformui_r_instantiation.htm) | Placeholders | The <instantiation> element is used to instantiate objects on placeholders.  
[include](refformui_r_include.htm) | Nesting | The element <include> inserts the content of a Form-UI at the place where the element tag <include> is positioned.  
[open](refformui_r_open.htm) |  Navigation | The element <open> opens a Form-UI page or an Internet page.  
[link](refformui_r_link.htm) | Navigation | The <link> element opens a Form-UI page.  
[dialog](refformui_r_dialog.htm) | Navigation | The <dialog> element configures a modal dialog window to display a Form-UI page.  
[command](refformui_r_command.htm) | Navigation | By means of the <command> element enclosed by the <dialog> element before opening and after closing as well as by clicking the buttons [OK], [Cancel], [Yes] and [No] actions, resp. commands are executed.  
[browser](refformui_r_browser.htm) | Web pages | The <browser> element shows the content of a web site in a browser within a form-UI.  
[mailto](refformui_r_mailto.htm) | E-mail | The element <mailto> creates a new e-mail by means of the locally installed mail client.  
[tooltip](refformui_r_tooltip.htm) | Tooltips | The element <tooltip> creates a tooltip, that appears as a pop-up window.  
[inputValidators](refformui_r_inputvalidators.htm) | Validation | The element <inputValidators> encompasses the specific elements <numberRangeValidator>, <contentValidator>, or <keyValidator> for validation of the input in a text box or a drop-down box.  
[numberRangeValidator](refformui_r_numberrangevalidator.htm) | Validation | In this type of validation, the content that has been input is converted into a number and compared with the specifications for the lower limit (attribute start) and upper limit (attribute end).  
[contentValidator](refformui_r_contentvalidator.htm) | Validation | In this type of validation, the input content is compared with the given specifications by means of a regular expression.  
[keyValidator](refformui_r_keyvalidator.htm) | Validation | This type of validation compares each letter while entering with the specification of a regular expression.
