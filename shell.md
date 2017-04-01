## Bash tidbits

http://tldp.org/LDP/abs/html/

### Redirection
```
 >  foo.txt    # Redirect stdout
 >> foo.txt    # Redirect and append stdout
2>  foo.txt    # Redirect stderr
2>> foo.txt    # Redirect and append stderr
&>  foo.txt    # Bash 4 - Redirect both stdout and stderr
```

older bash will need ``` > foo.txt 2>&1```

#### Redirect output but fool the app in thinking it's connected to a TTY

Linux
```$ function faketty { script -qfc "$(printf "%q " "$@")" /dev/null; }
$ python -c "import sys; print sys.stdout.isatty()"
True
$ python -c "import sys; print sys.stdout.isatty()" | cat
False
$ faketty python -c "import sys; print sys.stdout.isatty()" | cat
True
```

OS X
```script -q /dev/null python -c "import sys; print sys.stdout.isatty()" | cat```
