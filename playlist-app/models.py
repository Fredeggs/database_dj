"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    __tablename__ = "playlists"

    def __repr__(self):
        p = self
        return f"<Playlist id={p.id} name={p.name} description={p.description}>"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(300))

    playlist_song = db.relationship("PlaylistSong", backref="playlist")
    song = db.relationship("Song", secondary="playlist_song", backref="playlists")


class Song(db.Model):
    """Song."""

    __tablename__ = "songs"

    def __repr__(self):
        s = self
        return f"<Song id={s.id} title={s.title} artist={s.artist}>"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    artist = db.Column(db.Text, nullable=False)

    playlist_song = db.relationship("PlaylistSong", backref="song")
    playlist = db.relationship("Playlist", secondary="playlist_song", backref="songs")


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = "playlist_song"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey("playlists.id"), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey("songs.id"), primary_key=True)


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
