import logging

import requests

from config.secret_settings import LOL_API_KEY

logger = logging.getLogger(__name__)

BASE_URL = "https://kr.api.riotgames.com/lol"

GET_SUMMONER = "summoner/v4/summoners"
BY_NAME = "by-name"

GET_MATCH = "match/v4/matches"

GET_MATCHLIST = "match/v4/matchlists"
BY_ACCOUNT = "by-account"


def join_url(*args):
    return "/".join([BASE_URL, *args])


def get_token_header():
    return {"X-Riot-Token": LOL_API_KEY}


def get_summoner_by_name(name: str):
    response = requests.get(
        url=join_url(GET_SUMMONER, BY_NAME, name),
        headers=get_token_header(),
    )
    logger.debug(response)
    return response.json()


def get_matches_by_account(account_id: str):
    response = requests.get(
        url=join_url(GET_MATCHLIST, BY_ACCOUNT, account_id),
        headers=get_token_header(),
    )
    logger.debug(response)
    return response.json()


def get_match(match_id):
    if type(match_id) == int:
        match_id = str(match_id)

    response = requests.get(
        url=join_url(GET_MATCH, match_id),
        headers=get_token_header(),
    )
    logger.debug(response)
    return response.json()
