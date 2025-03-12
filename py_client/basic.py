

import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/"

get_responce = requests.get(endpoint, json={"key":"value"} , data= {"name":"somnath"} )

print(get_responce.text )
print(get_responce.status_code)
# print(get_responce.headers)
# print("url",get_responce.url)
# print(get_responce.encoding)
# print(get_responce.elapsed)
# print(get_responce.history)
# print(get_responce.is_redirect)
# print(get_responce.ok)
# print(get_responce.reason)
# print(get_responce.request)

# {
#   "args": {}, 
#   "data": "", 
#   "files": {}, 
#   "form": {}, 
#   "headers": {
#     "Accept": "*/*", 
#     "Accept-Encoding": "gzip, deflate", 
#     "Host": "httpbin.org", 
#     "User-Agent": "python-requests/2.31.0", 
#     "X-Amzn-Trace-Id": "Root=1-67d0401c-26df7979059355e0646fe1e3"
#   }, 
#   "json": null, 
#   "method": "GET", 
#   "origin": "49.37.39.40", 
#   "url": "https://httpbin.org/anything"
# }

# {
#   "args": {}, 
#   "data": "{\"key\": \"value\"}", 
#   "files": {}, 
#   "form": {}, 
#   "headers": {
#     "Accept": "*/*", 
#     "Accept-Encoding": "gzip, deflate", 
#     "Content-Length": "16", 
#     "Content-Type": "application/json", 
#     "Host": "httpbin.org", 
#     "User-Agent": "python-requests/2.31.0", 
#     "X-Amzn-Trace-Id": "Root=1-67d0408a-4c574959151a597714ef99c8"
#   }, 
#   "json": {
#     "key": "value"
#   }, 
#   "method": "GET", 
#   "origin": "49.37.39.40", 
#   "url": "https://httpbin.org/anything"
# }


# {
#   "args": {}, 
#   "data": "", 
#   "files": {}, 
#   "form": {
#     "name": "somnath"
#   }, 
#   "headers": {
#     "Accept": "*/*", 
#     "Accept-Encoding": "gzip, deflate", 
#     "Content-Length": "12", 
#     "Content-Type": "application/x-www-form-urlencoded", 
#     "Host": "httpbin.org", 
#     "User-Agent": "python-requests/2.31.0", 
#     "X-Amzn-Trace-Id": "Root=1-67d04107-35f7ecd77a67f0625bce7d69"
#   }, 
#   "json": null, 
#   "method": "GET", 
#   "origin": "49.37.39.40", 
#   "url": "https://httpbin.org/anything"
# }