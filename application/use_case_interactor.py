from abc import ABCMeta, abstractmethod
from domain.input_data import InputData

class UseCaseInteractor(metaclass=ABCMeta):
	@abstractmethod
	def handle_input_request(self, data: InputData) -> str:
		pass
