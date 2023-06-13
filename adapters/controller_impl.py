from domain.repository import Repository
from domain.input_data import InputData
from adapters.controller import Controller
from application.use_case_interactor import UseCaseInteractor
from application.use_case_interactor_impl import UseCaseInteractorImpl

class ControllerImpl(Controller):
	repository: Repository

	def __init__(self, repository) -> None:
		self.repository = repository

	def convert_raw_data_to_business_data(self, raw_data: dict) -> InputData:
		data = InputData
		data.name = raw_data["name"]
		return data

	def handle_input_request(self, raw_data: dict) -> str:
		data: InputData = self.convert_raw_data_to_business_data(raw_data)
		use_case_interactor: UseCaseInteractor = UseCaseInteractorImpl(self.repository)

		return use_case_interactor.handle_input_request(data)

