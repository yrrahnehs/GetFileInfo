import sys
import os


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
# Creates a new file with those lines
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


def keywordcount(fromstring, tostring, newfilename):
    try:
        file = open(sys.argv[1], "r")
        newfile = open(newfilename, "w+")
        line_count = 0
        for line in file:
            target = line[line.find(fromstring) + len(fromstring): line.find(tostring)]
            if target in line:
                stringtowrite = str(target) + ": 1 \n"
                if os.stat(sys.argv[1]).st_size == 0:
                    newfile.write(stringtowrite)
                    return
                if target not in newfile:
                    newfile.write(stringtowrite)
        file.close()
        print(f"The file has", line_count, "lines")
        return
    except FileNotFoundError:  # when file can not be found
        print("File not found")
    except FileExistsError:
        print("File already exists")
    except:  # handle other exceptions such as attribute errors
        print("Unexpected error:", sys.exc_info()[0])


# Returns the number of lines in a file
#   example: /getfileinfo.py <filepath> -keyword <keyword> <newFileName>
#   Argv[1] = file path OR "-help"
#   Argv[2] = "-keyword" | "-keycount"

if __name__ == '__main__':
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

    elif sys.argv[2] == "-keycount":
        if len(sys.argv) == 6:
            keywordcount(sys.argv[3], sys.argv[4], sys.argv[5])
        elif len(sys.argv) != 6:
            print("Invalid amount of arguments")
