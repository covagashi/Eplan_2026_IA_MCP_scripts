---
title: "Downloading generated files"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refjobserver_r_webservicetrigger_download.htm"
file: "refjobserver_r_webservicetrigger_download"
category: "refjobserver"
---

# Downloading generated files

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Downloading generated files webserviceTrigger The list of created files of the Job can be sampled by the downloads link contained in the Job status. The individual file is then downloaded through the included file link. The files have to be made known to the Job Server during the Job execution by means of the MarkFileForDownloadCommand. [Example GET to the download URI](javascript:void\(0\);) Request | GET /api/jobs/<jobId>/downloads  
---|---  
Accept | application/json  
Accept-Encoding | gzip, deflate  
Pragma | no-cache  
Body | 
    
    
    [
    	{ "title": "proj.px",
    		"links":{
    			"file": {
    				"href": "http://aliasurl/api/jobs/<jobId>/downloads/proj.px"
    			}
    		}
    	},
    	{ "title": "proj1.px",
    		"links":{
    			"file": {
    				"href": "http://aliasurl/api/jobs/<jobId>/downloads/proj1.px"
    			}
    		}
    	}
    ]
