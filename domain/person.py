class Person:
	name: str

	def __init__(self, name: str) -> None:
		self.name = name

	def validate(self) -> bool:
		if self.name == "" or self.name == "Batman":
			return False
		return True

	def add_lastname_rule(self):
		if self.name == "Martin":
			self.name += " Fowler"
