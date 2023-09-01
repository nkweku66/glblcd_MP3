import random
from queue import Queue

class MP3Playlist:
    def __init__(self):
        self.playlist_queue = Queue()
        self.track_durations = {}
    
    def load_playlist(self, filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    track_info = line.strip().split('-')
                    track_name = track_info[0]
                    track_duration = int(track_info[-1])
                    self.playlist_queue.put(track_name)
                    self.track_durations[track_name] = track_duration
            print("Playlist loaded successfully.")
        except FileNotFoundError:
            print("File not found.")
    
    def display_playlist(self):
        if self.playlist_queue.empty():
            print("Playlist is empty.")
        else:
            print("Current playlist:")
            for idx, track in enumerate(self.playlist_queue.queue, start=1):
                print(f"{idx}. {track}")
    
    def enqueue_track(self, track):
        self.playlist_queue.put(track)
        print(f"'{track}' added to the playlist.")
    
    def remove_track(self, track):
        removed = False
        temp_queue = Queue()
        
        while not self.playlist_queue.empty():
            current_track = self.playlist_queue.get()
            if track.lower() != current_track.lower():
                temp_queue.put(current_track)
            else:
                removed = True
        
        self.playlist_queue = temp_queue
        
        if removed:
            print(f"Track '{track}' removed from the playlist.")
        else:
            print(f"Track '{track}' not found in the playlist.")
    
    def save_playlist(self, filename):
        try:
            with open(filename, 'w') as file:
                file.write('\n'.join(self.playlist_queue.queue))
            print("Playlist saved successfully.")
        except Exception as e:
            print("Error saving playlist:", e)
    
    def shuffle_playlist(self):
        playlist_list = list(self.playlist_queue.queue)
        random.shuffle(playlist)
        self.playlist_queue.queue = playlist_list
        print("Playlist shuffled.")
    
    def count_tracks(self):
        return self.playlist_queue.qsize()

    def calculate_duration(self):
        total_duration = sum(self.track_durations.get(track, 0) for track in self.playlist_queue.queue)
        hours = total_duration // 3600
        minutes = (total_duration % 3600) // 60
        seconds = total_duration % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    
    def clear_playlist(self):
        self.playlist_queue.queue.clear()
        print("Playlist cleared.")
    
    def is_empty(self):
        return self.playlist_queue.empty()

# Create an instance of MP3Playlist
playlist = MP3Playlist()

# Load playlist from a file
playlist.load_playlist('playlist.txt')

# Display the playlist
playlist.display_playlist()

total_duration = playlist.calculate_duration()
print(f"Total playlist duration: {total_duration}")

# Enqueue a track
track_to_enqueue = "Bad Liar - Imagine Dragons"
playlist.enqueue_track(track_to_enqueue)

# Remove a track
track_to_remove = "Song 0 - God is king"
playlist.remove_track(track_to_remove)

# Shuffle the playlist
playlist.shuffle_playlist()

# Display the updated playlist
playlist.display_playlist()

# Save the playlist
playlist.save_playlist('new_playlist.txt')

# Clear the playlist
playlist.clear_playlist()

# Check if the playlist is empty
print("Is playlist empty?", playlist.is_empty())