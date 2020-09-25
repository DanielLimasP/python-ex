#Python the hard way: excercise 40

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_song(self):
        for line in self.lyrics:
            print(line)
    
happy_bday = Song(["""
    Happy birthday to you...
    Happy birthday to you..
    I don't want to get sued...
"""])

bulls = Song(["""
    They rally around the family!
    With the pockets full of shells
"""])

happy_bday.sing_me_song()
bulls.sing_me_song()