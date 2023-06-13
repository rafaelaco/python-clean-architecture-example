from domain.input_data import InputData
from domain.repository import Repository
from domain.person import Person
from application.use_case_interactor import UseCaseInteractor

class UseCaseInteractorImpl(UseCaseInteractor):
	repository: Repository

	def __init__(self, repository: Repository) -> None:
		self.repository = repository

	def handle_input_request(self, data: InputData) -> str:
		person: Person = Person(data.name)

		if person.validate() != True:
			exit("The name is invalid!")

		person.add_lastname_rule()
		self.repository.save_person(person)

		return person.name