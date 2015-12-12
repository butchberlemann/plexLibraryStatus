import urllib2 as URL
import xml.etree.ElementTree as ET

content = URL.urlopen("http://127.0.0.1:32400/library/all").read()
root = ET.fromstring(content)
child = root.find("Video")
csvOutput = open('./testfile.csv','w')

csvOutput.write("Title, rating \r")

for child in root:
    csvOutput.write(child.attrib.get('title') + ",")
    audienceRatingImage = child.attrib.get('audienceRatingImage')
    if audienceRatingImage != None:
        if audienceRatingImage.
        csvOutput.write(rating + ",\r")
    else:
        csvOutput.write("No Rating Found ,\r")
    #break

csvOutput.close()    
