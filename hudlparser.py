from typing import List

from lxml import etree
import vbaction
import vbmatch


def make_action(moment_dict, vb_id):
    # print(moment_dict)
    if moment_dict["type"] == "beginMatch":
        begin_match = vbaction.BeginMatch(vb_id, int(moment_dict["startTimeMs"]))
        return begin_match
    if moment_dict["type"] == "endMatch":
        end_match = vbaction.EndMatch(vb_id, int(moment_dict["startTimeMs"]))
        return end_match
    if moment_dict["type"] == "beginSet":
        begin_set = vbaction.BeginSet(vb_id, int(moment_dict["startTimeMs"]))
        return begin_set
    if moment_dict["type"] == "endSet":
        end_set = vbaction.EndSet(vb_id, int(moment_dict["startTimeMs"]))
        return end_set
    if moment_dict["type"] == "pass":
        vb_pass = vbaction.Pass(vb_id,
                                int(moment_dict["startTimeMs"]),
                                int(moment_dict["team"]),
                                int(moment_dict["rotation"]),
                                int(moment_dict["playerJersey"]),
                                int(moment_dict["quality"]))
        return vb_pass
    if moment_dict["type"] == "attack":
        result = 0 if "result" not in moment_dict else 1 if moment_dict["result"] == "kill" else -1
        attack = vbaction.Attack(vb_id,
                                 int(moment_dict["startTimeMs"]),
                                 int(moment_dict["team"]),
                                 int(moment_dict["rotation"]),
                                 int(moment_dict["playerJersey"]),
                                 result)
        return attack
    if moment_dict["type"] == "scoreAdjustment":
        score_adjustment = vbaction.ScoreAdjustment(vb_id,
                                                    int(moment_dict["startTimeMs"]),
                                                    int(moment_dict["team"]),
                                                    int(moment_dict["amount"]))
        return score_adjustment
    if moment_dict["type"] == "set":
        result = 0 if "result" not in moment_dict else 1 if moment_dict["result"] == "assist" else -1
        vb_set = vbaction.Set(vb_id,
                              int(moment_dict["startTimeMs"]),
                              int(moment_dict["team"]),
                              int(moment_dict["rotation"]),
                              int(moment_dict["playerJersey"]),
                              result)
        return vb_set
    if moment_dict["type"] == "serve":
        result = 0 if "result" not in moment_dict else 1 if moment_dict["result"] == "ace" else -1
        vb_serve = vbaction.Serve(vb_id,
                                  int(moment_dict["startTimeMs"]),
                                  int(moment_dict["team"]),
                                  int(moment_dict["rotation"]),
                                  int(moment_dict["playerJersey"]),
                                  result)
        return vb_serve

    if moment_dict["type"] == "block":
        result = 0
        if "result" in moment_dict:
            if moment_dict["result"] == "block":
                result = 1
            else:
                if moment_dict["result"] == "assist":
                    result = 2
                else:
                    result = -1
        vb_block = vbaction.Block(vb_id,
                                  int(moment_dict["startTimeMs"]),
                                  int(moment_dict["team"]),
                                  int(moment_dict["rotation"]),
                                  int(moment_dict["playerJersey"]),
                                  result)
        return vb_block

    if moment_dict["type"] == "dig":
        result = 1 if "result" not in moment_dict else -1 if moment_dict["result"] == "error" else 0
        vb_dig = vbaction.Dig(vb_id,
                              int(moment_dict["startTimeMs"]),
                              int(moment_dict["team"]),
                              int(moment_dict["rotation"]),
                              int(moment_dict["playerJersey"]),
                              result)
        return vb_dig

    if moment_dict["type"] == "freeBall":
        free_ball = vbaction.FreeBall(vb_id,
                                      int(moment_dict["startTimeMs"]),
                                      int(moment_dict["team"]),
                                      int(moment_dict["rotation"]),
                                      int(moment_dict["playerJersey"]),
                                      int(moment_dict["quality"]))
        return free_ball

    if moment_dict["type"] == "substitution":
        substitution = vbaction.Substitution(vb_id,
                                             int(moment_dict["startTimeMs"]),
                                             int(moment_dict["team"]),
                                             int(moment_dict["playerIn"]),
                                             int(moment_dict["playerOut"]))
        return substitution


def calculate_rotations(moments):
    current_set = 0
    active_set = 0
    rotations: List[vbmatch.Rotation] = []
    for moment in moments:
        if isinstance(moment, vbaction.BeginSet):
            current_set += 1
            active_set = current_set
            rotations.append(vbmatch.Rotation())

        if isinstance(moment,vbaction.Serve):
            if not rotations[active_set].is_set():
                rotations[active_set].add_player(moment.rotation, moment.jersey_no)
        if isinstance(moment, vbaction.EndSet):
            active_set = -1

    return rotations



def play_moments(moments, teams, starting_rotation, server_first):
    vb_match = None
    vb_set = None
    for moment in moments:
        if isinstance(moment, vbaction.BeginMatch):
            vb_match = vbmatch.Match(match_id, teams[0], teams[1])
        if isinstance(moment, vbaction.BeginSet):
            vb_set = vbmatch.VBSet(starting_rotation, vb_match, 1, 0, 0))




def parse_xml(xml_file: object) -> object:
    """
    Parse the xml
    """
    parser_hudl = etree.iterparse(xml_file)

    i = 0
    moments = []
    teams = []
    for action, elem in parser_hudl:
        if elem.tag == "value" and elem.getparent().tag == "team":
            teams.append(elem.text)
        if elem.tag == "moment":
            i += 1
            key_value = ""
            moment_dict = {}
            for node in elem.iter():
                if node.tag == "startTimeMs":
                    moment_dict["startTimeMs"] = node.text
                if node.tag == "key":
                    key_value = node.text
                if node.tag == "value":
                    moment_dict[key_value] = node.text

            vbaction = make_action(moment_dict, i)
            print(vbaction)
            moments.append(vbaction)

    rotations = calculate_rotations(moments)
    play_moments(moments, teams, rotations)


if __name__ == "__main__":
    parse_xml("/Users/gcornell/Downloads/Hudl_EpicUnited13Black_190505.xml")
