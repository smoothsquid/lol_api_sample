import logging

from . import api

logger = logging.getLogger(__name__)


def search_match(summoner_name):
    summoner = api.get_summoner_by_name(summoner_name)
    account_id = summoner["accountId"]

    result = api.get_matches_by_account(account_id)
    matches = result["matches"]

    if matches and len(matches) > 0:
        game_id = matches[0]["gameId"]
        match = api.get_match(game_id)
        participant_id_list = match["participantIdentities"]
        return participant_id_list
