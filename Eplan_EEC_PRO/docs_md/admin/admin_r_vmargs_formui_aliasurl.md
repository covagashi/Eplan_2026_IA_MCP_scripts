---
title: "com.mind8.formui.aliasUrl"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_formui_aliasurl.htm"
file: "admin_r_vmargs_formui_aliasurl"
category: "admin"
---

# com.mind8.formui.aliasUrl

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## com.mind8.formui.aliasUrl

The EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dcom.mind8.formui.aliasUrl=<URL> |  Only for Web EEC  
**Annotation**  
Replaces the URL for the download of generated documents. Example:
    
        -Dcom.mind8.formui.aliasUrl=https:\\www.downloads.MyCompany.com

URL for downloads without specification for com.mind8.formui.aliasUrl:
    
        http:\\MyCompany.com

URL for downloads with specification for com.mind8.formui.aliasUrl:
    
        https:\\www.downloads.MyCompany.com
