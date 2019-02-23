import cookielib,urllib,urllib2
zabbix_url="http://www.pythonchallenge.com/pc/return/good.html"
zabbix_header = {"Content-Type":"application/json"}
zabbix_user   = "huge"
zabbix_pass   = "file"

cj = cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
data = urllib.urlencode({"name":zabbix_user,"password":zabbix_pass,'form_refresh':1,'enter':'Sign in'}) 
response = opener.open(zabbix_url,data)
print response.headers
