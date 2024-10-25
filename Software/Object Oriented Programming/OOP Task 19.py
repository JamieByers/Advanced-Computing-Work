class Track:
    def __init__(self, title, artist) -> None:
        self._title = title
        self._artist = artist

    def getTitle(self):
        return self._title
    
    def getArtsit(self):
        return self._artist 
    
    def setTitle(self, title):
        self._title = title

    def setArtist(self, artist):
        self._artist = artist


