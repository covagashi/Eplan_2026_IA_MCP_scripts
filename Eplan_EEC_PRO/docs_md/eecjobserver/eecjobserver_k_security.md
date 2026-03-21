---
title: "Security precautions"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecjobserver_k_security.htm"
file: "eecjobserver_k_security"
category: "eecjobserver"
---

# Security precautions

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Security precautions

If the Job Server is used in productive operation, certain security precautions have to be taken to ensure that the Job Server cannot be manipulated. The Job Server itself does not provide any protection strategies. In practice a reverse proxy is usually inserted between the Job Server and the Internet / Intranet (for example nginx).

The Job Server communicates with the browser via URLs. The basic idea is to enable or disable these URLs in order to protect the Job Server and ensure its functionality.

A URL is divided into a scheme, host and components (Scheme: http, Host: www.JobServer.de:8080). The components form the path of the URL. This has to be either enabled or disabled. A component can either by a text (for example jobs, bower_components) or a variable (for example {id} a text that changes constantly) or a variable amount of components (for example /bower_components/* means the components bower_components and all components lying behind it).

As a rule the following areas exist:

Job Status

     * Display of the standard Job Status page. The following URLs must be enabled for the Job Status page to function:
        
                /jobs/{id}
        
                /bower_components/*
        
                /api/jobs/{id}
        
                /api/jobs/{id}/downloads/{filename}

     * Display of a self-created Job Status page. The URLs for the standard Job Status page and the following ones have to be enabled:
        
                /custom/html/*

     * Display of the version number in the Job Status page:
        
                /api/version

Create Job

     * Posting of a Job to the Job Server:
        
                /jobs/request/{triggerName}
        
                /api/jobs/request/{triggerName}

Administration page

All the URLs must be enabled for the Administration page. In practice only allowing specific computers or users access to the complete Job Server to administer it has proved to be successful.
