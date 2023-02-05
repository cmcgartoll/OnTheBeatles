# Generated by Django 4.1.2 on 2023-02-01 06:47

from django.db import migrations

def add_beatles_albums(apps, schema_editor):
    # if schema_editor.connection.alias != 'default':
    #     return
    Artist = apps.get_model('spotify', 'Artist')
    Album = apps.get_model('spotify', 'Album')
    Song = apps.get_model('spotify', 'Song')
    # beatles = Artist.objects.filter(spotify_id='3WrFJ7ztbogyGnTHbHJFl2').first()
    beatles = Artist.objects.create(spotify_id='3WrFJ7ztbogyGnTHbHJFl2', name='The Beatles')
    Album.objects.create(spotify_id='3KzAvEXcqJKBF97HrXwlgf', title='Please Please Me', release_date='1963-03-22', cover='https://i.scdn.co/image/ab67616d0000b273dbeec63ad914c973e75c24df').artist.add(beatles)
    album = Album.objects.filter(spotify_id='3KzAvEXcqJKBF97HrXwlgf').first()
    Song.objects.create(spotify_id='3KiexfmhxHvG5IgAElmTkd', name='I Saw Her Standing There', track_number=1, duration_ms=173946, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='40qXGg5nRbcWzcFb26KWkQ', name='Misery', track_number=2, duration_ms=108546, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='2baEFuU0gQon0hgVRioI1o', name='Anna (Go To Him)', track_number=3, duration_ms=177133, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='3JQWLa88R35d971o5bIImd', name='Chains', track_number=4, duration_ms=145080, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='7JxGM1R32ZqfwZou3VtnTg', name='Boys', track_number=5, duration_ms=146440, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='7529Z6b1rlGZFFPWjHPeV5', name='Ask Me Why', track_number=6, duration_ms=146533, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='6EHuOufBeL6vk3TvVJB5qo', name='Please Please Me', track_number=7, duration_ms=120853, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='3VbGCXWRiouAq8VyMYN2MI', name='Love Me Do', track_number=8, duration_ms=141693, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='7Msq9qojB7yORuJvz49iUy', name='P.S. I Love You', track_number=9, duration_ms=124360, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='2VmB1rF9FtfKUmFHDVnq8Q', name='Baby It\'s You', track_number=10, duration_ms=160520, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='7Aobt67JnaF7qN8jCCKvHq', name='Do You Want To Know A Secret', track_number=11, duration_ms=117013, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='7fh53ta3vAOGJMQ4i5tCHe', name='A Taste Of Honey', track_number=12, duration_ms=123480, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='4dessGxnKXmTbHPhVgqODq', name='There\'s A Place', track_number=13, duration_ms=110493, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='5ZBeML7Lf3FMEVviTyvi8l', name='Twist And Shout', track_number=14, duration_ms=155226, album=album).artist.add(beatles)
    Album.objects.create(spotify_id='1aYdiJk6XKeHWGO3FzHHTr', title='With The Beatles', release_date='1963-11-22', cover='https://i.scdn.co/image/ab67616d0000b273608a63ad5b18e99da94a3f73').artist.add(beatles)
    album = Album.objects.filter(spotify_id='1aYdiJk6XKeHWGO3FzHHTr').first()
    Song.objects.create(spotify_id='4ekUX4pWizXXksJe0JfS9U', name='It Won\'t Be Long', track_number=1, duration_ms=133386, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='5tztLBvTlNC15Np2tnQ5Ll', name='All I\'ve Got To Do', track_number=2, duration_ms=122573, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='4joiWvli4qJVEW6qZV2i2J', name='All My Loving', track_number=3, duration_ms=127853, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='7y1hMqXNa0dKQLZH7CKbUG', name='Don\'t Bother Me', track_number=4, duration_ms=148253, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='0KogQrSowDnZoU8GSpaxkj', name='Little Child', track_number=5, duration_ms=106400, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='0ESIjVxnDnCDaTPo6sStHm', name='Till There Was You', track_number=6, duration_ms=133506, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='6wfK1R6FoLpmUA9lk5ll4T', name='Please Mister Postman', track_number=7, duration_ms=154160, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='3idqWaBn3mRdsIodCU6uBi', name='Roll Over Beethoven', track_number=8, duration_ms=165466, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='2RvKsA6Ho7VbJkVFiD4UQF', name='Hold Me Tight', track_number=9, duration_ms=151906, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='7rgUYidQh5tH0YlXCoKaYJ', name='You Really Got A Hold On Me', track_number=10, duration_ms=181346, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='0sIZcoe69iSym9AecvZ7CT', name='I Wanna Be Your Man', track_number=11, duration_ms=119506, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='5maTh4fY9SlgR3FhRkf040', name='Devil In Her Heart', track_number=12, duration_ms=146213, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='5vl0sRtrQM1BTSAxQZFqEN', name='Not A Second Time', track_number=13, duration_ms=126826, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='3zw4FTrVNfy2teEkV9FOvh', name='Money (That\'s What I Want)', track_number=14, duration_ms=169506, album=album).artist.add(beatles)
    Album.objects.create(spotify_id='6wCttLq0ADzkPgtRnUihLV', title='A Hard Day\'s Night', release_date='1964-07-10', cover='https://i.scdn.co/image/ab67616d0000b273e230f303815e82a86713eedd').artist.add(beatles)
    album = Album.objects.filter(spotify_id='6wCttLq0ADzkPgtRnUihLV').first()
    Song.objects.create(spotify_id='5J2CHimS7dWYMImCHkEFaJ', name='A Hard Day\'s Night', track_number=1, duration_ms=154200, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='3pU1CUgPiFfxPCpscwIwQR', name='I Should Have Known Better', track_number=2, duration_ms=163080, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='1hgvykolO4kBIEozATmpyj', name='If I Fell', track_number=3, duration_ms=139466, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='0gd50I2gKioJ59C827EdAY', name='I\'m Happy Just To Dance With You', track_number=4, duration_ms=116373, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='65vdMBskhx3akkG9vQlSH1', name='And I Love Her', track_number=5, duration_ms=149693, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='0Wzp5pWPoX0YoBg002HXL9', name='Tell Me Why', track_number=6, duration_ms=128693, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='3SdingSsFcZDZAyvcJbgAw', name='Can\'t Buy Me Love', track_number=7, duration_ms=131866, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='70XHAdaMaoLIOVb1hSaeJ4', name='Any Time At All', track_number=8, duration_ms=131280, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='01xMiErR26kH1KCif6uEYI', name='I\'ll Cry Instead', track_number=9, duration_ms=105986, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='0voUr8lubIafUVJlauJxYF', name='Things We Said Today', track_number=10, duration_ms=155333, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='4oLQ0imA5IDtNUnhFKY87q', name='When I Get Home', track_number=11, duration_ms=136640, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='5b9G4dtK3Tdguuy9BO3Nwo', name='You Can\'t Do That', track_number=12, duration_ms=154893, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='3lSi6qfnp2YZazTzcOLBZk', name='I\'ll Be Back', track_number=13, duration_ms=144186, album=album).artist.add(beatles)
    Album.objects.create(spotify_id='1vANZV20H5B4Fk6yf7Ot9a', title='Beatles For Sale', release_date='1964-12-04', cover='https://i.scdn.co/image/ab67616d0000b27355612ece447bec5d62c68375').artist.add(beatles)
    album = Album.objects.filter(spotify_id='1vANZV20H5B4Fk6yf7Ot9a').first()
    Song.objects.create(spotify_id='4ltC6PrqkTtpcRNi5lvS4z', name='No Reply', track_number=1, duration_ms=136066, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='7wC4EW11mBVxDK3xdC7FTf', name='I\'m A Loser', track_number=2, duration_ms=150026, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='7cb2SdLm1UMLwdUoWwrZN1', name='Baby\'s In Black', track_number=3, duration_ms=124520, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='7Ho3T7ERfooiAfvODaMQ2N', name='Rock And Roll Music', track_number=4, duration_ms=151280, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='45WX2cfbL8bCIqv3rOq1G3', name='I\'ll Follow The Sun', track_number=5, duration_ms=108853, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='6pPOkr2OxhQ6htrzOiDmq9', name='Mr Moonlight', track_number=6, duration_ms=158626, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='5xf0zdP4KCfshyVn02D3Ea', name='Kansas City / Hey-Hey-Hey-Hey', track_number=7, duration_ms=158146, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='1Dg4dFJr3HW7sbA7vPejre', name='Eight Days A Week', track_number=8, duration_ms=163600, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='42qkSeX6HNJYHxlk6cWoFe', name='Words Of Love', track_number=9, duration_ms=124320, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='2d7GP7Fz1NrfPpo7MzWZgb', name='Honey Don\'t', track_number=10, duration_ms=177426, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='2CxTkdvhDuQrOxl8xXkdJS', name='Every Little Thing', track_number=11, duration_ms=123800, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='3kQDIa85ZK8cKVn72NfBnl', name='I Don\'t Want To Spoil The Party', track_number=12, duration_ms=154466, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='6C6y4OWK1Ki3FVF1TIonxW', name='What You\'re Doing', track_number=13, duration_ms=150040, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='4DZAH8eiqSAkMIE9l5D71U', name='Everybody\'s Trying To Be My Baby', track_number=14, duration_ms=146000, album=album).artist.add(beatles)
    Album.objects.create(spotify_id='0PT5m6hwPRrpBwIHVnvbFX', title='Help!', release_date='1965-08-06', cover='https://i.scdn.co/image/ab67616d0000b273e3e3b64cea45265469d4cafa').artist.add(beatles)
    album = Album.objects.filter(spotify_id='0PT5m6hwPRrpBwIHVnvbFX').first()
    Song.objects.create(spotify_id='7DD7eSuYSC5xk2ArU62esN', name='Help!', track_number=1, duration_ms=139560, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='5xcfepnz1v7a83T8An9gjw', name='The Night Before', track_number=2, duration_ms=154933, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='4F1AgKpuFRMLEgtPETVwZk', name='You\'ve Got To Hide Your Love Away', track_number=3, duration_ms=129120, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='5EzvwjFwdP5Kfl5AZAemzu', name='I Need You', track_number=4, duration_ms=148786, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='7hefVXaGsFPesbK6fKwS6F', name='Another Girl', track_number=5, duration_ms=125360, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='70HNt0eoBVqr4ss68U8x3B', name='You\'re Going To Lose That Girl', track_number=6, duration_ms=138666, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='7CZiDzGVjUssMSOXrDNYHL', name='Ticket To Ride', track_number=7, duration_ms=189680, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='0IxxqsYBcCHEQ1HqLYJnwx', name='Act Naturally', track_number=8, duration_ms=150373, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='2ue1KRstSKHF8jQkIJZiNC', name='It\'s Only Love', track_number=9, duration_ms=116480, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='0y1LLH0NiwOD5tM3aNMXTr', name='You Like Me Too Much', track_number=10, duration_ms=156866, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='2jnr9KaaMAmvk0zMcM9UzV', name='Tell Me What You See', track_number=11, duration_ms=157986, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='788U1Sqej9M6c4iikuDGxO', name='I\'ve Just Seen A Face', track_number=12, duration_ms=125040, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='3BQHpFgAp4l80e1XslIjNI', name='Yesterday', track_number=13, duration_ms=125666, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='70Dohn82wv6VtxGesqRzbZ', name='Dizzy Miss Lizzy', track_number=14, duration_ms=176506, album=album).artist.add(beatles)
    Album.objects.create(spotify_id='50o7kf2wLwVmOTVYJOTplm', title='Rubber Soul', release_date='1965-12-03', cover='https://i.scdn.co/image/ab67616d0000b273ed801e58a9ababdea6ac7ce4').artist.add(beatles)
    album = Album.objects.filter(spotify_id='50o7kf2wLwVmOTVYJOTplm').first()
    Song.objects.create(spotify_id='06ypiqmILMdVeaiErMFA91', name='Drive My Car', track_number=1, duration_ms=148893, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='1H7gMYGykdtwZOV6s1N0by', name='Norwegian Wood (This Bird Has Flown)', track_number=2, duration_ms=124693, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='4LLBKnNCrSRrSjSTuiwjE9', name='You Won\'t See Me', track_number=3, duration_ms=199960, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='5SUlhldQJtOhUr2GzH5RI7', name='Nowhere Man', track_number=4, duration_ms=163693, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='64bKVrkaXQAKx04dLHqCNz', name='Think For Yourself', track_number=5, duration_ms=138520, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='4GBaPHvAyj4V2jeobD9tsy', name='The Word', track_number=6, duration_ms=163106, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='5By7Pzgl6TMuVJG168VWzS', name='Michelle', track_number=7, duration_ms=162373, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='19QXdPRZFHI5kNK3tN8Mh7', name='What Goes On', track_number=8, duration_ms=168573, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='6tQvjqDIK9GXWIC6mejms8', name='Girl', track_number=9, duration_ms=151720, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='5E3BVY66TEDexFutOO5GeS', name='I\'m Looking Through You', track_number=10, duration_ms=146386, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='3KfbEIOC7YIv90FIfNSZpo', name='In My Life', track_number=11, duration_ms=146333, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='0CGbof9amBnsNlRhZ8IY2H', name='Wait', track_number=12, duration_ms=134720, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='7C6hdDIz90Uf5YmdZnYbJJ', name='If I Needed Someone', track_number=13, duration_ms=142266, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='4gUYV3ktbaOeAK5KrXMWV5', name='Run For Your Life', track_number=14, duration_ms=141093, album=album).artist.add(beatles)
    Album.objects.create(spotify_id='3PRoXYsngSwjEQWR5PsHWR', title='Revolver', release_date='1966-08-05', cover='https://i.scdn.co/image/ab67616d0000b27328b8b9b46428896e6491e97a').artist.add(beatles)
    album = Album.objects.filter(spotify_id='3PRoXYsngSwjEQWR5PsHWR').first()
    Song.objects.create(spotify_id='4BRkPBUxOYffM2QXVlq7aC', name='Taxman', track_number=1, duration_ms=158853, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='5GjPQ0eI7AgmOnADn1EO6Q', name='Eleanor Rigby', track_number=2, duration_ms=126533, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='2ylCrFiBu98SC0vFfaCent', name='I\'m Only Sleeping', track_number=3, duration_ms=180320, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='4RdJFhfLQcezwN5LsXl4qP', name='Love You To', track_number=4, duration_ms=179826, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='2B4Y9u4ERAFiMo13XPJyGP', name='Here, There And Everywhere', track_number=5, duration_ms=144880, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='50xwQXPtfNZFKFeZ0XePWc', name='Yellow Submarine', track_number=6, duration_ms=158880, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='3VSuWxZM6x6V3ig5nYtikL', name='She Said She Said', track_number=7, duration_ms=156040, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='7HTH1ppjkkOe7RLoBDKXYJ', name='Good Day Sunshine', track_number=8, duration_ms=129293, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='4KRgqwb4kvBuTz1utbYxfb', name='And Your Bird Can Sing', track_number=9, duration_ms=120493, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='1kDkaFlmkdEZiVUogaP9OZ', name='For No One', track_number=10, duration_ms=119813, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='1ob06Ol8FMIPQgjpg7bMyk', name='Doctor Robert', track_number=11, duration_ms=134266, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='7orb0y6ySGdsYZywMoQtsD', name='I Want To Tell You', track_number=12, duration_ms=147973, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='3tGhRLgcCP6SIZU3tbGl7l', name='Got To Get You Into My Life', track_number=13, duration_ms=149240, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='00oZhqZIQfL9P5CjOP6JsO', name='Tomorrow Never Knows', track_number=14, duration_ms=179546, album=album).artist.add(beatles)
    Album.objects.create(spotify_id='6QaVfG1pHYl1z15ZxkvVDW', title='Sgt. Pepper\'s Lonely Hearts Club Band', release_date='1967-06-01', cover='https://i.scdn.co/image/ab67616d0000b27334ef8f7d06cf2fc2146f420a').artist.add(beatles)
    album = Album.objects.filter(spotify_id='6QaVfG1pHYl1z15ZxkvVDW').first()
    Song.objects.create(spotify_id='4fUKE8EULjQdHF4zb0M8FO', name='Sgt. Pepper\'s Lonely Hearts Club Band', track_number=1, duration_ms=122893, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='2RnPATK99oGOZygnD2GTO6', name='With A Little Help From My Friends', track_number=2, duration_ms=164106, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='25yQPHgC35WNnnOUqFhgVR', name='Lucy In The Sky With Diamonds', track_number=3, duration_ms=208466, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='3LtOmWpTXLhilL5odoKysR', name='Getting Better', track_number=4, duration_ms=168120, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='3pKKxkeB1pOUMHwWBmKc3Y', name='Fixing A Hole', track_number=5, duration_ms=156826, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='3PjMtNzwhDHqxoKudm6GvF', name='She\'s Leaving Home', track_number=6, duration_ms=215160, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='6W35n1UlkvqhfMZstB4BXs', name='Being For The Benefit Of Mr. Kite!', track_number=7, duration_ms=157533, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='3Umg8CDhO8dOSj7yBTInYb', name='Within You Without You', track_number=8, duration_ms=304666, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='1NrbnHlR2BFREcyWXHIHip', name='When I\'m Sixty Four', track_number=9, duration_ms=157666, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='6h9W5FxX4E9lUFsyq8j1AD', name='Lovely Rita', track_number=10, duration_ms=162093, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='0xIuNHHcKI1JDuBPlSwzb1', name='Good Morning Good Morning', track_number=11, duration_ms=161226, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='42ocGQCOT0xYtV3f5kJDsD', name='Sgt. Pepper\'s Lonely Hearts Club Band - Reprise / Remastered 2009', track_number=12, duration_ms=79066, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='0hKRSZhUGEhKU6aNSPBACZ', name='A Day In The Life', track_number=13, duration_ms=337413, album=album).artist.add(beatles)
    Album.objects.create(spotify_id='2BtE7qm1qzM80p9vLSiXkj', title='Magical Mystery Tour', release_date='1967-11-27', cover='https://i.scdn.co/image/ab67616d0000b273692d9189b2bd75525893f0c1').artist.add(beatles)
    album = Album.objects.filter(spotify_id='2BtE7qm1qzM80p9vLSiXkj').first()
    Song.objects.create(spotify_id='0qHMhBZqYb99yhX9BHcIkV', name='Magical Mystery Tour', track_number=1, duration_ms=170106, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='6rHh8urosEFRI67xVa6fzU', name='The Fool On The Hill', track_number=2, duration_ms=179106, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='1itLKsCWHtLnxALkgBk1Fa', name='Flying', track_number=3, duration_ms=135520, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='0QIX9BS0AUCQcHYvyrsMkV', name='Blue Jay Way', track_number=4, duration_ms=235066, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='1dxbAIfCASqv6jix2R1Taj', name='Your Mother Should Know', track_number=5, duration_ms=148413, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='6Pq9MmkDQYZiiCDpxnvrf6', name='I Am The Walrus', track_number=6, duration_ms=275866, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='0vZ97gHhemKm6c64hTfJNA', name='Hello, Goodbye', track_number=7, duration_ms=208840, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='3Am0IbOxmvlSXro7N5iSfZ', name='Strawberry Fields Forever', track_number=8, duration_ms=247320, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='1h04XMpzGzmAudoI6VHBgA', name='Penny Lane', track_number=9, duration_ms=180893, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='0JBvtprXP2Z0LP3jmzA7Xp', name='Baby, You\'re A Rich Man', track_number=10, duration_ms=181306, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='68BTFws92cRztMS1oQ7Ewj', name='All You Need Is Love', track_number=11, duration_ms=230386, album=album).artist.add(beatles)
    Album.objects.create(spotify_id='1klALx0u4AavZNEvC4LrTL', title='The Beatles', release_date='1968-11-22', cover='https://i.scdn.co/image/ab67616d0000b2734ce8b4e42588bf18182a1ad2').artist.add(beatles)
    album = Album.objects.filter(spotify_id='1klALx0u4AavZNEvC4LrTL').first()
    Song.objects.create(spotify_id='0j3p1p06deJ7f9xmJ9yG22', name='Back In The U.S.S.R.', track_number=1, duration_ms=163453, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='5NQYyej46WQkgCbnzGD21W', name='Dear Prudence', track_number=2, duration_ms=235773, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='2jAojvUaPoHPFSPpF0UNRo', name='Glass Onion', track_number=3, duration_ms=137840, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='1gFNm7cXfG1vSMcxPpSxec', name='Ob-La-Di, Ob-La-Da', track_number=4, duration_ms=188960, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='6j67aNAPeQ31uw4qw4rpLa', name='Wild Honey Pie', track_number=5, duration_ms=52973, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='5Z3Rd1fMcaty8g5Pn7yhBQ', name='The Continuing Story Of Bungalow Bill', track_number=6, duration_ms=194160, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='389QX9Q1eUOEZ19vtzzI9O', name='While My Guitar Gently Weeps', track_number=7, duration_ms=285000, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='71LsKf3xISiOlY1mj7FFPP', name='Happiness Is A Warm Gun', track_number=8, duration_ms=164546, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='1swmf4hFMJYRNA8Rq9PVaW', name='Martha My Dear', track_number=9, duration_ms=148573, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='2X9H5BokS1u5O46YpNYNsZ', name='I\'m So Tired', track_number=10, duration_ms=123493, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='5jgFfDIR6FR0gvlA56Nakr', name='Blackbird', track_number=11, duration_ms=138386, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='4ZmjfLdJXbqjAENqk7eWSE', name='Piggies', track_number=12, duration_ms=124266, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='1ITQbrueGLl581a25XXm9c', name='Rocky Raccoon', track_number=13, duration_ms=213106, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='4zq4rrfHZeZsTbo5vjJXSV', name='Don\'t Pass Me By', track_number=14, duration_ms=230453, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='4eLIq1nQNwz2qLu8DeiWIp', name='Why Don\'t We Do It In The Road?', track_number=15, duration_ms=101160, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='09x9v1o51dbqi5H0u7UGfp', name='I Will', track_number=16, duration_ms=105933, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='5FnpXVgDOk2sLT58qM22Of', name='Julia', track_number=17, duration_ms=176666, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='1ABegtCPBMMJaMpfDyATjE', name='Birthday', track_number=1, duration_ms=163080, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='2AsGApoUuN8pTM17Lq9eUd', name='Yer Blues', track_number=2, duration_ms=240453, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='6TjUg1cTUzWHbal6yQAi7c', name='Mother Nature\'s Son', track_number=3, duration_ms=168026, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='64P3zpRsDHIk7YTpRtaKYL', name='Everybody\'s Got Something To Hide Except Me And My Monkey', track_number=4, duration_ms=144773, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='2tBv9tAdqEbLNDi5smSjbg', name='Sexy Sadie', track_number=5, duration_ms=195266, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='0Bs0hUYxz7REyIHH7tRhL2', name='Helter Skelter', track_number=6, duration_ms=269786, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='40d2EcaOOCUjDzzo2YvUWn', name='Long, Long, Long', track_number=7, duration_ms=186306, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='1aOzDhi5a1RWWRy5dmYA8I', name='Revolution 1', track_number=8, duration_ms=255706, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='1TPcNcmuKlq0PKpYOBgP1U', name='Honey Pie', track_number=9, duration_ms=161160, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='5iyCSUM7zzficwaGo8GIoc', name='Savoy Truffle', track_number=10, duration_ms=174466, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='5XmetMMUFNXClbiYnGdVmP', name='Cry Baby Cry', track_number=11, duration_ms=182080, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='5dZ8PeKKZJLIQAWNTdp8WX', name='Revolution 9', track_number=12, duration_ms=502013, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='3T4Kt51PV4k8tx6YCtBgcl', name='Good Night', track_number=13, duration_ms=193760, album=album).artist.add(beatles)
    Album.objects.create(spotify_id='0ETFjACtuP2ADo6LFhL6HN', title='Abbey Road', release_date='1969-09-26', cover='https://i.scdn.co/image/ab67616d0000b273dc30583ba717007b00cceb25').artist.add(beatles)
    album = Album.objects.filter(spotify_id='0ETFjACtuP2ADo6LFhL6HN').first()
    Song.objects.create(spotify_id='2EqlS6tkEnglzr7tkKAAYD', name='Come Together', track_number=1, duration_ms=259946, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='0pNeVovbiZHkulpGeOx1Gj', name='Something', track_number=2, duration_ms=182293, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='2S8xyNRJX1XQdo3qnTuovI', name='Maxwell\'s Silver Hammer', track_number=3, duration_ms=207920, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='2mxByJWOajjiVsLWjNXvDJ', name='Oh! Darling', track_number=4, duration_ms=207240, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='0suLngfo7rJoetk7Ub6N8l', name='Octopus\'s Garden', track_number=5, duration_ms=170720, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='3Z25k4ZF6QENy2d9YatsM5', name='I Want You (She\'s So Heavy)', track_number=6, duration_ms=467320, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='6dGnYIeXmHdcikdzNNDMm2', name='Here Comes The Sun', track_number=7, duration_ms=185733, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='1rxoyGj1QuPoVi8fOft1Kt', name='Because', track_number=8, duration_ms=165666, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='1jOLTO379yIu9aMnCkpMQl', name='You Never Give Me Your Money', track_number=9, duration_ms=242973, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='4nwKdZID1ht0lDBJ5h2p87', name='Sun King', track_number=10, duration_ms=146266, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='4JOyMhad5dD81uGYLGgKrS', name='Mean Mr Mustard', track_number=11, duration_ms=66533, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='1FTCA6wQwulQFokDddKE68', name='Polythene Pam', track_number=12, duration_ms=72640, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='2jtUGFsqanQ82zqDlhiKIp', name='She Came In Through The Bathroom Window', track_number=13, duration_ms=118626, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='01SfTM5nfCou5gQL70r6gs', name='Golden Slumbers', track_number=14, duration_ms=91760, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='5eZrW59C3UgBhkqNlowEID', name='Carry That Weight', track_number=15, duration_ms=96466, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='5aHHf6jrqDRb1fcBmue2kn', name='The End', track_number=16, duration_ms=141613, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='6UCFZ9ZOFRxK8oak7MdPZu', name='Her Majesty', track_number=17, duration_ms=25986, album=album).artist.add(beatles)
    Album.objects.create(spotify_id='0jTGHV5xqHPvEcwL8f6YU5', title='Let It Be', release_date='1970-05-08', cover='https://i.scdn.co/image/ab67616d0000b27384243a01af3c77b56fe01ab1').artist.add(beatles)
    album = Album.objects.filter(spotify_id='0jTGHV5xqHPvEcwL8f6YU5').first()
    Song.objects.create(spotify_id='0CaBBQsaAiRHhiLmzi7ZRp', name='Two Of Us', track_number=1, duration_ms=216813, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='4OUmlC67FoPLvQNuE5C7kF', name='Dig A Pony', track_number=2, duration_ms=235000, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='4dkoqJrP0L8FXftrMZongF', name='Across The Universe', track_number=3, duration_ms=228133, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='2BMqay80iBzZTa608Y1eG1', name='I Me Mine', track_number=4, duration_ms=145586, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='0eRyOunOVBChlXxIvqwOxH', name='Dig It', track_number=5, duration_ms=50466, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='7iN1s7xHE4ifF5povM6A48', name='Let It Be', track_number=6, duration_ms=243026, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='2VsX1BoWSGiuVXGiFSUr6h', name='Maggie Mae', track_number=7, duration_ms=40040, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='3gwRWIbr5ycEVLIAXrWaw7', name='I\'ve Got A Feeling', track_number=8, duration_ms=217560, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='50qHmeex1nPTyQTwBXjSE4', name='One After 909', track_number=9, duration_ms=173960, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='3mlMpmY8oZIBFc39D9zLbh', name='The Long And Winding Road', track_number=10, duration_ms=218186, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='5dpRJkvY8oWMQmQbEQTXhO', name='For You Blue', track_number=11, duration_ms=152213, album=album).artist.add(beatles)
    Song.objects.create(spotify_id='4MLBqAEzNN89o2M9h92Z26', name='Get Back', track_number=12, duration_ms=189386, album=album).artist.add(beatles)

class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0006_remove_song_dislikes_remove_song_likes_songrating_and_more'),
    ]

    operations = [
        migrations.RunPython(add_beatles_albums),
    ]
