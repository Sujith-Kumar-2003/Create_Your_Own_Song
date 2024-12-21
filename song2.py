from midiutil import MIDIFile

# Helper functions
def add_notes_to_midi(notes, durations, midi_file, track, channel, start_time, volume):
    for note, duration in zip(notes, durations):
        midi_file.addNote(track, channel, note_to_midi(note), start_time, duration, volume)
        start_time += duration
    return start_time


def note_to_midi(note):
    """Convert note name to MIDI number."""
    note_map = {'c': 0, 'c#': 1, 'd': 2, 'd#': 3, 'e': 4, 'f': 5, 'f#': 6, 'g': 7, 'g#': 8, 'a': 9, 'a#': 10, 'b': 11}
    base_octave = 4
    name, octave = note[:-1], int(note[-1])
    return 12 * (octave + 1) + note_map[name.lower()]


# Functions for song sections
def play_jingle_bells_chorus(midi_file, track, channel, start_time, volume):
    notes = [
        'e5', 'e5', 'e5', 'e5', 'e5', 'e5', 'e5', 'g5', 'c5', 'd5', 'e5',
        'f5', 'f5', 'f5', 'f5', 'f5', 'e5', 'e5', 'e5', 'e5', 'e5', 'd5', 'd5', 'e5', 'd5', 'g5'
    ]
    durations = [
        0.5, 0.5, 1, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 1,
        0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 2
    ]
    return add_notes_to_midi(notes, durations, midi_file, track, channel, start_time, volume)


def play_jingle_bells_verse(midi_file, track, channel, start_time, volume):
    notes = [
        'g5', 'e5', 'd5', 'c5', 'a4', 'a4', 'a4', 'a4', 'b4', 'c5', 'd5', 'e5', 'f5', 'e5', 'd5', 'c5', 'd5'
    ]
    durations = [
        0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 2
    ]
    return add_notes_to_midi(notes, durations, midi_file, track, channel, start_time, volume)


# Main logic
def main():
    bpm = 90  # Further reduced BPM to extend song duration
    volume = 100  # MIDI volume (0-127)
    midi_file = MIDIFile(1)  # Create a MIDIFile object with one track
    track = 0
    channel = 0
    start_time = 0  # Time in beats

    midi_file.addTrackName(track, start_time, "Jingle Bells")
    midi_file.addTempo(track, start_time, bpm)


    # Structure of "Jingle Bells" (chorus and verse)
    section_duration = 32  # Approximate duration of one section in beats
    total_duration = 0
    section_repeats = 8  # Increased repetition to lengthen song

    while total_duration < bpm * 4:  # Loop to ensure the song is longer than 2.5 minutes (around 4 minutes)
        for _ in range(section_repeats):
            if total_duration % (2 * section_duration) == 0:
                start_time = play_jingle_bells_chorus(midi_file, track, channel, start_time, volume)
            else:
                start_time = play_jingle_bells_verse(midi_file, track, channel, start_time, volume)
            total_duration += section_duration

    # Save MIDI file
    with open("jingle_bells_extended_proper.mid", "wb") as output_file:
        midi_file.writeFile(output_file)

    print("MIDI file 'jingle_bells_extended_proper.mid' has been saved.")


# Run the program
if __name__ == "__main__":
    main()
