DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Albums;
DROP TABLE IF EXISTS Songs;

CREATE TABLE Artist (
    artist_id INTEGER PRIMARY KEY,
    artist TEXT NOT NULL
);

CREATE TABLE Albums (
    album_id INTEGER PRIMARY KEY,
    artist_id INTEGER NOT NULL REFERENCES Artist(artist_id),
    album_title TEXT NOT NULL
);

CREATE TABLE Songs (
    song_id INTEGER PRIMARY KEY,
    song_title TEXT NOT NULL,
    album_id INTEGER NOT NULL REFERENCES Albums(album_id),
    artist_id INTEGER NOT NULL REFERENCES Artist(artist_id),
    track_number INTEGER NOT NULL,
    track_length TEXT
);
