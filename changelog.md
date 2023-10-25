# Precision Feedback Knowledge Base (PFKB) - Changelog
## Version 0.1.0
### 10/24/23
**Improvement:** Added changelog  
- Implementing semantic versioning for PFKB, first step towards initial release
    - Need to have proper version control prior to pilot for rollback protection, work around breaking changes
    - See the governance policy [here][def]

**Improvement:** Added all extant measures used by MPOG to measures definition file  
- Will prevent errors from generating based on the sending of an "improper" measure  
    - Intend to have data pre-processed to avoid informational process and inverse measures
    - Using measures.json to filter (really more elegant error handling) a potential feature >1.0.0 
[def]: https://github.com/Display-Lab/knowledge-base#governance-policy