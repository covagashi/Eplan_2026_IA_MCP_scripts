---
title: "img"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_img.htm"
file: "refformui_r_img"
category: "refformui"
---

# img

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  img The element <img> inserts a picture. The image can be referenced as external or internal resource. Similarly, references to image registers (image objects) can be used to display different images depending on the object type (class or instance object). Note Path specifications to external picture files are evaluated like formulas, which is why they have to be enclosed in single quotation marks. Allowable paths specifications are:
    
        <img src="'T:/image.png'">
    <img src="='T:/image.png'">
    <img src="'images/image.png'">
    <img src="='images/image.png'">
    <img src="'T:\\image.png'">
    <img src="='T:\\image.png'">
    <img src="'images\\image.png'">
    <img src="='images\\image.png'">

Servers cannot be referenced by, for example, <img src="'//SRV01.MyDomain.local/images/image.png'">. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
src | required | absolute or relative path |  | absolute or relative path to an external image, starting from the installation directory or path to the image object of the internal image  
tooltip | optional |  |  | Text or Form-UI of the overlaying tooltip (see [tooltip](refformui_r_tooltip.htm))  
visible | optional | true,false | true | true = image is visible  
true = image is invisible  
Allowed sub-elements | Quantity  
---|---  
[tooltip](refformui_r_tooltip.htm) | 0..1  
Image objects can be manipulated by methods. These methods can be combined. Method | Example | Example code  
---|---|---  
disable |  | <img src="type('Documentation_UI_Configuration.ProjectLibrary.HelpObjects.Images.delta_abc').image.disable"/>  
flipH |  | <img src="type('Documentation_UI_Configuration.ProjectLibrary.HelpObjects.Images.delta_abc').image.flipH"/>  
flipV |  | <img src="type('Documentation_UI_Configuration.ProjectLibrary.HelpObjects.Images.delta_abc').image.flipV"/>  
rotate180 |  | <img src="type('Documentation_UI_Configuration.ProjectLibrary.HelpObjects.Images.delta_abc').image.rotate180"/>  
rotate270 |  | <img src="type('Documentation_UI_Configuration.ProjectLibrary.HelpObjects.Images.delta_abc').image.rotate270"/>  
rotate90 |  | <img src="type('Documentation_UI_Configuration.ProjectLibrary.HelpObjects.Images.delta_abc').image.rotate90"/>  
scale |  | <img src="type('Documentation_UI_Configuration.ProjectLibrary.HelpObjects.Images.delta_abc').image.scale(2)"/>  
Note For new Form-UIs should only references on image objects be used. Specification of an absolute path to an external picture file: [Example code](javascript:void\(0\);)
    
        <line>
    	<img src="='C:\\Users\\Public\\EPLAN\\
    	EngineeringConfiguration\\2_4_20140218_0227\\install\\
    	icon-collection\\Rumpf.png'"/>
    </line>

Result: Relative path to an external image file: [Example code](javascript:void\(0\);)
    
        <line>
    	<img src="='pics/action.png'"/>
    </line>

Result: Reference on an internalized image file (see also [image](refformulas_r_image_objects_method_image.htm)): [Example code](javascript:void\(0\);)
    
        <line>
    	<img src="type('Documentation_UI_Configuration.
    	ProjectLibrary.HelpObjects.Images.delta_abc').image"/>
    </line>

Result: Reference on an image register to display the image of a class object (see also [image](refformulas_r_image_objects_method_image.htm)): [Example code](javascript:void\(0\);)
    
        <line>
    	<img src="type('Documentation_UI_Configuration.
    	ProjectLibrary.HelpObjects.Images.nav_next').
    	image(this,ref('Documentation_UI_Configuration.
    	Mechatronic.Documentation').type)"/>
    </line>

Result: Reference on an image register to display the image of an instance object (see also [image](refformulas_r_image_objects_method_image.htm)): [Example code](javascript:void\(0\);)
    
        <line>
    	<img src="type('Documentation_UI_Configuration.
    	ProjectLibrary.HelpObjects.Images.nav_next').
    	image(this,ref('Documentation_UI_Configuration.
    	Mechatronic.Documentation'))"/>
    </line>

Result:
