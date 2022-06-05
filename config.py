#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", None)
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "")
    OWNER_ID = os.environ.get("OWNER_ID", 12345)
    LIMIT = int(os.environ.get("LIMIT", "25000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("BQBLUkFng9VnrmdWMx4LajkRxxIcciXsFxnwJr897Ws9GUe-Te8prcGz0UBgle_u3lkUtLnVTEmy97caEjDZkSjR906F9SAhw1JnYoOlTIlo3eimHK2LePkrw-jvXp-VE-lSJyQtMx3dWFiA5qfnv2mMhWp7GO4ArKI7d7aKG_puhH1GTM5SUDOcDYOxkCllYKqQEF75Q6-MTmQe2vYYkuTXqNLx9cFwqw4kJVWAYRsiYxZi4_E-IQcMKBNytdzpYbZUKTx39vZo4QNLeB-oq3s6SmXeoqndFj4BAMMomIo84X9zhh_n_wXZFDhDbjNjZMUn99XILyikbYVkLGy6EkUtAAAAAStVsgAA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", 12345))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
