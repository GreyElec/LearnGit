import urllib.request
import urllib.parse


Trans = input("Please give the sentences:")
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
data = dict()
data["from"] = "AUTO"
data["to"] = "AUTO"
data["smartresult"] = "dict"
data["client"] = "fanyideskweb"
data["i"] = "helloworld"
data["doctype"] = "json"
data["version"] = "2.1"
data["keyfrom"] = "fanyi.web"
data["action"] = "FY_BY_REALTIME"
data["typoResule"] = "true"

data = urllib.parse.urlencode(data).encode("utf-8")
response = urllib.request.urlopen(url, data)
html = response.read().decode("utf-8")
print(html)
