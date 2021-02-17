"""
라이엇 게임즈 API에서 제공하는 챔피언 데이터 JSON파일 champions.json을
데이터베이스에 입력하기 위해 Fixture로 변환합니다.
"""
import json
import os

CHAMPION_JSON_FILE_PATH = "champion.json"

if __name__ == "__main__":
    path = os.path.dirname(os.path.realpath(__file__))
    champions_json_path = os.path.join(path, CHAMPION_JSON_FILE_PATH)

    champions_file = open(champions_json_path, "r", encoding="UTF-8")
    champions_json = json.load(champions_file)

    champions = champions_json["data"]

    fixture = []

    for id in champions:
        champion = champions[id]
        # print(champion)
        champion_item = {}

        champion_item["name_kr"] = champion["name"]
        champion_item["name_en"] = id
        champion_item["title"] = champion["title"]
        champion_item["blurb"] = champion["blurb"]

        image = champion["image"]
        champion_item["image_full"] = image["full"]
        champion_item["image_group"] = image["group"]
        champion_item["image_sprite"] = image["sprite"]
        champion_item["image_sprite_x"] = image["x"]
        champion_item["image_sprite_y"] = image["y"]
        champion_item["image_sprite_w"] = image["w"]
        champion_item["image_sprite_h"] = image["h"]

        fixture_item = {}
        fixture_item["model"] = "lol.Champion"
        fixture_item["pk"] = champion["key"]
        fixture_item["fields"] = champion_item

        fixture.append(fixture_item)

    champions_fixture = open("lol/fixtures/champions.json", "w", encoding="UTF-8")
    champions_fixture.write(json.dumps(fixture))
