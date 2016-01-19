## OpsNotes
Collection of notes, tools and links relating to Ops

### logs.py
```
Usage:
    ./logs.py < ~/temp/bear.im.log | jq '. | {method, status}'
    ./logs.py ~/temp/bear.im.log   | jq '. | {method, status}'
```

Other `jq` queries

```
Filter by IP  | jq '. | select(.remote_host == "217.69.133.226") | {method, status, remote_host}'
```
