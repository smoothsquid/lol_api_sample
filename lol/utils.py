import logging

from . import api

logger = logging.getLogger(__name__)


def search_match(summoner_name):
    summoner = api.get_summoner_by_name(summoner_name)
    account_id = summoner["accountId"]

    result = api.get_matches_by_account(account_id)
    matches = result["matches"]

    match_list = []
    for match in matches:
        game_id = match["gameId"]
        match_data = api.get_match(game_id)
        participant_id_list = match_data["participantIdentities"]
        match_list.append(
            {
                "game_id": game_id,
                "participant_id_list": participant_id_list,
            }
        )
    return match_list
