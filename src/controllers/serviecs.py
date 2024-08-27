import requests
from fastapi.responses import JSONResponse
from fastapi import status, HTTPException
from src.core.config import settings
from src.database.connect import redis_client
from datetime import datetime, timedelta
from src.middleware.logging import logger


def get_top_news_ids(count: int, url: str):
    try:
        logger.info("%s", "Getting tops new ids form Hacker News api")
        ids = requests.get(url=f"{url}newstories.json?print=pretty").json()
        res = []
        for i in range(count):
            res.append(ids[i])

        logger.info("%s - %s", f"Top {count} news ids", res)
        return res

    except Exception as e:
        logger.error("%s %s", "Exception Ocurres : ", e)

        raise HTTPException(status_code=500, detail="exception ocurrs")


def hacker_news_service(count: int):
    logger.info("%s", "News Api excution started")

    try:
        res = redis_client.get(f"response_{count}")
        if res is None:
            response = []
            api_url = settings.HACKER_NEWS_API_URL
            ids = get_top_news_ids(count, api_url)

            for id in ids:

                data = requests.get(url=f"{api_url}item/{id}.json?print=pretty").json()
                response.append(data)
            redis_client.set(f"response_{count}", str(response))
            redis_client.expire("response", timedelta(seconds=600))

        else:
            response = eval(res.decode("utf-8"))

        logger.info("%s", "News Api excution compelete")

        return JSONResponse(content={"news": response}, status_code=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        logger.error("%s %s", "Exception Ocurres : ", e)
        raise HTTPException(status_code=500, detail="exception ocurrs")
