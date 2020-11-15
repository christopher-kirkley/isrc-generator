import os
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

def retrieve_settings():
    if os.path.exists('settings.json') == False:
        file = make_settings_file()
    with open('settings.json', 'r') as f:
        data = json.load(f)
    return data


def main():

    json = retrieve_settings()

    while True:
        country_code = input(f'Two character country code: [{json["country_code"]}] ')
        if len(country_code) != 2:
            continue
        else:
            break

    while True:
        isrc_registrant = input(f'Registrant of ISRC issuer: [{json["isrc_registrant"]}] ')
        if len(isrc_registrant) != 3:
            continue
        else:
            break

    while True:
        year = input(f'Two digit year: [{json["year"]}] ')
        if len(year) != 2:
            continue
        else:
            break

    while True:
        catalog_number = input(f'Three digit catalog number: [{json["catalog_number"]}] ')
        if len(catalog_number) != 3:
            continue
        else:
            break

    while True:
        tracks = input('Number of tracks: ')
        try:
            tracks = int(tracks)
            break
        except:
            continue

    isrcs = Isrcs(country_code, isrc_registrant, year, catalog_number, tracks)
    generated_isrcs = isrcs.make_isrcs()
    print(generated_isrcs)

if __name__ == '__main__':
    main()
