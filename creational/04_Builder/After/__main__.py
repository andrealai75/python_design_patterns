import sys
from computer import Computer

def main() -> str:
    try:
        print("Building a Computer.")
        computer = Computer(case = 'Coolermaster',
                            mainboard='MSI',
                            cpu = 'Intel Core 19',
                            memory = '2 X 160GB',
                            hard_drive = 'SSD 2TB',
                            video_card = 'GeForce')
        computer.display()
    except ValueError as ve:
        return str(ve)

if __name__ == '__main__':
    sys.exit(main())
