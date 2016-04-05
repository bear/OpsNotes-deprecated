Nginx

## Install

### OS X

```
brew tap homebrew/nginx
brew install nginx-full
```

- Lua Support `--with-lua-module --with-set-misc-module` 
- SSE / Push Support `--with-push-stream-module`

## CORS Support 
(from dan on HangOps (aka dcondomitti on GitHub)

```
# Match against all example.com domains and subdomains in
    # http and https
    if ($http_origin ~* (https?://[^/]*\.example\.com)) {
        set $cors "true";
    }
    if ($cors = "true") {
      # Allow all example.com hostnames
      add_header 'Access-Control-Allow-Origin' "$http_origin";
      add_header 'Access-Control-Allow-Methods' 'HEAD, GET, POST, OPTIONS';

    }
    if ($request_method = 'OPTIONS') {
      set $cors  "${cors}+OPTS";
    }
    if ($cors = "true+OPTS") {
      add_header 'Access-Control-Allow-Origin' "$http_origin";
      add_header 'Access-Control-Allow-Methods' 'HEAD, GET, POST, OPTIONS';

      # Tell client that this pre-flight info is valid for 20 days
      add_header 'Access-Control-Max-Age' 1728000;
      add_header 'Content-Type' 'text/plain charset=UTF-8';
      add_header 'Content-Length' 0;

      return 204;
    }
  ```
