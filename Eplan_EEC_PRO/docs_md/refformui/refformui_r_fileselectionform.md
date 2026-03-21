---
title: "fileSelectionForm"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_fileselectionform.htm"
file: "refformui_r_fileselectionform"
category: "refformui"
---

# fileSelectionForm

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  fileSelectionForm A <fileSelectionForm> is used for file selection. The file selection window is called by means of the <open> element and the ID of the window. The selected file can be processed directly by a script or the absolute name can be passed to a parameter. The title (see **1** in the figure File selection window) and the selectable file type (see 2 in File selection window) can be defined for the file selection window. The fileSelectionForm is called by using the element [open](refformui_r_open.htm) from another Form-UI or from a Graph2D diagram. The representation of the file selection window differ depending on whether it is started in a desktop or Web EEC installation.  
     * In the case of a desktop installation a Windows standard dialog is displayed that supports standard functions, for example file filters.
     * In the case of a Web EEC installation a window is displayed that supports uploading of the file to be selected. In it the selected file is listed (**2** in the following figure) and the upload to the server is visualized with a progress bar (**3** in the following figure) and a status display (**1** in the following figure). The actual file selection takes place as an intermediate step in a Windows standard dialog that is started via a button (**4** in the following figure).
If the [Cancel] button is not to execute any action, it need not be explicitly shown in the fileButtonArea. An action should always be provided for the [OK] button. For the action that is triggered upon actuating a button, no argument need be provided in the list of arguments for the run() method for the selected file path (see figure File path for action). EEC will append the absolute path to the selected file as the last argument before the run() method of the action is called. It is merely ensured that the transferred filename is the same as the one that is returned by <fileSelectionForm>. Note In a Client/Server environment, the path of the client side is replaced by a temporary path on the server side - for example, the client-side c:\test\BOM.csv becomes, on the server side, c:\tmp\33568991\BOM.csv. Note In a Web EEC environment an upload file is stored in a temporary file below <Tomcat_Installation Path>\temp. This folder is called fileupload_<Session_Number>. Note The associated temporary folder is deleted by terminating or exiting a session. The data in the temporary folder are then no longer available for any generations of target data possibly started beforehand. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
id | required | any |  | Unique ID, which is referred to as reference  
title | required | any |  | Name of the Form-UI  
Allowed sub-elements | Quantity  
---|---  
[fileButtonArea](refformui_r_filebuttonarea.htm) | 0..1  
[fileFilters](refformui_r_filefilters.htm) (not for Web EEC) | 0..1  
[pathLocation](refformui_r_pathlocation.htm) (not for Web EEC) | 0..1  
  
[Example code](javascript:void\(0\);)
    
        <form id="openSelectFileForm" title="Open file window">
    	<open ref="FileSelectionFormUI" type="link" receiver="=this" >Open file selection window </open>
    </form>
    <fileSelectionForm id="FileSelectionFormUI" title="Open File" >
    	<pathLocation text="C:\" />
    	<fileFilters>
    		<ext name="*.csv" />
    		<ext name="*.mdb" />
    	</fileFilters>
    	<fileButtonArea>
    		<okButton>
    			<performEvent
    				name="Documentation_UI_Configuration.ProjectLibrary.HelpObjects.ImportFileDataAction"
    				arguments="=List{$selectionReceiver}" />
    		</okButton>
    		<cancelButton></cancelButton>
    	</fileButtonArea>
    </fileSelectionForm>

Result:
