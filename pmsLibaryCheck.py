import urllib2 as URL
import xml.etree.ElementTree as ET
import json
purgeDir = " E:\Purge"

content = URL.urlopen("http://127.0.0.1:32400/library/all").read()
root = ET.fromstring(content)
child = root.find("Video")
csvOutput = open('./testfile.csv','w')

csvOutput.write("Title, Rotten Tomato Rating, IMDB, Metascore, File loc \r")

for child in root:
    title = child.attrib.get('title')
    media = child.find("Media").find("Part")
    
    csvOutput.write(title.replace(',','') + ",")
    audienceRatingImage = child.attrib.get('audienceRatingImage')

    if audienceRatingImage != None:
        csvOutput.write(audienceRatingImage.replace("rottentomatoes://image.rating.", "") + "," )
    else:
        csvOutput.write("No Rating Found , ")
    #Open Movie DB
    openMovie = URL.urlopen("http://www.omdbapi.com/?i=&t=" + title.replace(' ', '+') ).read()
    parsed_json = json.loads(openMovie)

    if parsed_json['Response'] == "False":
        csvOutput.write(",")
        csvOutput.write(",")
    else:
        csvOutput.write(parsed_json['imdbRating'] + ",")
        csvOutput.write(parsed_json['Metascore'] + ",")

    csvOutput.write("Move-Item " + media.attrib.get("file")+ purgeDir + ",\r")
    #break
    

csvOutput.close()    
