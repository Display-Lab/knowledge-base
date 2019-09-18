# Useful CLI commands

## Get list of all preconditions

Use program `jq` to 
```sh
jq -s '[ .[]."@graph"[]."slowmo:HasPrecondition"[] ] | unique' causal_pathways/*.json
```

## Consolidate all causal pathways into a single graph
```sh 
jq -s '{ "@context": ([ .[]."@context" ] | unique | .[0]), "@graph":[ .[]."@graph"[] ]}' causal_pathways/*.json
```
