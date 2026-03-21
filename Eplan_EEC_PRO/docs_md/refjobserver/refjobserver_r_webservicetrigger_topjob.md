---
title: "Calling up a job and placing it directly at the head of the queue"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refjobserver_r_webservicetrigger_topjob.htm"
file: "refjobserver_r_webservicetrigger_topjob"
category: "refjobserver"
---

# Calling up a job and placing it directly at the head of the queue

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Calling up a job and placing it directly at the head of the queue webserviceTrigger A new job can be triggered and set directly at the head of the queue. [Example POST call](javascript:void\(0\);) Request | POST /api/jobs/<job-id>?to=highestPriority  
---|---  
Content-Type | application/json  
Accept | application/json  
Accept-Encoding | gzip, deflate  
Pragma | no-cache  
Body | 
    
        {
    	"params": {
    		"mykey":"1234",
    		"anotherkey":"abcd"
    	}
    }  
  
Note All URL parameters specified are ignored in case of a POST call. The Job object with status information at the moment of generation is given as the response. Further progress information has to be polled. Alternatively, calling of an external Webservice by the Job Server when the Job has been completed under specification of a callback URL is possible. For more information see [Call back by the Job Server](refjobserver_r_webservicetrigger_callback.htm). [Example POST Body with Callback URL](javascript:void\(0\);) Body | 
    
        {
    	"callback": {
    		"href": "http://callbackurl"
    	},
    	"params": {
    		"mykey":"1234",
    		"anotherkey":"abcd"
    	}
    }  
  
---|---
