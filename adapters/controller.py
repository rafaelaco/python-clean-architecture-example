from abc import ABCMeta, abstractmethod
from domain.input_data import InputData

class Controller(metaclass=ABCMeta):
	@abstractmethod
	def convert_raw_data_to_business_data(self, raw_data: dict) -> InputData:
		pass

	@abstractmethod
	def handle_input_request(self, raw_data: dict) -> str:
		pass
