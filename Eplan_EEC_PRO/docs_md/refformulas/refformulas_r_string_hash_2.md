---
title: "hash(String hashAlgorithm)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_string_hash_2.htm"
file: "refformulas_r_string_hash_2"
category: "refformulas"
---

# hash(String hashAlgorithm)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  hash(String hashAlgorithm) String methods Returns the hash value of a character string as a hex string according to the selected hash algorithm. hash(String hashAlgorithm)  
---  
Argument | String | MD2  
MD5  
SHA-1  
SHA-256  
SHA-384  
SHA-512 | Hash algorithm to be used to create the hash value  
Return value | Hex string | Character string of the hash value  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=Feeder.Mechatronic.Feeder.name.hash('SHA-512') | 28c9e70c91f6890ca9e7e5a4ae1c587bdd9cb615bb24d0a0ace6a533e80487d0b258ba67e28fc61ed14593a3bba3f76e3fa94fb6adc2c1f1366004e42cd395dc
