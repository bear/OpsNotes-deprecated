#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:copyright: (c) 2016 by Mike Taylor
:license: MIT, see LICENSE for more details.

Usage:
    ./logs.py < ~/temp/bear.im.log | jq '. | {method, status}'
    ./logs.py ~/temp/bear.im.log   | jq '. | {method, status}'
"""

import sys
import json
import traceback
import apache_log_parser


if len(sys.argv) > 1:
    source = open(sys.argv[1])
else:
    source = sys.stdin

# These are the format codes that can be used for apache_log_parser
# (taken from the source of apache_log_parser)
#
# %a   Remote IP-address
# %A   Local IP-address
# %B   Size of response in bytes, excluding HTTP headers.
# %b   Size of response in bytes, excluding HTTP headers. In CLF format, i.e. a '-' rather than a 0 when no bytes are sent.
# %D   The time taken to serve the request, in microseconds.
# %f   Filename
# %h   Remote host
# %H   The request protocol
# %k   Number of keepalive requests handled on this connection. Interesting if KeepAlive is being used, so that, for example, a '1' means the first keepalive request after the initial one, '2' the second, etc...; otherwise this is always 0 (indicating the initial request). Available in versions 2.2.11 and later.
# %l   Remote logname (from identd, if supplied). This will return a dash unless mod_ident is present and IdentityCheck is set On.
# %m   The request method
# %p   The canonical port of the server serving the request
# %P   The process ID of the child that serviced the request.
# %q   The query string (prepended with a ? if a query string exists, otherwise an empty string)
# %r   First line of request
# %R   The handler generating the response (if any).
# %s   Status. For requests that got internally redirected, this is the status of the *original* request --- %>s for the last.
# %t   Time the request was received (standard english format)
# %T   The time taken to serve the request, in seconds.
# %u   Remote user (from auth; may be bogus if return status (%s) is 401)
# %U   The URL path requested, not including any query string.
# %v   The canonical ServerName of the server serving the request.
# %V   The server name according to the UseCanonicalName setting.
# %X   Connection status when response is completed:
#        X =   connection aborted before the response completed.
#        + =   connection may be kept alive after the response is sent.
#        - =   connection will be closed after the response is sent.
# %I   Bytes received, including request and headers, cannot be zero. You need to enable mod_logio to use this.
# %O   Bytes sent, including headers, cannot be zero. You need to enable mod_logio to use this.
# Special case of below, for matching just user agent
# %{User-Agent}i

# typical nginx log line
# 217.69.133.226 - - [18/Jan/2016:06:26:33 +0100] "GET /robots.txt HTTP/1.0" 200 170 "-" "Mozilla/5.0 (compatible; Linux x86_64; Mail.RU_Bot/2.0; +http://go.mail.ru/help/robots)" "-"
# 217.69.133.222 - - [18/Jan/2016:06:26:42 +0100] "GET /bearlog/2004/019/football-and-the-internet.html HTTP/1.1" 200 2738 "-" "Mozilla/5.0 (compatible; Linux x86_64; Mail.RU_Bot/2.0; +http://go.mail.ru/help/robots)" "-"
# 192.241.192.83 - - [18/Jan/2016:06:26:47 +0100] "GET /bearlog/ HTTP/1.1" 304 0 "-" "Woodwind (https://github.com/kylewm/woodwind)" "-"

parser = apache_log_parser.make_parser("%h %l %u %t \"%m %r %H\" %s %b")

# loop thru source one line at a time
for line in source:
    try:
        d = parser(line)

        # {'status': '200', 'request_http_ver': '', 'remote_user': '-', 'protocol': 'HTTP/1.1',
        #  'request_first_line': '/bearlog/bearlog.atom',
        #  'remote_logname': '-',
        #  'request_method': '',
        #  'response_bytes_clf': '23657',
        #  'request_url': '',
        #  'remote_host': '107.170.102.81',
        #  'method': 'GET',
        #  'time_received': '[19/Jan/2016:05:58:40 +0100]'
        #  'time_received_isoformat': '2016-01-19T05:58:40',
        #  'time_received_datetimeobj': datetime.datetime(2016, 1, 19, 5, 58, 40),
        #  'time_received_utc_datetimeobj': datetime.datetime(2016, 1, 19, 4, 58, 40, tzinfo='0000'),
        #  'time_received_tz_datetimeobj': datetime.datetime(2016, 1, 19, 5, 58, 40, tzinfo='0100'),
        #  'time_received_tz_isoformat': '2016-01-19T05:58:40+01:00',
        #  'time_received_utc_isoformat': '2016-01-19T04:58:40+00:00',
        # }

        for k in ('time_received_isoformat','time_received_datetimeobj','time_received_utc_datetimeobj',
                  'time_received_tz_datetimeobj','time_received_tz_isoformat','time_received_utc_isoformat'):
            d[k] = '%s' % d[k]
        print json.dumps(d)
    except:
        traceback.print_exc(file=sys.stderr)
