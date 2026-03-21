---
title: "Calling up jobs (without callback)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refjobserver_r_webservicetrigger_jobcall.htm"
file: "refjobserver_r_webservicetrigger_jobcall"
category: "refjobserver"
---

# Calling up jobs (without callback)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Calling up jobs (without callback) webserviceTrigger The Job can be triggered by calling a URL in the browser (HTTP GET) or via an HTTP Webservice call (HTTP POST). Any key-value pairs can be included in sending via the URL parameter (HTTP GET) or in the Request body (HTTP POST). These are accessed in the job definition via trigger.params. You can also transfer the data in the form of a JSON structure. [Example GET call](javascript:void\(0\);)  
      
        [http://aliasurl/jobs/request/myjob?mykey=1234&anotherkey=abcd](http://aliasurl/jobs/request/myjob?mykey=1234&anotherkey=abcd)

The progress page for the created Job is displayed as the response. [Example POST call](javascript:void\(0\);) Request | POST /api/jobs/request/WebShopNoOutput HTTP/1.1  
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
  
[Example POST call transfers JSON data](javascript:void\(0\);) Request | POST /api/jobs/request/WebShopNoOutput HTTP/1.1  
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
    },
    	"json": {
    		"OrderHeader":{
    			"Name":"Order1234"
    		},
    		"OrderPos":{
    			"Number":"20210203"
    		}
    	}
    }  
  
The contents of the JSON data is saved in a parameter as Map with key-value pairs. The name of the parameter has to be named in the model variables under Commands > SetParameterValueFromJsonCommand > Name of the parameter which stores the JSON structure and the parameter by the same has to be installed in the corresponding component. Note All URL parameters specified are ignored in case of a POST call. The Job object with status information at the moment of generation is given as the response. Further progress information has to be polled. Alternatively, calling of an external Webservice by the Job Server when the Job has been completed under specification of a callback URL is possible. For more information see [Call back by the Job Server](refjobserver_r_webservicetrigger_callback.htm). [Example POST Body with Callback URL](javascript:void\(0\);) Body | 
    
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
