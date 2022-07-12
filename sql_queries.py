#!/usr/bin/python
# -*- coding: utf-8 -*-

# DROP TABLES

songplay_table_drop = 'drop table if exists songplays'
user_table_drop = 'drop table if exists users'
song_table_drop = 'drop table if exists songs'
artist_table_drop = 'drop table if exists artists'
time_table_drop = 'drop table if exists time'

# CREATE TABLES

user_table_create = \
    """create table if not exists users (user_id int primary key, first_name varchar, last_name varchar, gender varchar, level varchar)
"""

artist_table_create = \
    """create table if not exists artists(artist_id varchar primary key,
    name varchar not null,
    location varchar,
    lattitude float,
    longitude float
) 
"""

time_table_create = \
    """create table if not exists time(start_time timestamp primary key,
    hour int,
    day int,
    week int,
    month int,
    year int,
    weekday int
    )
"""

songplay_table_create = \
    """ create table if not exists songplays (songplay_id serial primary key, start_time timestamp not null, user_id int not null, level varchar, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent text)
"""

song_table_create = \
    """create table if not exists songs (song_id varchar primary key, title varchar not null, artist_id varchar not null,year int not null, duration float not null)
"""

# INSERT RECORDS

songplay_table_insert = \
    """INSERT INTO songplays(
    start_time,
    user_id,
    level,
    song_id,
    artist_id,
    session_id,
    location,
    user_agent)
VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
"""

user_table_insert = \
    """INSERT INTO users(user_id, first_name, last_name, gender, level)
VALUES(%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO UPDATE set level = EXCLUDED.level
"""

song_table_insert = \
    """INSERT INTO songs(song_id, title, artist_id, year, duration)
VALUES(%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO NOTHING
"""

artist_table_insert = \
    """INSERT INTO artists(artist_id, name, location, lattitude, longitude)
VALUES(%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO NOTHING
"""

time_table_insert = \
    """INSERT INTO time(start_time, hour, day, week, month, year, weekday)
VALUES(%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) DO NOTHING
"""

# FIND SONGS

song_select = \
    """ select s.song_id, a.artist_id from songs s join artists a on a.artist_id=s.artist_id where s.title = %s and a.name = %s and s.duration = %s  
"""

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create,
                        song_table_create, artist_table_create,
                        time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop,
                      song_table_drop, artist_table_drop,
                      time_table_drop]
