---
title: "open"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_open.htm"
file: "refformui_r_open"
category: "refformui"
---

# open

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  open The element <open> opens a Form-UI page or an Internet page. The element can be represented by an image by means of the img attribute (see also [img](refformui_r_img.htm)). For the representation of a link as a button it is possible to use a shortcut in order to follow the link without clicking (see also [Shortcuts](refformui_r_shortcuts.htm)). The text for a link can comprise the text defined with the attribute text and the text between the opening tag and the closing tag. The text of the attribute and the text between the tags is delimited by a space and any spaces, tabs and line breaks that may be present are removed. If the component exists but the reference with ref="Reference-ID" is wrong or not existing, an appropriate error message is displayed (see the following figure). Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
bColor | optional, only for type = link | 0,0,0 to 255,255,255 | System color | Background color as RGB value  
fColor | optional, only for type = link | 0,0,0 to 255,255,255 | System color | Font color as RGB value  
font | optional | Font name-style-size | System font | Font name, style, and size for displaying text  
hSizeMax | optional |  |  | maximum width of the element  
EEC = width in characters  
Web application = width in pixels  
hSizeMaxPx | optional |  |  | maximum width of the element  
EEC = width in pixels  
Web application = width in pixels  
img | optional | png, gif, jpg |  | assigns another image to the element  
readonly | optional | true, false |  | true = element is disabled  
false = element is enabled  
receiver | required |  |  | Formula to the object  
ref | required | Form-UI ID, URL |  | shows the Form-UI page whose ID or the website whose URL is specified  
text | optional |  |  | the text to display  
tooltip | optional |  |  | Text or Form-UI of the overlaying tooltip (see [tooltip](JavaScript:TL_1902310.HHClick\(\)))  
type | required | button, link, doubleclick | link | Representation type of the placeholder:  
button = button  
link = text as a hyperlink  
doubleclick = Label with a link to the Form-UI  
visible | optional | true, false | true | true = the included element is visible  
false = the included element is invisible  
Allowed sub-elements | Quantity  
---|---  
[tooltip](refformui_r_tooltip.htm) | 0..1  
[dialog](refformui_r_dialog.htm) | 0..1  
[command](refformui_r_command.htm) | 0..1  
A hyperlink opens another Form-UI page in the editor of the same EO: The receiver attribute has the value this, which opens the referenced Form-UI in the same editor. [Example code](javascript:void\(0\);)
    
        <open type="link" receiver="this" ref="start">Go to page &quot;Structure&quot;</open>

Result: A hyperlink whose text is displayed in a different color, opens another Form-UI page: The receiver attribute has the value mos, which opens the referenced Form-UI in a new editor. By means of the fColor attribute the hyperlink text is displayed in a different color. [Example code](javascript:void\(0\);)
    
        <open fColor="255,0,0" type="link" receiver="mos('Station')" ref="docu">Go to Station</open>

Result: A hyperlink whose background is displayed in a different color, opens another Form-UI page: The receiver attribute has the value mos, which opens the referenced Form-UI in a new editor. By means of the bColor attribute the hyperlink background is displayed in a different color. [Example code](javascript:void\(0\);)
    
        <open bColor="255,0,0" type="link" receiver="mos('Station')" ref="docu">Go to Station</open>

Result: A button opens a Form-UI page in the editor of another EO: The receiver attribute has the value mos('Station'), which opens the referenced Form-UI page in the editor of the EO 'Station'. [Example code](javascript:void\(0\);)
    
        <open type="button" receiver="mos('Station')" tooltip="Tooltip an Open" ref="docu">Go to Station</open>

Result: A disabled hyperlink to open a Form-UI in a different editor: If the readonly attribute is set to true, the hyperlink is disabled. [Example code](javascript:void\(0\);)
    
        <open type="link" readonly="true" receiver="mos('Station')" ref="docu">Go to Station</open>

Result: A hyperlink opens a website: A hyperlink within a line of text should link to an Internet page. [Example code](javascript:void\(0\);)
    
        <line>
    	<label>Click on the following</label>
    	<open ref="http://www.test.de">link</open>
    	<label>to open the internet test page</label>
    </line>

Result: A complex hyperlink with parameters for the target page: The formula parameter('Parameter').value returns a value, that is passed to the page as param. [Example code](javascript:void\(0\);)
    
        <open text="='order' + $Parameter" ref="='http://www.anywhere/site.asp?param=' + parameter('Parameter').value + '&amp;param2=' + parameter('Parameter2').value">link</open>

Result: Displayed text: order value1 Underlying link: [http://www.anywhere/site.asp?param=value1&param2=value2](http://www.anywhere/site.asp?param=value1&param2=value2) In a pureTable, it should be possible to access Form-UIs by double-clicking the label: The target of the link is specified by the receiver attribute, and the ID of the Form-UI to be opened is specified by the ref attribute. A Tooltip appears in the pureTable when the mouse is moved over an entry in the âStationâ column. Double-clicking next to the Tooltip but within the table cell opens up the linked Form-UI. [Example code](javascript:void\(0\);)
    
        <form id="Stations" title="stations">
    	<pureTable receiver="=mos('Documentation_UI_Configuration.ProjectLibrary.HelpObjects.Station')" variable="x">
    		<column heading="No.">
    			<label text="=mos('Documentation_UI_Configuration.ProjectLibrary.HelpObjects.Station').indexOf(x)+1"></label>
    		</column>
    		<column heading="Station" hSizeMinPx="150">
    			<open type="doubleclick" text="=x.name" receiver="x" ref="docu"></open>
    		</column>
    	</pureTable>
    </form>

Result:
