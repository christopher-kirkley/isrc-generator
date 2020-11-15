import pytest
import json

from isrc import make_settings_file, Isrcs, retrieve_settings

def test_can_make_setting_file():
    filename = make_settings_file()
    assert filename == 'settings.json'
    with open(filename, 'r') as f:
        assert json.loads(f.read()) == {
                'country_code': '',
                'isrc_registrant': '',
                'year': '',
                'catalog_number': '',
                }

def test_can_make_isrcs():
    test_isrcs = Isrcs('QZ', '123', '20', '012', 10)
    assert test_isrcs.country_code == 'QZ'
    isrcs = test_isrcs.make_isrcs()
    assert len(isrcs) == 10
    for i in range(10):
        assert isrcs[i] == f'QZ12320012{i+1:02d}'
        
def test_can_retrieve_settings():
    settings_json = retrieve_settings()
    assert len(settings_json) > 0
    assert settings_json['country_code'] == ''
    assert settings_json['isrc_registrant'] == ''
    assert settings_json['year'] == ''
    assert settings_json['catalog_number'] == ''


