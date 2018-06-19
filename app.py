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
		user_data = web.input(id=[])
		pars = Parser()
		pars.readFeed()
		data = pars.get_data(user_data.id)
		return self.render.page(data)
		

class dump:
	def GET(self):
		user_data = web.input(id=[])
		pars = Parser()
		pars.readFeed()
		data = pars.get_data(user_data.id)
		data_string = json.dumps(data,indent=2)
		return data_string
		

if __name__ == "__main__":
	app = web.application(urls,globals())
	app.run()
	