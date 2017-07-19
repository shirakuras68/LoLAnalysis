import utility
import json
import os
import sys
from datetime import datetime

gameIds = open("../output/list/gameIds.csv").readlines()

cnt = 0
gameIdsLen = len(gameIds)

for gameId in gameIds:
    gameId = gameId.replace("\n", "")

    # get matchVersion from game json and decide a folder to put each json in the near future
    # "matchVersion": "7.4.176.9828",

    print("expected gameId json = " + gameId)

    if os.path.exists(utility.matchVersionDirectoryPath + gameId + ".json"):
        # exclude from target files
        gameIdsLen -= 1
        print("skipped gameId json = " + gameId + "\n")
        continue

    else:
        # print("we have to create " + gameId + ".csv!")

        gameJson = utility.getLoLGameJson(utility.gameUrl, gameId)

        if gameJson == "" or gameJson == "429":
            print("get json value is [" + gameJson + "]")
            print("Unexpectational error, so it ended.")
            sys.exit()

        cnt += 1

        # detailMatchVersion = gameJson["matchVersion"].split(".")
        #  simpleMatchVersion = str(detailMatchVersion[0]) + "." + str(detailMatchVersion[1])
        # matchVersionDirectoryPath = "../output/game/" + simpleMatchVersion
        # matchVersionDirectoryPath = "../output/game/" + simpleMatchVersion

        if cnt % 10 == 0:
            print(str(cnt) + " / " + str(gameIdsLen) + " " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

        if not os.path.exists(utility.matchVersionDirectoryPath):
            os.mkdir(utility.matchVersionDirectoryPath)

        fjson = open(utility.matchVersionDirectoryPath + gameId + ".json", "w")
        # json.dump(gameJson, fjson, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))

        try:
           # json.dump(gameJson, fjson, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
           json.dump(gameJson, fjson, separators=(',', ': '))
        except UnicodeEncodeError as e:
            print("UnicodeEncodeError [getGamejson] gameId = " + gameId)
            # give up getting json

        fjson.close()