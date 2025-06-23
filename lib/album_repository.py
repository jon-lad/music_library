from lib.album import Album

class AlbumRepository:
    def __init__(self, connection) -> None:
        self.connection = connection
    
    def all(self):
        self.connection.connect()
        rows = self.connection.execute("SELECT * FROM albums")
        albums = []
        for row in rows:
            albums.append(Album(row["id"], row["title"], row["release_year"], row["artist_id"]))

        return albums
    
    def find(self, album_id):
        self.connection.connect()
        rows = self.connection.execute('SELECT * FROM albums WHERE id = %s', [album_id])
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])