import logging

from django.test import TestCase

from requests.models import Response

from . import api

logger = logging.getLogger(__name__)
logging.disable(logging.NOTSET)
logger.setLevel(logging.DEBUG)


class SummonerTests(TestCase):
    username = "SmoothSquid"

    def test_get_summoner_by_name(self):
        result: dict = api.get_summoner_by_name(self.username)
        self.assertEqual(result["name"].lower(), self.username.lower())
        print(result)

    def test_get_match_by_account(self):
        account_id: str = api.get_summoner_by_name(self.username)["accountId"]
        result = api.get_matches_by_account(account_id)
        matches = result["matches"]
        print(len(matches))

        match_result = api.get_match(matches[0]["gameId"])
        # print(match_result)
        participantIdentities = match_result["participantIdentities"]
        participants = match_result["participants"]
        for participant_id in participantIdentities:
            print(participant_id)

        for participant in participants:
            print(participant)
