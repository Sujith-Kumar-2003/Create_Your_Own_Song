import time
from midiutil import MIDIFile

# Helper functions
def add_notes_to_midi(notes, durations, midi_file, track, channel, start_time, volume):
    for note, duration in zip(notes, durations):
        midi_file.addNote(track, channel, note_to_midi(note), start_time, duration, volume)
        start_time += duration
    return start_time

def note_to_midi(note):
    """Convert note name to MIDI number."""
    note_map = {'c': 0, 'd': 2, 'e': 4, 'f': 5, 'g': 7, 'a': 9, 'bb': 10, 'b': 11}
    base_octave = 4
    name, octave = note[:-1], int(note[-1])
    return 12 * (octave + 1) + note_map[name.lower()]

# Functions for song sections
def play_intro(midi_file, track, channel, start_time, volume):
    notes = ['c4', 'c4', 'c4', 'f4', 'f4', 'f4', 'e4', 'f4', 'g4', 'a4', 'bb4', 'g4', 'a4']
    durations = [0.5, 0.5, 1, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1]
    return add_notes_to_midi(notes, durations, midi_file, track, channel, start_time, volume)

def play_partridge(midi_file, track, channel, start_time, volume):
    notes = ['c5', 'd5', 'bb4', 'a4', 'f4', 'g4', 'f4']
    durations = [1, 0.5, 0.5, 0.5, 0.5, 1, 1]
    return add_notes_to_midi(notes, durations, midi_file, track, channel, start_time, volume)

def play_verse(midi_file, track, channel, start_time, volume):
    notes = ['c5', 'g4', 'a4', 'bb4', 'g4']
    durations = [1, 0.5, 0.5, 0.5, 0.5]
    return add_notes_to_midi(notes, durations, midi_file, track, channel, start_time, volume)

def play_and_a(midi_file, track, channel, start_time, volume):
    notes = ['a4', 'bb4']
    durations = [0.5, 0.5]
    return add_notes_to_midi(notes, durations, midi_file, track, channel, start_time, volume)

def play_five_gold_rings(midi_file, track, channel, start_time, volume):
    notes = ['c5', 'd5', 'b4', 'c5']
    durations = [2, 0.5, 1.5, 2]
    return add_notes_to_midi(notes, durations, midi_file, track, channel, start_time, volume)

def play_four_three_two(midi_file, track, channel, start_time, volume):
    notes = ['c5', 'bb4', 'a4', 'g4', 'f4', 'bb4', 'd4', 'd4', 'f4', 'g4', 'f4', 'e4', 'd4', 'c4']
    durations = [0.5, 0.5, 0.5, 0.5, 1, 1, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 1]
    return add_notes_to_midi(notes, durations, midi_file, track, channel, start_time, volume)

# Main logic
def main():
    bpm = 120
    volume = 100  # MIDI volume (0-127)
    midi_file = MIDIFile(1)
    track = 0
    channel = 0
    start_time = 0  # Time in beats

    midi_file.addTrackName(track, start_time, "12 Days of Christmas")
    midi_file.addTempo(track, start_time, bpm)

    days = 1
    for _ in range(12):
        start_time = play_intro(midi_file, track, channel, start_time, volume)

        if days >= 5:
            for _ in range(days - 5):
                start_time = play_verse(midi_file, track, channel, start_time, volume)
            start_time = play_five_gold_rings(midi_file, track, channel, start_time, volume)
            start_time = play_four_three_two(midi_file, track, channel, start_time, volume)
            start_time = play_and_a(midi_file, track, channel, start_time, volume)
        elif days > 1:
            for _ in range(days - 1):
                start_time = play_verse(midi_file, track, channel, start_time, volume)
            start_time = play_and_a(midi_file, track, channel, start_time, volume)

        start_time = play_partridge(midi_file, track, channel, start_time, volume)
        days += 1

    # Save MIDI file
    with open("12_days_of_christmas.mid", "wb") as output_file:
        midi_file.writeFile(output_file)

    # Print statement indicating completion
    print("MIDI file for '12 Days of Christmas' has been successfully created and saved as '12_days_of_christmas.mid'.")

# Run the program
if __name__ == "__main__":
    main()
