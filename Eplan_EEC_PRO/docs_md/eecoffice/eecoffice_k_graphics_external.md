---
title: "External images"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecoffice_k_graphics_external.htm"
file: "eecoffice_k_graphics_external"
category: "eecoffice"
---

# External images

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## External images

All images are designated as external images when they are stored on the file system and are inserted in the main document or fragment per reference. At the moment of generation of the project document, the referenced image must be available on the file system.

Two different parameter sequences are available to reference an image:

Parameter sequence 1: #{ImagePath:Parameter name}

This parameter sequence should not be used anymore for new projects because it requires that an image with a resolution of 100 DPI is available. If the image is available in a different resolution, the expansion of the image in the Word document does not match the expectations. If the resolution of the image corresponds to 100 DPI, it is inserted with a scaling of 100% into the document. The parameter of the type ImagePath must contain an absolute path to an image file.

Parameter sequence 2: #{ImageInfo:Parametername}

The parameter of the type ImageInfo must include a map with special key-value pairs:

Key | Value | Description  
---|---|---  
SourceImagePath | <absolute path> | Absolute path to the image file  
SourceImageVerticalResolutionInDPI | Integer | Vertical resolution of the image in DPI. Without this parameter EEC tries to read this value from the meta information of the image file.  
WordDocumentPageWidthInCM | Double | Width of the Word document in cm. For example, a value of 21.0 has to be specified for an A4 document.  
WordDocumentPageHeightInCM | Double | Height of the Word document in cm. For example, a value of 29.7 has to be specified for an A4 document.  
WordDocumentMarginLeftInCM | Double | Left margin in cm.  
WordDocumentMarginRightInCM | Double | Right margin in cm.  
FitToDocumentWidth | Boolean |  Adjust the image to the width of the document. true = Adjust the image size to the document width false = Do not adjust the image size to the document width  
WordDocumentDestinationScaleHorizontalInPercent | Integer | Horizontal scaling of the image in per cent.  
WordDocumentDestinationScaleVerticalInPercent | Integer | Vertical scaling of the image in percent.  
WordDocumentDestinationRotation |  Right Left |  Rotation of the image by 90 degrees. Right = Rotation clockwise Left = Rotation counterclockwise  
  
### Note

The Word_Customizing library must be imported in order to use the ImagePath and ImageInfo types. The library is provided with the file <EEC installation folder>\install\other\model\Word_Customizing.eox.

The following figure shows a fragment with a parameter sequenced for an external image:
