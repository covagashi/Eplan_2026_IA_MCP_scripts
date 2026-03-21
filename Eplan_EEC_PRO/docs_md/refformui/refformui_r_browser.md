---
title: "browser"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_browser.htm"
file: "refformui_r_browser"
category: "refformui"
---

# browser

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  browser The <browser> element shows the content of a web site in a browser within a form-UI. Currently the browsers chromium and Internet Explorer can be chosen at present. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
hSize | optional |  |  | Width of the element  
EEC = width in characters  
Web application = width in pixels  
hSizeMax | optional |  |  | maximum width of the element  
EEC = width in characters  
Web application = width in pixels  
hSizeMaxPx | optional |  |  | maximum width of the element in pixels  
hSizeMin | optional |  |  | minimum width of the element  
EEC = minimum width in characters  
Web application = minimum width in pixels  
hSizeMinPx | optional |  |  | minimum width of the element  
EEC = minimum width in pixels  
Web application = minimum width in pixels  
readonly | optional | true, false |  | true = Website content is read-only.  
false = Input can be written to the Website.  
type | optional | webkit, iexplorer | webkit | Browser type  
webkit = chromium (is not supported by 64-bit installation)  
iexplorer = Internet Explorer  
url | required |  |  | URL of the web page to display  
visible | optional | true, false | true | true = element is visible  
true = element is invisible  
vSize | optional |  |  | Height of the element  
EEC = height in characters  
Web application = height in pixels  
Allowed sub-elements | Quantity  
---|---  
none |   
Example for the chromium browser, which displays the web site http://www.eplan.de/?L=1&no_cache=1: [Example code](javascript:void\(0\);)
    
        <form title="Browser" id="browser">
    	<label>Browser</label>
    	<browser type="webkit" url="http://www.eplan.de/en/start/" hSizePx="1000" vSizePx="1200" />
    </form>

Result:
