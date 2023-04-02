import sys

from acme_payroll.cli import automaticProcessing, manualProcessing

def main():
    args = sys.argv[1:]
    if len(args) >= 1:
        manualProcessing(args)
    else:
        automaticProcessing()


if __name__ == '__main__':
    main()
