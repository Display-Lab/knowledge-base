# Useful CLI commands

## Get list of all preconditions

Use program `jq` to 
```sh
jq -s '[ .[]."@graph"[]."slowmo:HasPrecondition"[] ] | unique' causal_pathways/*.json
```
