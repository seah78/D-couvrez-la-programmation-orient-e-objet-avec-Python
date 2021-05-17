class CoffeeMachine: 

	WATER_LEVEL=100

	def _start_machine(self):
		if self.WATER_LEVEL > 20:
			return True
		else:
			print("Please add water!")
			return False

	def __boils_water(self):

		return "boiling...."

	def make_coffee(self):

		if self._start_machine():
			self.WATER_LEVEL -= 20
			print(self.__boils_water())
			print("Coffe is ready my dear !")

machine = CoffeeMachine()
#for i in range(0, 5):
#	machine.make_coffee()


print(" Make coffee: Public", machine.make_coffee())
print(" Start machine: protected", machine._start_machine())
print("Boil water : private", machine._CoffeeMachine__boils_water())

print("Boil water : private", machine.__boils_water())
