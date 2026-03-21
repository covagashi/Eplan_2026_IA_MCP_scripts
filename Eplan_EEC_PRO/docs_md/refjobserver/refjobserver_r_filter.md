---
title: "filter"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refjobserver_r_filter.htm"
file: "refjobserver_r_filter"
category: "refjobserver"
---

# filter

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  filter The <filter> tag defines which files from the Worker should be reacted to when executing this Job definition in the incoming folder. Attribute | Usage | Values | Default value | Description  
---|---|---|---|---  
value | required | *.xls, *.xlsx, *.imx |  |  Specifies which files the Job Server should react to when executing the Job definition. Multiple entries should be separated by the pipe symbol, e.g. *.xls|*.xslx.  
[Example of a file specification that permits all Excel formats.](javascript:void\(0\);)
    
        <filter value="*.xlsx|*.xls" />
