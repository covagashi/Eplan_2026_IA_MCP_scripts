---
title: "dialog"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_dialog.htm"
file: "refformui_r_dialog"
category: "refformui"
---

# dialog

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  dialog The <dialog> element configures a modal dialog window to display a Form-UI page. Prior to continuing in the main window, the dialog window must be closed. The element is configured as a subelement of <open>. With the buttons attribute buttons are shown in the dialog window to initiate actions resp. commands. Actions or commands may be executed by means of the <command> sub-element before opening and after closing (see [command](refformui_r_command.htm)). Clicking [OK] must always execute an action, whereas executing an action is optional for [CANCEL], [YES] and [NO]. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
buttons | optional | ok, cancel, yes, no |  | Displays buttons in the dialog window, which are used to execute actions. Several buttons are separated by '|', e.g. buttons="ok|cancel".  
ok = Ok  
cancel = Cancel  
yes = Yes  
no = No  
hSize | optional |  |  | Width of the element  
EEC = width in characters  
Web application = width in pixels  
hSizeMax | optional |  |  | maximum width of the element  
EEC = width in characters  
Web application = width in pixels  
hSizeMin | optional |  |  | minimum width of the element  
EEC = minimum width in characters  
Web application = minimum width in pixels  
visible | optional | true, false | true | true = label is visible  
false = label is invisible  
vSize | optional |  |  | Height of the element  
EEC = height in characters  
Web application = height in pixels  
vSizeMax | optional |  |  | maximum height of the element  
EEC = maximum height in characters  
Web application = maximum height in pixels  
vSizeMin | optional |  |  | minimum height of the element  
EEC = minimum height in characters  
Web application = minimum height in pixels  
title | optional |  |  | Formula for the text to be displayed as the title of the dialog.  
Allowed sub-elements | Quantity  
---|---  
[command](refformui_r_command.htm) | any  
A button opens a modal dialog, which displays another Form-UI page. At starting and also at closing the dialog an action is executed: [Example code](javascript:void\(0\);)
    
        <form title="Dialog" id="dialog">
    	<open text="='open dialog'" type="button" ref="modaldialog">
    		**< dialog title="=****'Modal dialog Title Text****'" buttons="ok|cancel" >**
    			<command event="ok" name="Documentation_UI_Configuration.ProjectLibrary.HelpObjects.okAction" />
    			<command event="cancel" name="Documentation_UI_Configuration.ProjectLibrary.HelpObjects.cancelAction" />
    		</dialog>
    	</open>
    </form>
    <form id="modaldialog" title="Modal Dialog">
    	<label>[OK] closes the modal dialog and executes the action "okAction"</label>
    	<label>[Abbrechen] closes the modal dialog and executes the action "cancelAction"</label>
    </form>

Result:
