import requests
import datetime
from dotenv import load_dotenv
import os

# 環境変数の読み込み
load_dotenv(dotenv_path="config.env")
API_KEY = os.getenv("API_KEY")

# APIからマップ情報取得
def fetch_map_data() -> dict:
    url = f"https://api.mozambiquehe.re/maprotation?auth={API_KEY}&version=2"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

# JSTに変換
def get_current_time_JST() -> str:
    return (datetime.datetime.utcnow() + datetime.timedelta(hours=9)).strftime("%Y/%m/%d %H:%M")

# マップ情報の抽出
def extract_ranked_maps(data: dict) -> dict:
    current = data["ranked"]["current"]
    next = data["ranked"]["next"]
    remaining_time = f"{current['remainingSecs'] // 3600}時間 {current['remainingSecs'] % 3600 // 60}分"
    
    return {
        "current_map": current["map"],
        "next_map": next["map"],
        "remaining_time": remaining_time,
        "current_asset": current["asset"],
        "next_asset": next["asset"],
        "time_now": get_current_time_JST()
    }