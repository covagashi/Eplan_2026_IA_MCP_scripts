---
title: "image(Object contextEO, Object keyEO)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_image_register_image_1.htm"
file: "refformulas_r_image_register_image_1"
category: "refformulas"
---

# image(Object contextEO, Object keyEO)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  image(Object contextEO, Object keyEO) This method returns an image for an object via an image register. image(Object contextEO, Object keyEO)  
---  
Arguments | Object | contextEO | Image register or image register extension that contains the image object.  
Object | keyEO | Absolute path to the project component.  
Return value | image |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=type('absolutePathToRegistry').  
image(this,ref('absolutePathToLookupObjekt').type) | Image of the class object  
Note To display the image object as inactive, the method disable is used (image.disable). As a shortcut the expression disabledimage can also be used.
