from abc import ABCMeta, abstractmethod
from adapters.controller import Controller

class GraphicalUserInterface(metaclass=ABCMeta):
	@abstractmethod
	def handle_input_request(self, controller: Controller):
		pass

	@abstractmethod
	def send_data_to_controller(self, data: dict, controller: Controller) -> str:
		pass