'''
Jukebox

Piero Orderique

Design a musical jukebox using ood principles
Users: General Public (Say, Country's BBQ in Downtown Columbus)

What they can see:
    DONE: Song that is playing and at what volume
    DONE: (List of available songs) - for now any is available!
    DONE: Queue of songs that going to play next

What they can do:
    DONE: turn up the volume
    request a song (add to song queue)

'''
from datastructures import Dequeue
from time import sleep

class Jukebox:
    def __init__(self, *songs):
        self.volume = 0
        self.currently_playing = None
        self.song_queue = Dequeue()
        self.timeout = 2
        self.options = {
            "1":"See screen",
            "2":"Request a song",
            "3":"Play next song",
            "4":"See song queue",
            "5":"Set volume",
            "6":"TURN OFF",
        }
        # add the songs to queue if any
        for song in songs:
            self.song_queue.add(song)
        if not self.song_queue.is_empty():
            self.currently_playing = self.song_queue.pop_first()

    def request_song(self, song):
        if not self.currently_playing:
            self.currently_playing = song
        else:
            self.song_queue.add(song)

    def set_volume(self, volume):
        self.volume = volume

    def peek_volume(self):
        return "Vol: " + str(self.volume)

    def peek_song(self):
        if self.currently_playing:
            return str(self.currently_playing)
        else:
            return "REQUEST A SONG"

    def peek_screen(self):
        screen = "\n|" + self.peek_song() + "| " + self.peek_volume() + " |\n"
        SCREEN_WIDTH = (len(screen)-2)
        rep = "-"*SCREEN_WIDTH + screen + "-"*SCREEN_WIDTH
        rep += "\n" + self.peek_queue()
        return rep

    def peek_queue(self):
        return "UP NEXT: " + str(self.song_queue)

    def play_next(self):
        if self.song_queue.is_empty(): self.currently_playing = None
        else: self.currently_playing = self.song_queue.pop_first()

    def _show_options(self):
        print("\nJUKEBOX OPTIONS:")
        for num, option in self.options.items(): print(num+": "+option)

    def get_command(self):
        self._show_options()
        return input("\nPlease Enter a Number: ")

    def show_action(self, choice):
        if choice not in self.options:
            print("-"*25, "\nOPTION INVALID")
            print("-"*25)
        else:
            if choice == "1":
                print(self.peek_screen())
            elif choice == "2":
                title = input("Enter Song Title: ")
                artist = input("Enter Song Artist: ")
                self.request_song(Song(title, artist))
                print("\n" + self.peek_screen())
            elif choice == "3":
                self.play_next()
                print("\n" + self.peek_screen())
            elif choice == "4":
                print("\n" + self.peek_queue())
            elif choice == "5":
                vol = None
                while vol is None:
                    vol = input("Set volume (1-100): ")
                    try:
                        vol = int(vol)
                        if vol < 0 or vol > 100:
                            print("INVALID INPUT")
                            continue
                        else:
                            self.set_volume(vol)
                    except:
                        print("INVALID INPUT")
            elif choice == "6":
                pass

    def __str__(self):
        return self.peek_screen()

class Song:
    def __init__(self, title, artist, **info):
        self.title = title
        self.artist = artist
        self.info = {"title":self.title, "artist":self.artist}
        for key, value in info.items():
            self.info[key] = value

    def get_info(self):
        print(self.info)

    def __str__(self):
        return self.title + " by " + self.artist

def start_jukebox():
    juke = Jukebox(
        Song("Ophelia", "The Lumineers"),
        Song("Coffee", "QuinXCII"),
        Song("Hello", "Adele"),
    )
    print("\nBOOTING UP JUKEBOX...")
    sleep(juke.timeout)
    # juke._show_options()
    choice = juke.get_command()
    while choice != "6":
        juke.show_action(choice)
        sleep(juke.timeout)
        choice = juke.get_command()
    # if out of loop, juke box was turned off
    print("\nJUKE BOX TURNED OFF")

if __name__ == "__main__":
    start_jukebox()
