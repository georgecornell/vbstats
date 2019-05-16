
class Action:
    def __init__(self, id: int, start_time: int) -> object:
        self._start_time = start_time
        self._id = id

    def increment(self):
        self._id += 1

    def __str__(self):
        result: str = ""
        result += str(self._id)
        result += ";"
        result += str(self._start_time)
        return result


class BeginMatch(Action):
    def __init__(self, id: int, start_time: int) -> object:
        Action.__init__(self, id, start_time)

    def __str__(self):
        return "%s;%s" % (Action.__str__(self), self.__class__.__name__)


class EndMatch(Action):
    def __init__(self, id, start_time):
        Action.__init__(self, id, start_time)

    def __str__(self):
        return "%s;%s" % (Action.__str__(self), self.__class__.__name__)


class BeginSet(Action):
    def __init__(self, id, start_time):
        Action.__init__(self, id, start_time)

    def __str__(self):
        return "%s;%s" % (Action.__str__(self), self.__class__.__name__)


class EndSet(Action):
    def __init__(self, id, start_time):
        Action.__init__(self, id, start_time)

    def __str__(self):
        return "%s;%s" % (Action.__str__(self), self.__class__.__name__)


# 123 9112907;type;pass;team;1;rotation;6;playerJersey;67;quality;1;
class Pass(Action):
    def __init__(self, id, start_time, team, rotation, jersey, quality):
        Action.__init__(self, id, start_time)
        self._team = team
        self._rotation = rotation
        self._jersey_no = jersey
        self._quality = quality

    def __str__(self):
        action_str = "%s;%s;team;%s;rotation;%s;jersey;%s;quality;%s" % \
                     (Action.__str__(self),
                      self.__class__.__name__,
                      self._team,
                      self._rotation,
                      self._jersey_no,
                      self._quality)
        return action_str


# type;attack;team;1;rotation;6;playerJersey;1;result;kill;
# result = 0 .. nothing
# result = 1 .. kill
# result = 2 .. error
class Attack(Action):
    def __init__(self, id: int, start_time: int, team: int, rotation: int, jersey: int, result: int = 0) -> None:
        Action.__init__(self, id, start_time)
        self._team = team
        self._rotation = rotation
        self._jersey_no = jersey
        self._result = result

    def __str__(self):
        action_str = "%s;%s;team;%s;rotation;%s;jersey;%s;result;%s" % \
                     (Action.__str__(self),
                      self.__class__.__name__,
                      self._team,
                      self._rotation,
                      self._jersey_no,
                      self._result)
        return action_str


# 118 9046358;type;scoreAdjustment;team;2;amount;1;
class ScoreAdjustment(Action):
    def __init__(self, id, start_time, team, amount):
        Action.__init__(self, id, start_time)
        self._team = team
        self._amount = amount

    def __str__(self):
        action_str = "%s;%s;team;%s;amount;%s" % \
                     (Action.__str__(self),
                      self.__class__.__name__,
                      self._team,
                      self._amount)
        return action_str


# 7 435226;type;set;team;1;rotation;1;playerJersey;1;result;assist;
# result = 0 .. nothing
# result = 1 .. assist
# result = 2 .. error
class Set(Action):
    def __init__(self, id, start_time, team, rotation, jersey, result=0):
        Action.__init__(self, id, start_time)
        self._team = team
        self._rotation = rotation
        self._jersey_no = jersey
        self._result = result

    def __str__(self):
        action_str = "%s;%s;team;%s;rotation;%s;jersey;%s;result;%s" % \
                     (Action.__str__(self),
                      self.__class__.__name__,
                      self._team,
                      self._rotation,
                      self._jersey_no,
                      self._result)
        return action_str


# 151 9381842;type;serve;team;1;rotation;1;playerJersey;10;result;ace;
# result = 0 .. nothing
# result = 1 .. ace
# result = 2 .. error
class Serve(Action):
    def __init__(self, id, start_time, team, rotation, jersey, result=0):
        Action.__init__(self, id, start_time)
        self._team = team
        self._rotation = rotation
        self._jersey_no = jersey
        self._result = result

    def __str__(self):
        action_str = "%s;%s;team;%s;rotation;%s;jersey;%s;result;%s" % \
                     (Action.__str__(self),
                      self.__class__.__name__,
                      self._team,
                      self._rotation,
                      self._jersey_no,
                      self._result)
        return action_str


# 75 1792544;type;block;team;1;rotation;3;playerJersey;41;result;block;
# result = 0 .. nothing
# result = 1 .. block
# result = 2 .. assist
# result = 3 .. error
class Block(Action):
    def __init__(self, id, start_time, team, rotation, jersey, result=0):
        Action.__init__(self, id, start_time)
        self._team = team
        self._rotation = rotation
        self._jersey_no = jersey
        self._result = result

    def __str__(self):
        action_str = "%s;%s;team;%s;rotation;%s;jersey;%s;result;%s" % \
                     (Action.__str__(self),
                      self.__class__.__name__,
                      self._team,
                      self._rotation,
                      self._jersey_no,
                      self._result)
        return action_str


# 345 11928856;type;dig;team;1;rotation;5;playerJersey;24;result;error;
# result = 0 .. attempt
# result = 1 .. dig
# result = 2 .. error
class Dig(Action):
    def __init__(self, id, start_time, team, rotation, jersey, result=1):
        Action.__init__(self, id, start_time)
        self._team = team
        self._rotation = rotation
        self._jersey_no = jersey
        self._result = result

    def __str__(self):
        action_str = "%s;%s;team;%s;rotation;%s;jersey;%s;result;%s" % \
                     (Action.__str__(self),
                      self.__class__.__name__,
                      self._team,
                      self._rotation,
                      self._jersey_no,
                      self._result)
        return action_str


# 91 2130982;type;freeBall;team;1;rotation;3;playerJersey;41;quality;3;
class FreeBall(Action):
    def __init__(self, id, start_time, team, rotation, jersey, quality):
        Action.__init__(self, id, start_time)
        self._team = team
        self._rotation = rotation
        self._jersey_no = jersey
        self._quality = quality

    def __str__(self):
        action_str = "%s;%s;team;%s;rotation;%s;jersey;%s;quality;%s" % \
                     (Action.__str__(self),
                      self.__class__.__name__,
                      self._team,
                      self._rotation,
                      self._jersey_no,
                      self._quality)
        return action_str


# 120 9077344;type;substitution;team;1;playerIn;43;playerOut;67;
class Substitution(Action):
    def __init__(self, id, start_time, team, player_in, player_out):
        Action.__init__(self, id, start_time)
        self._team = team
        assert isinstance(player_in, int)
        self._player_in = player_in
        assert isinstance(player_out, int)
        self._player_out = player_out

    def __str__(self):
        action_str = "%s;%s;team;%s;player_in;%s;player_out;%s" % \
                     (Action.__str__(self),
                      self.__class__.__name__,
                      self._team,
                      self._player_in,
                      self._player_out)
        return action_str


