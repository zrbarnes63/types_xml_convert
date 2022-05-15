"""
FILE: CONVERT_TYPES_XML.PY
AUTHOR: ZACH BARNES
DATE: 5/14/2022

PROGRAM TO MODIFY THE TYPES.XML (STORED AS TXT) OF THE WINDSTRIDERCLOTHINGPACK TO BE COMPATIABLE WITH NAMALSK TYPES.XML

"""
import re

INNAME = "types.xml"
OUTNAME = "types_new.xml"

def main():
    with open(INNAME, 'r') as inFile:
        with open(OUTNAME, 'w') as outFile:
            for line in inFile:
                checkUsage = re.search("<usage", line)
                checkFlags = re.search("<flags", line)
                if checkFlags != None:
                    outFile.write(line)
                    usageLine = valLine = re.split('<', line)
                    usageLine[1] = "usage />\n"
                    usageLine = '<'.join(usageLine)
                    outFile.write(usageLine)
                    valLine[1] = "value />\n"
                    valLine = '<'.join(valLine)
                    outFile.write(valLine)
                elif checkUsage != None:
                    line = re.split("\"", line)
                    # which clothing type
                    if (line[1] == "Town"):
                        line[1] = "civilian"
                    elif (line[1] == "Village"): # since Town and Village both == civilian, just remove village so no duplicate civilians tags are inserted
                        line = ""                
                    elif (line[1] == "Police"):
                        line[1] = "police"
                    elif (line[1] == "Military"):
                        line[1] = "military"
                    elif (line[1] == "Hunting"):
                        line[1] = "hunting"
                    elif (line[1] == "Coast"):
                        line[1] = "fishing"
                    else:
                        print("Didnt find match for %s", line[1])

                    line = "\"".join(line)
                    line = re.sub('<usage', '<tag', line)

                    outFile.write(line)
                else:
                    outFile.write(line)
    print("end")

if __name__ == "__main__":
    main()