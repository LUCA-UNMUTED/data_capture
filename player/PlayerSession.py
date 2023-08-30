import json
from pathlib import Path


class PlayerSession:
    def __init__(self, player_config: dict, playtime: str):
        self.gender = player_config.get("gender")
        self.name = player_config.get("name")
        self.id = player_config.get("id")
        self.age = player_config.get("age")

        self.playtime = playtime
        self.gsr_dir = None
        self.websocket_dir = None
        self.eog_dir = None

    def set_folders(self, eog, websocket, gsr):
        self.eog_dir = eog
        self.websocket_dir = websocket
        self.gsr_dir = gsr

    def create_player_conf(self, location, file_name):
        # create a conf file for the player
        # **important** we don't record the players name! This is solemnly used to show the name in VR
        conf = {
            "id": self.id,
            "date": self.playtime,
            "age": self.age,
            "gender": self.gender,
        }
        with open(Path(location / file_name), "w+") as c:
            res = json.dumps(conf)
            c.write(res)
