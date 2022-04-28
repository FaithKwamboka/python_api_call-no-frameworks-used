from flask import Flask
from urllib import request,parse
import json

params={
    "api_key":"e5396e534ae1d9a462751e4e8be2e9be",
    "limit":"5",
    "q":""
}
qrstring=parse.urlencode(params)
print(qrstring)
base_url='https://api.themoviedb.org/3/movie/550?'
req=request.urlopen(base_url+qrstring)
details=parse.urlparse(base_url)
print(details)
print(type(req))

var = req.read()
print(type(var))

dat_=json.loads(var)
print(type(dat_))

jsondata=json.dumps(dat_)
print(type(jsondata))

print(dat_["genres"])