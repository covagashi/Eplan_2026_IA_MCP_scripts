---
title: "action"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_action.htm"
file: "refformui_r_action"
category: "refformui"
---

# action

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  action Clicking the <action> element initiates a defined action or a component method.  
     * Action: An action must be compiled in the library. The action must contain a run method.
     * Component method: For a library component, methods are defined in the methods editor. These can be called in the <action> element by prefixing the method name with a colon (<action name=":Method_name"/>).
There are two types of component methods:
     * Instance methods (Static=false): The self object in the code of a method points to the project component.
     * Class method (Static=true): The self object in the code of a method points to the library component here.
If there is no instance method for the method call to apply, a suitable class method is sought. Both the run method of the action and the component method receive their parameters via the Arguments attribute. The arguments are to be transferred as a list. An action can be represented as a text with the appearance of a hyperlink and a preceding image or as a button with an image. The default image of the action is replaced by the img attribute (see also [img](refformui_r_img.htm)). Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
arguments | optional | List |  | List of arguments which are passed to the run method of the action  
bColor | optional | 0,0,0 to 255,255,255 | System color | Background color as RGB value  
fColor | optional | 0,0,0 to 255,255,255 | System color | Font color as RGB value for type="link"  
font | optional | Font name-style-size | System font | Font name, style, and size for displaying text  
hSize | optional |  |  | Width of the element  
EEC = width in characters  
Web application = width in pixels  
hSizeMax | optional |  |  | maximum width of the element  
EEC = width in characters  
Web application = width in pixels  
hSizeMax | optional |  |  | maximum width of the element  
EEC = width in characters  
Web application = width in pixels  
hSizeMaxPx | optional |  |  | maximum width of the element  
EEC = width in pixels  
Web application = width in pixels  
hSizeMaxPx | optional |  |  | maximum width of the element  
EEC = width in pixels  
Web application = width in pixels  
hSizeMin | optional |  |  | minimum width of the element  
EEC = width in characters  
Web application = width in pixels  
hSizeMinPx | optional |  |  | minimum width of the element in pixels  
hSizePx | optional |  |  | Width of the element in pixels  
id | required | any |  | Unique ID, which is referred to as reference  
img | optional | png, gif, jpg | action.png | assigns another image to the element  
name | required |  |  | absolute name of the action  
readonly | optional | true, false | false | true = action is disabled  
false = action is enabled  
refresh | optional | true, false | true | Element is rebuilt after each modification of the EO  
showIcon | optional | true, false | true | true = icon is visible  
false = icon is not visible  
text | optional |  |  | the text to display can be calculated using the formula language  
tooltip | optional |  |  | Text or Form-UI of the overlaying tooltip (see [tooltip](refformui_r_tooltip.htm))  
type | optional | link, button | link | Representation type of the action:  
link = text with hyperlink  
button = button  
visible | optional | true, false | true | true = element is visible  
true = element is invisible  
vSize | optional |  |  | Height of the element  
EEC = height in characters  
Web application = height in pixels  
vSizeMax | optional |  |  | maximum height of the element  
EEC = height in characters  
Web application = height in pixels  
vSizeMaxPx | optional |  |  | maximum height of the element in pixels  
vSizeMin | optional |  |  | minimum height of the element  
EEC = height in characters  
Web application = height in pixels  
vSizeMinPx | optional |  |  | minimum height of the element in pixels  
vSizePx | optional |  |  | Height of the element in pixels  
Allowed sub-elements | Quantity  
---|---  
[tooltip](refformui_r_tooltip.htm) | 0..1  
Action as hyperlink with yellow background: The element is displayed with preceding default image as a hyperlink on yellow background. The action ShowReadmeAction is executed, whose absolute name is specified: [Example code](javascript:void\(0\);)
    
        <action **name="Documentation_UI_Configuration.ProjectLibrary.HelpObjects.ShowReadmeAction" type="link"** bColor="255,255,0" font="Arial-bold-12">show readme</action>

Result: Action as a hyperlink with tooltip: The element is displayed with preceding default image and tooltip as a hyperlink: [Example code](javascript:void\(0\);)
    
        <action name="**Documentation_UI_Configuration.ProjectLibrary.HelpObjects.ShowReadmeAction** " **type="link"** font="Arial-bold-12" **tooltip="open readme"** >show readme</action>

Result: Action as a button: The element is displayed as a button with default image: [Example code](javascript:void\(0\);)
    
        <action name="**Documentation_UI_Configuration.ProjectLibrary.HelpObjects.ShowReadmeAction** " **type="button"** >show readme</action>

Result: Action as a disabled button: The element is configured as a button with default image, but is displayed disabled by means of the attribute readonly: [Example code](javascript:void\(0\);)
    
        <action **readonly="true"** text="='show readme'" name="**Documentation_UI_Configuration.ProjectLibrary.HelpObjects.ShowReadmeAction** " type="button"/>

Result: Action as a link passes two arguments: The element is defined as a link with text. Two arguments are passed, the value of the parameter Coordinate (0, 90, 180 or 270) and the project component this. The action determines a direction from the parameter value that is passed and writes it to the parameter CardinalPoints. [Example code](javascript:void\(0\);)
    
        <form id="coordinate" title="coordinate">  
     <input receiver="=parameter('Coordinate')" type="text"></input>  
     <action   
     type="link"  
     arguments="=List{$Coordinate, this}"  
     name="**Documentation_UI_Configuration.ProjectLibrary.HelpObjects**.  
    CalculateCoordinateAction">  
     </action>  
     <label text="=$CardinalPoints"></label>  
    </form>

Result: The action CalculateCoordinateAction in this example calls the Command CalculateCoordinate , which has been previously created specially for this purpose. The following figure shows the method view of the command editor. Two arguments are defined (1) in it and the transfer of the arguments is implemented in Java code (2) of the Command. The command is called by this action: Calling an instance method: The sample code illustrates a call to the CalculateCoordinate method of the Docu_UI_Configuration project component. Two arguments are passed, the value of the parameter Coordinate (0, 90, 180 or 270) and the project component this. The action determines a cardinal direction from the parameter value that is passed and writes it to the CardinalPoints parameter. [Example code](javascript:void\(0\);)
    
        <form id="CalculateCoordinate" title="Calculate coordinate with instance method">
    	<input receiver="=parameter('Coordinate')" type="text"></input>
    	<action type="link"
    	showImg="true"
    	**arguments="=List{$Coordinate, this}"**
    	img="=type('Documentation_UI_Configuration.ProjectLibrary.HelpObjects.Images.action').image"
    	**name=":CalculateCoordinate"** >  
    </action>
    	<label text="=$CardinalPoints"></label>
    	<progressBar bColor="255,255,0" font="Arial-bold_10" type="both" visible="true" />
    </form>

Result:
