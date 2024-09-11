import sys
from functools import reduce

helpFlags = [
    "h",
    "help",
    "?"
]

if __name__ == "__main__":
    argsQuantity = len(sys.argv)
    isHelpFlagTrue = False
    for arg in sys.argv:
        isFlag = arg.startswith(("-", "--", "/"))
        isHelpRequest = reduce(lambda isHelp, helpFlag : isHelp or helpFlag in arg, helpFlags, False)
        if isHelpRequest:
            break
    if isHelpRequest:
        programName = sys.argv[0]
        print(f"Usage: {programName} <inc> <fim> <stp> <rpt>", file=sys.stderr)
        print("inc\t<-- é o tamanho inicial de um vetor de entrada")
        print("fim\t<-- é o tamanho final")
        print("stp\t<-- é o intervalo entre dois tamanhos")
        print("inc\t<-- é o número de repetições a serem realizadas")
        sys.exit(0)
    elif argsQuantity != 5:
        programName = sys.argv[0]
        print(f"Usage: {programName} <inc> <fim> <stp> <rpt>", file=sys.stderr)
        sys.exit(1)
    inc = sys.argv[1]
    fim = sys.argv[2]
    stp = sys.argv[3]
    rpt = sys.argv[4]
