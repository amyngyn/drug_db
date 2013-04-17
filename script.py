import csv

def readFile(filename):
    drugs = dict()
    f = open(filename, 'r')
    for line in f:
        drugs[line.strip()] = []
    return drugs

# TODO: Edit the script arguments to pass in which columns to look at
# As of right now, the assumption is that the fourth column contains keys
# and the fifth column contains values (Also, ignores all other columns)
def readValues(drugDict, valuesTSV):
    with open(valuesTSV, 'r') as values:
        for row in csv.reader(values, delimiter="\t"):
            drugName = row[3]
            adverseEffect = row[4]
            if drugName in drugDict and adverseEffect not in drugDict[drugName]:
                drugDict[drugName].append(adverseEffect)

def writeDrugs(drugs):
    sideEffectFile = open('sideeffects.txt', 'w')
    foundDrugsFile = open('founddrugs.txt', 'w')

    for drugName in drugs:
        if len(drugs[drugName]) == 0:
            foundDrugsFile.write(drugName + "\t0\n")
        else:
            foundDrugsFile.write(drugName + "\t1\n")
            for adverseEffect in drugs[drugName]:
                sideEffectFile.write(drugName + "\t" + adverseEffect + "\n")

    sideEffectFile.close()
    foundDrugsFile.close()

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print "usage: python script.py drugList.txt adverseEffects.tsv"
        sys.exit(0)

    drugs = readFile(sys.argv[1])
    readValues(drugs, sys.argv[2])
    writeDrugs(drugs)
