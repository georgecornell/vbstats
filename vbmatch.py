
class Team:
    def __init__(self, team_name, team_rank=0):
        """

        :type team_rank: integer
        """
        self._id = None
        self._name = team_name
        self._rank = team_rank


class Match:
    def __init__(self, first_team, second_team_id, start_time):
        self._id = None
        self._first_team = first_team
        self._second_team = second_team
        self._start_time = start_time


class Rotation:
    def __init__(self, jersey_1=-1, jersey_2=-1, jersey_3=-1, jersey_4=-1, jersey_5=-1, jersey_6=-1):
        self._rotation = [jersey_1, jersey_2, jersey_3, jersey_4, jersey_5, jersey_6]

    def add_player(self, pos, jersey_no):
        assert isinstance(jersey_no, int)
        assert (pos < 6)
        self._rotation[pos] = jersey_no

    def is_set(self, pos, jersey_no):
        assert isinstance(jersey_no, int)
        assert (pos < 6)
        return self._rotation[pos] > 0

    def rotate(self):
        return Rotation(self._rotation[1:] + self._rotation[:1])

    def substitution(self, current_player_no, new_player_no):
        new_rotation = []
        for jersey in self._rotation:
            if jersey != current_player_no:
                new_rotation.append(jersey)
            else:
                new_rotation.append(new_player_no)
        return Rotation(new_rotation)

class VBSet:
    def __init__(self, starting_rotation, vb_match, rotation_no = 1, team_score1=0, team_score2=0):
        self._id = None
        self._rotation = starting_rotation
        self._rotation_no = rotation_no
        self._match = vb_match
        assert isinstance(team_score1, int)
        self._team_score1 = team_score1
        assert isinstance(team_score2, int)
        self._team_score2 = team_score2
        self._serve_first = serve_first

    def score_team1(self):
        self._team_score1 += 1

    def score_team2(self):
        self._team_score2 += 1

    @property
    def serve_first(self):
        return self._serve_first
