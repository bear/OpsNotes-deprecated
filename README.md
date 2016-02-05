## OpsNotes
Collection of notes, tools and links relating to Ops

## Command Line
https://github.com/jlevy/the-art-of-command-line

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
