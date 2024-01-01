from mido import MidiFile
import mido
import time

mid = MidiFile('overworld.mid')
notes = 0
tracks = len(mid.tracks)
ppq = mid.ticks_per_beat
min_bpm = 999
max_bpm = 0

for msg in mid:
    if msg.type == 'note_on':
        notes += 1
    if msg.type == 'set_tempo':
        bpm = mido.tempo2bpm(msg.tempo)
        if bpm < min_bpm:
            min_bpm = bpm
        if bpm > max_bpm:
            max_bpm = bpm

print("Number of notes:", notes)
print("Number of tracks:", tracks)
print("PPQ (resolution):", ppq)
print("Minimum BPM:", min_bpm)
print("Maximum BPM:", max_bpm)