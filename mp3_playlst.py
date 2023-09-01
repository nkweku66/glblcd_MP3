from queue import Queue

class MP3Playlist:
    def __init__(self):
        # Initialize the playlist queue
        self.playlist_queue = Queue()
    
    
    def load_playlist(self, filename):
        # Load a playlist from a text file and enqueue the tracks
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    self.playlist_queue.put(line.strip())
            print("Playlist loaded successfully.")
        except FileNotFoundError:
            print("File not found.")
    
    def display_playlist(self):
        if self.playlist_queue.empty():
            print("Playist is empty.")
        else:
            print("Current playlist:")
            for track in self.playlist_queue.queue:
                print(track)
    
    def enqueue_track(self, track):
        # Enqueue an MP3 track to the playlist
        pass
    
    def remove_track(self, track):
        # Remove an MP3 from the playlist
        pass
    
    def save_playlist(self, filename):
        # Save the playlist to a text file
        pass
    
    def shuffle_playlist(self):
        # Shuffle all the songs in the playlist
        pass
    
    def count_tracks(self):
        # Count the number of tracks in the playlist
        pass
    
    def calculate_duration(self):
        # Calculate the total duration of the playlist
        pass
    
    def clear_playlist(self):
        # Clear/Reset the playlist
        pass
    
    def is_empty(self):
        # Check if the playlist is empty
        pass

# Create an instance of MP3Playlist
playlist = MP3Playlist()

# Load playlist
playlist.load_playlist('playlist.txt')

#Display the playlist
playlist.display_playlist()
