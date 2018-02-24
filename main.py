from src.checker import Checker
from src.config import Configuration
from src.salutem import Salutem
from src.printer import Printer


if __name__ == '__main__':

    salutem = Salutem()

    print_with_color = True if salutem.args.colored else False

    checker = Checker(
        Configuration('/home/joe/.config/salutem/checks'),
        Printer(print_with_color)
    )

    checker.check()
