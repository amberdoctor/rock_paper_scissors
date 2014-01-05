import random
import string

class RockPaperScissors(object):
    '''
    Rock Paper Scissors Domain Specific Language Example
    '''
    games = [
            {'name':'Rock Paper Scissors', 
            'options':{'rock':['scissors'], 
                        'paper':['rock'], 
                        'scissors':['paper']
                        },
            'shortcut':'RPS'
            },
            {'name':'Rock Paper Scissors Lizard Spock', 
            'options':{'rock':['scissors', 'lizard'], 
                        'spock':['scissors', 'rock'], 
                        'paper':['spock', 'rock'], 
                        'lizard':['paper', 'spock'], 
                        'scissors':['paper', 'lizard']
                        },
            'shortcut':'RPSLS'
            }
    ]

    player_win_message = 'player wins'
    computer_win_message = 'computer wins'
    tied_message = 'a tie'

    def key_list_to_options_string(self, key_list):
        return string.join(key_list[: -1], ', ') + ', or %s ' % key_list[-1]

    def get_player_choice(self, options):
        while True:
            player_choice = raw_input('Choose %s: ' 
                    % self.key_list_to_options_string(options.keys())
                    ).lower()
            if player_choice in options:
                return player_choice 
            print 'Your selection was not valid, please choose again.'

    def get_computer_choice(self, options):
        return random.choice(options.keys())

    def play_round(self, game):
        player_choice = self.get_player_choice(game['options'])
        computer_choice = self.get_computer_choice(game['options'])
        if computer_choice in game['options'][player_choice]:
            results = self.player_win_message
        elif player_choice in game['options'][computer_choice]:
            results = self.computer_win_message
        else:
            results = self.tied_message
        return dict(player_choice=player_choice, 
                computer_choice=computer_choice, results=results
                )

    def get_number_of_rounds(self):
        while True:
            number_of_rounds = raw_input('How many rounds would you like to play? ')
            if self.is_number_of_rounds_valid(number_of_rounds):
                int_number_of_rounds = int(number_of_rounds)
                self.warn_user_on_range(int_number_of_rounds)
                return int_number_of_rounds
            print 'Your selection was not valid, please choose an integer greater than zero.'

    def is_number_of_rounds_valid(self, number_of_rounds):
        try:
            int_number_of_rounds = int(number_of_rounds)
        except ValueError:
            return False
        if not int_number_of_rounds > 0:
            return False
        return True

    def warn_user_on_range(self, number_of_rounds):
        if number_of_rounds > 10:
            print "You're the boss but I hope you don't get bored!"

    def choose_game(self):
        while True:
            game_choice = raw_input('Choose a game (type the name or the shortcut): \n%s\n>>> ' 
                        % string.join(["%s [%s]" % (game['name'], game['shortcut']) for game in self.games], '\n')
                        ).upper()
            for game in self.games:
                if game['name'].upper() == game_choice or game['shortcut'].upper() == game_choice:
                    return game
            print 'Your selection was not valid, please choose again.'

    def play_game(self):
        selected_game = self.choose_game()
        print 'Welcome to %s' % selected_game['name']
        computer_win_count = 0
        player_win_count = 0
        number_of_rounds = self.get_number_of_rounds()
        for round_number in xrange(1, number_of_rounds + 1):
            print '.....'
            print 'Round %i' % round_number
            round_results = self.play_round(selected_game)
            if round_results['results'] == self.player_win_message:
                player_win_count += 1
            elif round_results['results'] == self.computer_win_message:
                computer_win_count += 1
            print 'Player Choice was: ' + round_results['player_choice']
            print 'Computer Choice was: ' + round_results['computer_choice']
            print 'Round %i results: %s!' % (round_number, 
                        round_results['results']
                        )
        print '.....'
        print 'Game Results: '
        print 'Player won %i round(s).' % player_win_count
        print 'Computer won %i round(s).' % computer_win_count
        if player_win_count > computer_win_count:
            print 'The winner of this game is .... The Player!'
        elif computer_win_count > player_win_count:
            print 'The winner of this game is .... The Computer!'
        else:
            print 'The game was tied!'

if __name__ == '__main__':
    RockPaperScissors().play_game()
