import unittest
import psn

def game_fixture():
    game = psn.PSNGame(
        '26. Osho Sen',
        'Gamagori City, Aichi Prefecture',
        '19760204',
        '3',
        'Oyama Yasuharu',
        'Nakahara Makoto',
        '1-0'
    )

    game.annotator = 'Thomas Majewski'
    game.plycount = '176'
    game.timecontrol = '205200' # 2 days 9 hours each
    game.mode = 'OTB'
    game.sfen = 'lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL'

    game.moves = ['P7g-7f', 'P8c-8d', 'R2h-7h', 'P3c-3d', 'P6g-6f', 'P8d-8e', 'B8h-7g', 'S7a-6b', 'S7i-6h', 'K5a-4b', 'K5i-4h', 'K4b-3b', 'K4h-3h', 'G6a-5b', 'K3h-2h', 'P1c-1d', 'P1g-1f', 'P5c-5d', 'S3i-3h', 'S3a-4b', 'G6i-5h', 'P7c-7d', 'P5g-5f', 'S4b-3c', 'S6h-5g', 'B2b-3a', 'R7h-8h', 'S6b-7c', 'B7g-5i', 'P4c-4d', 'P3g-3f', 'K3b-2b', 'P2g-2f', 'G4a-3b', 'S3h-2g', 'P2c-2d', 'G4i-3h', 'G5b-4c', 'B5i-3g', 'B3a-6d', 'P4g-4f', 'B6d-4b', 'G5h-4g', 'P9c-9d', 'P9g-9f', 'L9a-9c', 'S5g-4h', 'R8b-8d', 'P6f-6e', 'P7d-7e', 'P7fx7e', 'B4bx7e', 'S4h-5g', 'R8d-7d', 'P\'7f', 'B7e-4b', 'R8h-7h', 'R7d-8d', 'R7h-8h', 'P\'7h', 'S5g-6h', 'P6c-6d', 'B3g-4h', 'R8d-8b', 'P6ex6d', 'S7cx6d', 'N8i-7g', 'S6d-7c', 'R8h-8i', 'S7c-7d', 'N2i-3g', 'P7h-7i+', 'S6hx7i', 'R8b-6b', 'P\'6e', 'P\'7e', 'P7fx7e', 'S7dx7e', 'S7i-7h', 'P\'7f', 'N7gx8e', 'R6bx6e', 'R8i-6i', 'P\'6h', 'R6i-7i', 'P7f-7g+', 'S7hx7g', 'R6e-6g+', 'G4g-5g', '+R6g-6e', 'P\'6g', 'P6h-6i+', 'R7ix6i', '+R6e-7d', 'N8ex9c', 'N8ax9c', 'R6i-7i', 'N\'6e', 'S7g-8f', 'N6ex5g+', 'B4hx5g', '+R7d-6e', 'S8fx7e', '+R6ex6g', 'S7e-6f', 'P\'7h', 'R7i-2i', 'G\'5h', 'P\'6h', '+R6gx8g', 'B5g-3i', 'P7h-7i+', 'S6f-6e', 'P\'7e', 'P5f-5e', '+R8g-7g', 'P5ex5d', '+R7gx6h', 'P\'6g', 'P4d-4e', 'P5d-5c+', 'B4bx5c', 'P\'5i', 'G5hx5i', 'N\'5e', 'G4c-4b', 'P\'5d', 'B5c-4d', 'S6e-5f', 'P\'5c', 'N3gx4e', 'G5i-4i', 'P5dx5c+', 'G4ix3i', 'R2ix3i', 'B\'4h', '+P5cx4b', 'S3cx4b', 'G3hx4h', '+R6hx4h', 'G\'3h', 'G\'3g', 'K2h-1h', '+R4hx3i', 'G3hx3i', 'P1d-1e', 'S\'4a', 'G3b-3a', 'R\'6c', 'S4b-5c', 'R6cx5c+', 'B4dx5c', 'B\'3c', 'N2ax3c', 'N4ex3c+', 'K2bx3c', 'N\'4e', 'K3c-2b', 'G\'3c', 'K2b-1c', 'S\'1d']

    return game

PSN_TEXT = '''[Event "26. Osho Sen"]
[Venue "Gamagori City, Aichi Prefecture"]
[Date "19760204"]
[Round "3"]
[Sente "Oyama Yasuharu"]
[Gote "Nakahara Makoto"]
[Result "1-0"]
[Annotator "Thomas Majewski"]
[PlyCount "176"]
[TimeControl "205200"]
[Mode "OTB"]
[SFEN "lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL"]

P7g-7f P8c-8d R2h-7h P3c-3d P6g-6f P8d-8e B8h-7g S7a-6b S7i-6h K5a-4b K5i-4h K4b-3b K4h-3h G6a-5b K3h-2h P1c-1d P1g-1f P5c-5d S3i-3h S3a-4b G6i-5h P7c-7d P5g-5f S4b-3c S6h-5g B2b-3a R7h-8h S6b-7c B7g-5i P4c-4d P3g-3f K3b-2b P2g-2f G4a-3b S3h-2g P2c-2d G4i-3h G5b-4c B5i-3g B3a-6d P4g-4f B6d-4b G5h-4g P9c-9d P9g-9f L9a-9c S5g-4h R8b-8d P6f-6e P7d-7e P7fx7e B4bx7e S4h-5g R8d-7d P'7f B7e-4b R8h-7h R7d-8d R7h-8h P'7h S5g-6h P6c-6d B3g-4h R8d-8b P6ex6d S7cx6d N8i-7g S6d-7c R8h-8i S7c-7d N2i-3g P7h-7i+ S6hx7i R8b-6b P'6e P'7e P7fx7e S7dx7e S7i-7h P'7f N7gx8e R6bx6e R8i-6i P'6h R6i-7i P7f-7g+ S7hx7g R6e-6g+ G4g-5g +R6g-6e P'6g P6h-6i+ R7ix6i +R6e-7d N8ex9c N8ax9c R6i-7i N'6e S7g-8f N6ex5g+ B4hx5g +R7d-6e S8fx7e +R6ex6g S7e-6f P'7h R7i-2i G'5h P'6h +R6gx8g B5g-3i P7h-7i+ S6f-6e P'7e P5f-5e +R8g-7g P5ex5d +R7gx6h P'6g P4d-4e P5d-5c+ B4bx5c P'5i G5hx5i N'5e G4c-4b P'5d B5c-4d S6e-5f P'5c N3gx4e G5i-4i P5dx5c+ G4ix3i R2ix3i B'4h +P5cx4b S3cx4b G3hx4h +R6hx4h G'3h G'3g K2h-1h +R4hx3i G3hx3i P1d-1e S'4a G3b-3a R'6c S4b-5c R6cx5c+ B4dx5c B'3c N2ax3c N4ex3c+ K2bx3c N'4e K3c-2b G'3c K2b-1c S'1d'''

