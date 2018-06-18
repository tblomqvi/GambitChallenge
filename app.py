import web
import json
from Parser import Parser

urls = (
	"/","Index",
	"/dump","dump",
)

class Index:

	def __init__(self):
		self.render = web.template.render("templates/")
	
	def GET(self):
		pars = Parser()
		pars.readFeed()
		data = pars.get_data()
		return self.render.page(data)
		

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