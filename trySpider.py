from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import urllib.response
import re
import pandas

title_buf = []
result = {}
temp1 = []
temp2 = []
temp3 = []
salary = []

def urlMainpulate():
	url = ["http://www.jobs.ac.uk/search/?category=0800&sort=gl&show=25&s={}".format(str(i)) for i in range(1 ,2000 ,25)]
	return url

def searchdata():
	link = urlMainpulate()
	url = []

	for link_list in link:
		req = urllib.request.Request(link_list)
		response = urllib.request.urlopen(req)
		html = response.read()
		html = html.decode("utf-8")
		soup = BeautifulSoup(html, "html.parser")
		buf = soup.select(".text > a")
		key = re.compile('(.*)</a>')
		buff = key.findall(str(buf))
		for each in buff:
			temp1.append(each.strip())
		buf = soup.select(".employer")
		key2 = re.compile('(.*)</div>')
		temp_buf = key2.findall(str(buf))
		for each in temp_buf:
			temp2.append(each.strip())
		buf = soup.select('.department')
		key3 = re.compile('(.*)</div>')
		temp_buf = key3.findall(str(buf))
		for each in temp_buf:
			temp3.append(each.strip())
		buf = soup.select('.info')
		key4 = re.compile('(.*)</div>')
		temp_buf = key4.findall(str(buf))
		##print(temp_buf)
		for each in temp_buf:
			salary.append(each.strip())
		buf = soup.select('.text > a')
		for each in buf:
			url.append(each.get('href'))
		temp4 = []
		for each in url:
			temp4.append('http://www.jobs.ac.uk'+ str(each))

	result['department'] = temp3.copy()
	result['title'] = temp1.copy()
	result['employer'] = temp2.copy()
	result['salary'] = salary.copy()
	result['url'] = temp4.copy()

searchdata()

obj = pandas.DataFrame(result)
print(obj)
#obj.to_csv('C:\\Users\\Silver\\Desktop\\data.csv')