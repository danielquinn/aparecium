#!/usr/bin/env

import json

from mechanicalsoup import Browser
from flask import Flask

app = Flask(__name__)


@app.route("/<name>")
def main(name):

    with open("config.json") as f:
        account = json.load(f)[name]

    browser = Browser(soup_config={"features": "html.parser"})
    page = browser.get(account["url"]).soup
    form = page.select("#loginform")[0]
    form.select("#user_login")[0]["value"] = account["username"]
    form.select("#user_pass")[0]["value"] = account["password"]
    feed = browser.submit(form, page.url)

    return feed.text


if __name__ == "__main__":
    app.run()
