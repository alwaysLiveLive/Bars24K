import random

randsongs = []

randsongs.append("SOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIASOPHIA")

randsongs.append("KYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIEKYLIE")

def getSong(num):
  return randsongs[num]

def getRandSong():
  return random.choice(randsongs)

def songCrazyMashup(song, num):
  origLength = len(song)
  for i in range(num):
    randStart1 = random.randrange(0, int(len(song)/3))
    randEnd1 = random.randrange(randStart1, int(len(song)/3))
    randStart2 = random.randrange(int(len(song)/3), int(len(song)*2/3))
    randEnd2 = random.randrange(randStart2, int(len(song)*2/3))
    randStart3 = random.randrange(int(len(song)*2/3), len(song))
    randEnd3 = random.randrange(randStart3, len(song))
    song = song[:randStart1] + song[randEnd1:] + song[randStart1:randEnd1]
    song = song[randStart2:randEnd2] + song[:randStart2] + song[randEnd2:]
    lastRand = random.randrange(0, len(song))
    song = song[:lastRand] + song[randStart3:randEnd3] + song[lastRand:]
  return song[:origLength]
