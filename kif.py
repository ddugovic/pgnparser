# -*- coding:utf-8 -*-
# Copyright (c) 2011 Renato de Pontes Pereira, renato.ppontes at gmail dot com
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.

import re

'''
A simple KIF parser.

KIF (Kifu Notation) is computer-processible format for recording shogi
games, both the moves and related data. 

This module is based on features of others parser modules (such json and yaml).
The basic usage::

    import kif

    kif_text = open('madoka.kif').read()
    kif_game = kif.KIFGame()

    print kif.loads(kif_text) # Returns a list of KIFGame
    print kif.dumps(kif_game) # Returns a string with a kif game

'''

KIF_ENCODING = '#KIF version=2.0 encoding=UTF-8'
class KIFGame(object):
    '''
    Describes a single shogi game in KIF format.
    '''

    TAG_ORDER = ['Venue', 'Date', 'TimeControl', 'Result', 'Sente', 'Gote']
    TAG_LABEL = ['場所', '開始日時', '持ち時間', '手合割', '先手', '後手']

    def __init__(self, venue=None, date=None, timecontrol=None, result=None, sente=None, gote=None):

        '''
        Initializes the KIFGame, receiving the required tags.
        '''
        self.venue = venue
        self.date = date
        self.timecontrol = timecontrol
        self.result = result
        self.sente = sente
        self.gote = gote

        self.moves = []
    
    def dumps(self):
        return dumps(self)

    def __repr__(self):
        return '<KIFGame "%s" vs "%s">' % (self.sente, self.gote)

class GameStringIterator(object):
    """
        Iterator containing multiline strings
        that represent games from a KIF file
    """

    def __init__(self, file_name):
        """
            Args:
                file_name (str): KIF file name
        """
        self.file_name = file_name
        self.file_iter = iter(open(self.file_name))
        self.game_lines = []
        self.end = False

    def __iter__(self):
        """doc"""
        return self

    def next(self):
        """doc"""
        if self.end is True:
            raise StopIteration
        try:
            while True:
                line = self.file_iter.next()
                if line.startswith("場所") or line.startswith("開始日時"):
                    if len(self.game_lines) == 0:
                        self.game_lines.append(line)
                        continue
                    else:
                        game_lines = self.game_lines[:]
                        self.game_lines = []
                        self.game_lines.append(line)
                        game_str = "".join(game_lines)
                        return game_str
                else:
                    self.game_lines.append(line)
        except StopIteration:
            game_lines = self.game_lines[:]
            game_str = "".join(game_lines)
            self.end = True
            return game_str

class GameIterator(object):
    """
        Iterator containing games from a KIF file
    """

    def __init__(self, file_name):
        """
            Args:
                file_name (str): KIF file name
        """
        self.game_str_iterator = GameStringIterator(file_name)

    def __iter__(self):
        """doc"""
        return self

    def next(self):
        """doc"""
        for game_str in self.game_str_iterator:
            game = loads(game_str)[0]
            return game

def _pre_process_text(text):
    '''
    This function is responsible for removal of blank lines and aditional spaces.
    Also, it converts ``\\r\\n`` to ``\\n``.
    '''
    text = re.sub(r'\s*(\\r)?\\n\s*', '\n', text.strip())
    lines = []
    for line in text.split('\n'):
        line = re.sub(r'(\s*#.*|^\s*)', '', line)
        if line:
            lines.append(line)
    
    return lines

def _next_token(lines):
    '''
    Get the next token from lines (list of text kif file lines).
    '''
    if not lines:
        return None

    token = lines.pop(0).strip() 
    if '：' in token:
        return token

    while lines and not '：' in lines[0]:
        token += ' '+lines.pop(0).strip()
    
    return token.strip()

def _parse_tag(token):
    '''
    Parse a tag token and returns a tuple with (tagName, tagValue).
    '''
    label, value = re.match(r'(\w+)：(.+)', token).groups()
    tag = KIFGame.TAG_ORDER[KIFGame.TAG_LABEL.index(label)]
    return tag.lower(), value.strip('"[] ')

def _parse_moves(token):
    '''
    Parse a moves token and returns a list with movements
    '''
    moves = []
    
    while token:
        token = re.sub(r'^\s*(\d+\.+\s*)?', '', token)

        pos = token.find('\n')
        if pos > 0:
            move, clock = re.match(r'^\s*(?:\d+\s+(\S*)\s+(\S*))?', token[:pos]).groups()
            moves.append(move) # ignore clock for now
            token = token[pos:]
        else:
            move, clock = re.match(r'^\s*(?:\d+\s+(\S*)\s+(\S*))?', token).groups()
            moves.append(move) # ignore clock for now
            token = ''

    return moves

def loads(text):
    '''
    Converts a string ``text`` into a list of KIFGames
    '''
    games = []
    game = None
    lines = _pre_process_text(text)

    while True:
        token = _next_token(lines)

        if not token:
            break

        if '：' in token:
            tag, value = _parse_tag(token)
            if not game or (game and game.moves):
                game = KIFGame()
                games.append(game)

            setattr(game, tag, value)
        elif token != '手数----指手---------消費時間--':
            game.moves = _parse_moves(token)
    
    return games

def dumps(games):
    '''
    Serialize a list of KIFGames (or a single game) into text format.
    '''
    all_dumps = []

    if not isinstance(games, (list, tuple)):
        games = [games]

    for game in games:
        dump = ''
        for i, tag in enumerate(KIFGame.TAG_ORDER):
            if getattr(game, tag.lower()):
                label = KIFGame.TAG_LABEL[i]
                dump += '%s：%s\n' % (label, getattr(game, tag.lower()))
        
        dump += '手数----指手---------消費時間--\n'
        for j, move in enumerate(game.moves):
            dump += str(j+1) + '   ' + move + '\n'
            
        all_dumps.append(dump.strip())
            
    return KIF_ENCODING + '\n' + '\n\n\n'.join(all_dumps)
