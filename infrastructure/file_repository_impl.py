from domain.repository import Repository
from domain.person import Person

class FileRepositoryImpl(Repository):
	def connect(self) -> bool:
		print("Connecting...")
		return True

	def close(self) -> bool:
		print("Closing...")
		return True

	def save_person(self, person: Person) -> bool:
		print("Saving...")
		return True