from typing import Optional
import uvicorn
import requests

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

app = FastAPI()
app.mount("/home", StaticFiles(directory="static"), name="static")
fish_watch_api = 'https://www.fishwatch.gov/api/species/'

FISH_NAMES = []


@app.get("/")
def read_root():
    return RedirectResponse(url="/home/index.html")


@app.get("/names")
def read_names():
    global FISH_NAMES

    if len(FISH_NAMES) > 0:
        return FISH_NAMES

    res = requests.get(fish_watch_api)
    if not res.ok:
        raise HTTPException(status_code=404, detail=res.reason)

    decoded = res.json()
    names = []
    for entry in decoded:
        names.append(entry["Species Name"])

    FISH_NAMES = names

    return names


@app.get("/search/{name}")
def read_item(name: Optional[str] = ""):
    res = requests.get(fish_watch_api + name)
    if not res.ok:
        raise HTTPException(status_code=404, detail=res.reason)

    decoded = res.json()

    if len(decoded) == 0:
        # TODO: Fix statuscode for no results found
        raise HTTPException(status_code=404, detail="No results found")

    return decoded


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000, log_level="info")
