import sys
from collections import OrderedDict
import collections


# Counts the number of lines in a file
def countlines():
    try:
        file = open(sys.argv[1], "r")
        line_count = 0
        for line in file:
            if line != "\n":
                line_count += 1
        file.close()
        print(f"The file has", line_count, "lines")
        return
    except FileNotFoundError:  # when file can not be found
        print("File not found")
    except:  # handle other exceptions such as attribute errors
        print("Unexpected error:", sys.exc_info()[0])


# Counts the number of lines that has the keyword
# Creates a new file called newfilename with those lines
def keywordlines(keyword, newfilename):
    try:
        file = open(sys.argv[1], "r")
        newfile = open(newfilename, "x")
        line_count = 0
        for line in file:
            if keyword in line:
                newfile.write(line)
                line_count += 1
        file.close()
        print(f"The file has", line_count, "lines")
        return
    except FileNotFoundError:  # when file can not be found
        print("File not found")
    except FileExistsError:
        print("File already exists")
    except:  # handle other exceptions such as attribute errors
        print("Unexpected error:", sys.exc_info()[0])


# Counts the occurrences of the string between fromstring and tostring
# and creates a new file called newfilename with the results
def keybetween(fromstring, tostring, newfilename):
    try:
        targetlist = []
        file = open(sys.argv[1], "r")
        newfile = open(str(newfilename), "w+")

        for line in file:
            firstword = line.find(fromstring) + len(fromstring)
            rest = line[firstword:]
            secondword = rest.find(tostring)
            target = rest[0:secondword]
            if target in line and fromstring in line:
                targetlist.append(target)
        file.close()

        counts = collections.Counter(targetlist)
        sortedlist = sorted(targetlist, key=lambda x: -counts[x])

        uniqueids = list(OrderedDict.fromkeys(sortedlist))

        for i in uniqueids:
            amt_of_occurrences = targetlist.count(i)
            finalstring = "{}: {} \n".format(i, amt_of_occurrences)
            newfile.write(finalstring)

        print(f"The file has", len(uniqueids), "unique lines")

        return
    except FileNotFoundError:  # when file can not be found
        print("File not found")
    except FileExistsError:
        print("File already exists")


# Returns the number of lines in a file
#   example: /getfileinfo.py <filepath> -keyword <keyword> <newFileName>
#   Argv[1] = file path OR "-help"
#   Argv[2] = "-keyword" | "-between" | "-amount"

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Invalid arguments")
        sys.exit(0)

    if len(sys.argv) == 2:
        if sys.argv[1] == "-help":
            print(f"getfileinfo <filepath> [-keyword <keyword> <newFileName> |"
                  f" -keycount <from> <to> <newFileName>]")
        else:
            countlines()

    elif sys.argv[2] == "-keyword":
        if len(sys.argv) == 5:
            keywordlines(sys.argv[3], sys.argv[4])
        elif len(sys.argv) != 5:
            print("Invalid amount of arguments")

    elif sys.argv[2] == "-between":
        if len(sys.argv) == 6:
            keybetween(sys.argv[3], sys.argv[4], sys.argv[5])
        elif len(sys.argv) != 6:
            print("Invalid amount of arguments")

    else:
        print("Invalid amount of arguments, use -help for more info")
