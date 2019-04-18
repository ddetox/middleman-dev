#/bin/sh

dir=`pwd`
docker run --rm -it --name middleman-dev -p 8080:8080 -v ${dir}/certs:/home/mitmproxy/.mitmproxy -v ${dir}/src:/src mitmproxy/mitmproxy mitmdump -s /src/filter.py