from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository

class Aplication:
    def __init__(self):
        # Connect to the database
        self._connection = DatabaseConnection()
        self._connection.connect()
        # Seed with some seed data
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        print("Welcome to the music library manager!\n")
        print("What would you like to do?")
        print(" 1 - List all albums")
        print(" 2 - List all artists\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Retrieve all albums
            album_repository = AlbumRepository(self._connection)
            albums = album_repository.all()
            print("Here is a list of albums:")
            for i, album in enumerate(albums, 1):
                print(f" * {i} - {album.title}")
        else:
            # Retrieve all artists
            artist_repository = ArtistRepository(self._connection)
            artists = artist_repository.all()
            print("Here is a list of artists:")
            for i, artist in enumerate(artists, 1):
                print(f" * {i} - {artist.name}")

if __name__ == '__main__':
    app = Aplication()
    app.run()