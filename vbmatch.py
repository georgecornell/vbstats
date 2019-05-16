
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
    def __init__(self, pos_1, pos_2, pos_3, pos_4, pos_5, pos_6, libero):
        self._id = None
        self._pos_1 = pos_1
        self._pos_2 = pos_2
        self._pos_3 = pos_3
        self._pos_4 = pos_4
        self._pos_5 = pos_5
        self._pos_6 = pos_6
        self._libero = libero

    def rotate(self):
        # returns a new rotation
        pass

    def substitution(self):
        # returns a new rotation
        pass


class VBSet:
    def __init__(self, starting_rotation, vb_match, rotation_no = 1, serve_first=True, team_score1=0, team_score2=0):
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
