# middleman-dev

## Assumption

- Middleman is based on mitmproxy. Take a glance at https://docs.mitmproxy.org/stable/

## Setup

```
git clone https://github.com/ddetox/middleman-dev.git
cd middleman-dev
docker-compose up &
docker attach middleman-dev # run at another tab after you see "Attaching" message in the prompt
```

## Submit Filters

- put filter.py and manifest.json into a new directory and zip it up.
- submit the zip file at https://middleman.market/developer/apply_filter
