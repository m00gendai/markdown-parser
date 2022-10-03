from html_tags import htmlTags

newlines = []
openTag = []
closeTag = []

for tag in htmlTags:
    openTag.append(tag.replace(">", ""))
    cTag = tag + "\n"
    closeTag.append(cTag.replace("<", "</"))

with open('test.txt') as inputFile:
    lines = inputFile.readlines()

for element in lines:
# Post title
    if element.startswith("### "): 
        element = element.replace("### ", "<h1>")
        element = element.replace(" \n", "") + "</h1>"
        newlines.append(element)
# Post chapter title
    elif element.startswith("<chapter "): 
        element = element.replace("<chapter ", "<chapter title={")
        element = element.replace(">\n", "") + "} />"
        newlines.append(element)
# Gallery grid component
    elif element.startswith("<gallery "): 
        element = element.replace("<gallery ", "<gallery grid={")
        element = element.replace(">\n", "") + "} />"
        newlines.append(element)
# HTML5 tags
    elif (element.startswith(tuple(openTag)) and element.endswith(tuple(closeTag))) or (element.startswith(tuple(openTag)) and element.endswith("/>\n")):
        newlines.append(element)
# Paragraphs
    else:
        element = "<p>" + element.replace('\n', '') + "</p>"
        newlines.append(element)

inputFile.close()

outputFile = open("index.js", "w")

for line in newlines:
    outputFile.write(line + "\n")
    
outputFile.close()
