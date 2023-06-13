from adapters.controller import Controller
from infrastructure.graphical_user_interface import GraphicalUserInterface
from flask import Flask, request
from flask_restful import Resource, Api

todos = {}

class WebServer(Resource):
	gui: GraphicalUserInterface
	controller: Controller

	def post(self):
		json_raw_data = request.json
		response = self.gui.send_data_to_controller(json_raw_data, self.controller)
		return {"message": response}

class WebApiImpl(GraphicalUserInterface):
	def handle_input_request(self, controller: Controller):
		app = Flask(__name__)
		api = Api(app)
		webServer = WebServer
		webServer.gui = self
		webServer.controller = controller
		api.add_resource(webServer, '/input')
		app.run(debug=True)

	def send_data_to_controller(self, data: dict, controller: Controller) -> str:
		return controller.handle_input_request(data)
