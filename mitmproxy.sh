#/bin/sh

dir=`pwd`
docker run --rm -it --name middleman-dev -p 8080:8080 -v ${dir}/certs:/home/mitmproxy/.mitmproxy -v ${dir}:/src mitmproxy/mitmproxy mitmproxy -s /src/loader.py