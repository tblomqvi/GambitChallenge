import web
import json
from Parser import Parser

urls = (
	"/","Index",
	"/dump","dump",
)

class Index:
	def GET(self):
		return "Hello world!"
		

class dump:
	def GET(self):
		pars = Parser()
		pars.readFeed()
		data = pars.get_data()
		data_string = json.dumps(data,indent=2)
		return data_string
		

if __name__ == "__main__":
	app = web.application(urls,globals())
	app.run()
	
	#http://localhost:8080/
	#response = requests.get(http://)
	#data = json.loads(response.text)