import urllib2 as URL
import xml.etree.ElementTree as ET
import json
purgeDir = " E:\Purge"

content = URL.urlopen("http://127.0.0.1:32400/library/all").read()
root = ET.fromstring(content)
child = root.find("Video")
csvOutput = open('./testfile.csv','w')

movieLibList = []

csvOutput.write("Title, Rotten Tomato Rating, IMDB, Metascore, File loc \r")


for child in root:
    movie = []
    title = child.attrib.get('title')
    media = child.find("Media").find("Part")
    rottonTomato = ""
    imdbRating = ""
    metascore = ""
    
    csvOutput.write(title.replace(',','') + ",")
    audienceRatingImage = child.attrib.get('audienceRatingImage')

    if audienceRatingImage != None:
        rottonTomato = audienceRatingImage.replace("rottentomatoes://image.rating.", "") + ","
        csvOutput.write(rottonTomato )
        
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
