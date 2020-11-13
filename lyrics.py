import requests
import json

key = "&apikey=d7691f610c3add51456994dad5cc561f"
rooturl = " https://api.musixmatch.com/ws/1.1/"
whateverThisIs = "&page_size=3&page=1&s_track_rating=desc"


foundSong = False

while foundSong == False: 
    songQuery = input("Enter a song to find a lyrics to: ")
    trackResponse = requests.get(rooturl + "track.search?q_track=" + songQuery + whateverThisIs + key)
    if(trackResponse.json()["message"]["header"]["available"] == 0):
        print("No Songs Found")
    else: 
        trackObject = trackResponse.json()["message"]["body"]["track_list"][0]["track"]
        trackID= trackObject["commontrack_id"]
        
        lyricsObject = requests.get(rooturl + "track.lyrics.get?commontrack_id="+str(trackID)+ whateverThisIs + key)
        
        trackName = trackObject["track_name"]
        trackArtist = trackObject["artist_name"]
        trackAlbum = trackObject["album_name"]
        
        statusCode=lyricsObject.json()["message"]["header"]["status_code"]
        
        if(statusCode != 200):
            print("We couldn't find that song")
        else:
            foundSong = True
            print("Putting lyrics for " + trackName + " By " + trackArtist + " From " + trackAlbum)
            print(lyricsObject.json()["message"]["body"]["lyrics"]["lyrics_body"])