class PSNGame_Test(unittest.TestCase):
    def test_init(self):
        game = game_fixture()
        assert game.event == '26. Osho Sen'
        assert game.venue == 'Gamagori City, Aichi Prefecture'
        assert game.date == '19760204'
        assert game.round == '3'
        assert game.sente == 'Oyama Yasuharu'
        assert game.gote == 'Nakahara Makoto'
        assert game.result == '1-0'
        assert game.annotator == 'Thomas Majewski'
        assert game.plycount == '176'
        assert game.timecontrol == '205200'
        assert game.mode == 'OTB'
        assert game.sfen == 'lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL'


class PSN_Test(unittest.TestCase):    
    def test_next_token(self):
        '''Tests ``_next_token`` function'''

        lines = [
            '[Venue "81Dojo"]',
            '[Date "20200401"]',
            '',
            'P7g-7f P3c-3d P7f-7e P8c-8d',
            'R2h-7h',
            '   '
        ]

        token = psn._next_token(lines)
        assert token == '[Venue "81Dojo"]'
        assert len(lines) == 5

        token = psn._next_token(lines)
        assert token == '[Date "20200401"]'
        assert len(lines) == 4

        token = psn._next_token(lines)
        assert token == 'P7g-7f P3c-3d P7f-7e P8c-8d R2h-7h'
        assert len(lines) == 0

        token = psn._next_token(lines)
        assert not token
    
    def test_pre_process_text(self):
        '''Tests ``_pre_process_text`` function'''

        text = '''
        [tag "value"] ;comment

        ; commentary
        P7g-7f P3c-3d P7f-7e P8c-8d ;commentary
        R2h-7h'''

        lines = psn._pre_process_text(text)
        expt = ['[tag "value"]', 'P7g-7f P3c-3d P7f-7e P8c-8d', 'R2h-7h']
        assert lines == expt

    def test_parse_tag(self):
        '''Tests ``_parse_tag`` function'''

        token = '[Venue "Gamagori City, Aichi Prefecture"]'
        tag, value = psn._parse_tag(token)
        assert tag == 'venue'
        assert value == 'Gamagori City, Aichi Prefecture'

    def test_parse_moves(self):
        '''Tests ``_parse_moves`` function'''

        token = 'P7g-7f P3c-3d P7f-7e P8c-8d R2h-7h'
        moves = psn._parse_moves(token)
        assert moves == ['P7g-7f', 'P3c-3d', 'P7f-7e', 'P8c-8d', 'R2h-7h']

    def test_parse_moves_with_commentary(self):
        '''Tests ``_parse_moves`` function with commentary ({})'''

        token = '{start comment}P7g-7f{middlecomment}P3c-3d {dunno}P7f-7e P8c-8d' +\
                ' R2h-7h{end}'

        moves = psn._parse_moves(token)
        expected = ['{start comment}', 'P7g-7f', '{middlecomment}', 'P3c-3d', '{dunno}', 
                    'P7f-7e', 'P8c-8d', 'R2h-7h', '{end}']
        
        assert moves ==  expected

    def test_loads(self):
        '''Tests ``loads`` function'''

        text = '''
        [Venue "81DOjo"]
        [Date "20200401"]

        P7g-7f P3c-3d P7f-7e P8c-8d
        R2h-7h'''

        games = psn.loads(text)
        assert len(games) == 1

    def test_dumps_single(self):
        '''Tests ``dumps`` function for a single game'''
        game = game_fixture()
        dump = psn.dumps(game)

        assert dump == PSN_TEXT

    def test_dumps_multi(self):
        '''Tests ``dumps`` function for a list of games'''
        games = [game_fixture(), game_fixture()]
        dump = psn.dumps(games)

        assert dump == PSN_TEXT+'\n\n\n'+PSN_TEXT
    
    def test_dumps_special(self):
        '''Tests ``dumps`` function with move commentary and null tag'''
        game = psn.PSNGame('XYZ')
        game.moves = ['{comment}', 'P7g-7f', 'P3c-3d', '{in}', 'P7f-7e', '{lol}']

        dump = psn.dumps(game)
        first_expected = '[Event "XYZ"]\n[Venue "?"]'
        last_expected = '{comment} P7g-7f P3c-3d {in} P7f-7e {lol}'
        
        assert dump.startswith(first_expected)
        assert dump.endswith(last_expected)

if __name__ == '__main__':
    unittest.main()
