class Singer:
    def __init__(self,SingerID,SingerName):
        self.singerID = SingerID
        self.singerName = SingerName

class Song:
    def __init__(self,SongID, SongText):
        self.songID = SongID
        self.songText = SongText
        self.musicDirector = ""
        self.lyricist = ""
        self.singers = []
    def AddSinger(self,Singer):
        self.singers.append(Singer)
    def SetLyricist(self,LyricistName):
        self.lyricist = LyricistName
    def SetMusicDirector(self,MusicDirector):
        self.musicDirector = MusicDirector
class Movie:
    def __init__(self,MovieID,MovieName):
        self.movieID = MovieID
        self.movieName = MovieName
        self.Songs = []
    
    def AddSong(self,Song):
        self.Songs.append(Song)
    def GetSongCount(self):
        return len(self.Songs)
    '''def GetSongCountBySinger(self,singerID):
        count = 0
        for song in self.Songs:
            if(song.SingerID == singerID):
                count = count + 1
        return count'''

class MovieCollection:
    def __init__(self,Movie_List):
        self.MovieList = Movie_List
    def AddMovie(self,Movie):
        self.MovieList.append(Movie)
    def PrintDetails(self):
        count = 0
        for movie in self.MovieList:
            count = count +  movie.GetSongCount()
            print(movie.GetSongCount())
        print("Total songs in the Movie Collection: " ,count)
    def PrintSingerDetails(self, singerID):
        count = 0
        for movie in self.MovieList:
            for song in movie.Songs:
                for singer in song.singers:
                    if singer.singerID == singerID:
                        count =  count + 1
            
        print("Total songs sung by singer: " ,count)
            



objSinger1 = Singer(1,"singer1")
objSinger2 = Singer(2,"singer2")

objSong = Song(1,"songText goes here")
objSong.AddSinger(objSinger1)
objSong.AddSinger(objSinger2)

objSong2 = Song(2,"song2text")
objSong2.AddSinger(objSinger1)

objMovie = Movie(1,"MovieName1")
objMovie.AddSong(objSong)
objMovie.AddSong(objSong2)

print(objMovie.movieName)


MovieList = []
MovieList.append(objMovie)
objCollection = MovieCollection(MovieList)
objCollection.PrintDetails()
objCollection.PrintSingerDetails(1)

objMovie2 = Movie(2,"MovieName2")
objMovie2.AddSong(objSong)
objMovie2.AddSong(objSong2)
MovieList.append(objMovie2)

objCollection2 = MovieCollection(MovieList)
objCollection2.PrintDetails()
objCollection2.PrintSingerDetails(1)