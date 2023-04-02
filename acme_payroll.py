import sys

from acme_payroll.cli import automatic_processing, manual_processing

def main():
    args = sys.argv[1:]
    if len(args) >= 1:
        manual_processing(args)
    else:
        automatic_processing()


if __name__ == '__main__':
    main()
