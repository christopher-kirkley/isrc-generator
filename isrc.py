import json

"""Generate ISRC from the command line."""

def make_settings_file():
    data = {
            'country_code': '',
            'isrc_registrant': '',
            'year': '',
            'catalog_number': '',
            }
    with open('settings.json', 'w') as f:
        json.dump(data, f)
    return f.name

class Isrcs:
    def __init__(self, country_code, isrc_registrant, year, catalog_number, tracks):
        self.country_code = country_code
        self.isrc_registrant = isrc_registrant
        self.year = year
        self.catalog_number = catalog_number
        self.tracks = tracks
        
    def make_isrcs(self):
        isrcs = []

        for self.track in range(self.tracks):
            isrc = f'{self.country_code}{self.isrc_registrant}{self.year}{self.catalog_number}{self.track+1:02d}'
            isrcs.append(isrc)
        return isrcs


def main():

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

if __name__ == '__main__':
    main()
