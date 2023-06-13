from abc import abstractmethod, ABCMeta
from domain.person import Person

class Repository(metaclass=ABCMeta):
	@abstractmethod
	def connect(self) -> bool:
		pass

	@abstractmethod
	def close(self) -> bool:
		pass

	@abstractmethod
	def save_person(self, person: Person) -> bool:
		pass

