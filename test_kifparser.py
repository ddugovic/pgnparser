import unittest
import kif

def game_fixture():
    game = kif.KIFGame(
        '81Dojo',
        '2020/05/02',
        '15分+60秒',
        '平手',
        'Toadofsky',
        'zhangpuquan'
    )
    game.moves = ['２六歩(27)   (0:10/0:0:10)',
                  '３四歩(33)   (0:4/0:0:4)']
    return game

KIF_TEXT = '''場所：81Dojo
開始日時：2020/05/02
持ち時間：15分+60秒
手合割：平手
先手：Toadofsky
後手：zhangpuquan
手数----指手---------消費時間--
1   ２六歩(27)   (0:10/0:0:10)
2   ３四歩(33)   (0:4/0:0:4)'''

class KIFGame_Test(unittest.TestCase):
    def test_init(self):
        game = game_fixture()
        assert game.venue == '81Dojo'
        assert game.date == '2020/05/02'
        assert game.sente == 'Toadofsky'
        assert game.gote == 'zhangpuquan'
        assert game.result == '平手'
        assert game.timecontrol == '15分+60秒'

class KIF_Test(unittest.TestCase):    
    def test_next_token(self):
        '''Tests ``_next_token`` function'''

        lines = [
            '場所：81Dojo',
            '開始日時：2020/05/02',
            '手数----指手---------消費時間--',
            '1   ２六歩(27)   (0:10/0:0:10)',
            '2   ３四歩(33)   (0:4/0:0:4)'
        ]

        token = kif._next_token(lines)
        assert token == '場所：81Dojo'
        assert len(lines) == 4

        token = kif._next_token(lines)
        assert token == '開始日時：2020/05/02'
        assert len(lines) == 3

        token = kif._next_token(lines)
        assert token == '手数----指手---------消費時間-- 1   ２六歩(27)   (0:10/0:0:10) 2   ３四歩(33)   (0:4/0:0:4)'
        assert len(lines) == 0

        token = kif._next_token(lines)
        assert not token
    
    def test_pre_process_text(self):
        '''Tests ``_pre_process_text`` function'''

        text = '''#KIF version=2.0 encoding=UTF-8
        場所：81Dojo
        手数----指手---------消費時間--
        1   ２六歩(27)   (0:10/0:0:10)
        2   ３四歩(33)   (0:4/0:0:4)'''

        lines = kif._pre_process_text(text)
        expt = ['場所：81Dojo', '手数----指手---------消費時間--', '1   ２六歩(27)   (0:10/0:0:10)', '2   ３四歩(33)   (0:4/0:0:4)']
        assert lines == expt
    
    def test_parse_tag(self):
        '''Tests ``_parse_tag`` function'''

        token = '場所：81Dojo'
        tag, value = kif._parse_tag(token)
        assert tag == 'venue'
        assert value == '81Dojo'

    def test_parse_moves(self):
        '''Tests ``_parse_moves`` function'''

        token = '1   ２六歩(27)   (0:10/0:0:10)\n2   ３四歩(33)   (0:4/0:0:4)'
        moves = kif._parse_moves(token)
        assert moves == ['２六歩(27)', '３四歩(33)']

    def test_loads(self):
        '''Tests ``loads`` function'''

        text = '''
        場所：81Dojo
        開始日時：2020/05/02
        手数----指手---------消費時間--
        1   ２六歩(27)   (0:10/0:0:10)
        2   ３四歩(33)   (0:4/0:0:4)'''

        games = kif.loads(text)
        assert len(games) == 1

    def test_dumps_single(self):
        '''Tests ``dumps`` function for a single game'''
        game = game_fixture()
        dump = kif.dumps(game)

        assert dump == kif.KIF_ENCODING+'\n'+KIF_TEXT

    def test_dumps_multi(self):
        '''Tests ``dumps`` function for a list of games'''
        games = [game_fixture(), game_fixture()]
        dump = kif.dumps(games)

        assert dump == kif.KIF_ENCODING+'\n'+KIF_TEXT+'\n\n\n'+KIF_TEXT

if __name__ == '__main__':
    unittest.main()
