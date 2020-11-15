"""Generate ISRC from the command line."""

"""default values"""
CC = 'QZ'
XXX = ''
YY = 20
NNN = ''

i = input(f'Two character country code: [{CC}]')
if i != '':
    CC = i
i = input('Registrant of ISRC issuer: []')
if i != '':
    XXX = i
i = input(f'Catalog Number: [{NNN}]')
if i != '':
    NNN = i
tracks = int(input('Number of tracks:'))

isrcs = []

for track in range(tracks):
    isrc = f'{CC}{XXX}{NNN}{track:02d}'
    isrcs.append(isrc)

for isrc in isrcs:
    print(isrc)

