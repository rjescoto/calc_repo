#unit test the calculator lib

import calculator

class testCalculator:

    def testr_add(self):
        assert 4 == calculator.add(1,3)

    def testr_add(self):
        assert 2 == calculator.sub(4,2)