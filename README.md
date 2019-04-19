# middleman-dev

## Assumption

Middleman is based on mitmproxy. Take a glance at https://docs.mitmproxy.org/stable/

## Setup

```
git clone https://github.com/ddetox/middleman-dev.git
cd middleman-dev
sh mitmproxy.sh
```

`sh mitmdump.sh` is also available for development.

## install your root certificate

```
open certs/mitmproxy-ca.pem
```

## setup proxy

- host:localhost
- port:8080

## Submit Filters

- put filter.py and manifest.json into a new directory and zip it up.
- submit the zip file at https://middleman.market/developer/apply_filter
