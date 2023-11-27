import sys
from builders.standard_builder import StandardBuilder
from builders.budget_builder import BudgetBuilder
from builders.director import Director

def main() -> str:
    try:
        builder = StandardBuilder()
        director = Director(builder)
        director.build()
        computer = director.computer()
        computer.display()
        
        builder = BudgetBuilder()
        director = Director(builder)
        director.build()
        computer = director.computer()
        computer.display()
    except ValueError as ve:
        return str(ve)

if __name__ == '__main__':
    sys.exit(main())
