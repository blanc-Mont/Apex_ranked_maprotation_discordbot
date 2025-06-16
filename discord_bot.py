import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import map_rotation  # マップ情報取得のモジュール

# 環境変数の読み込み
load_dotenv(dotenv_path="config.env")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Botの設定
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot起動: {bot.user}")

@bot.command(name="map")
async def send_map_info(ctx):
    data = map_rotation.fetch_map_data()
    map_info = map_rotation.extract_ranked_maps(data)

    embed = discord.Embed(title="🗺️ Apex Legends Rankedマップローテーション", color=0x1E90FF)
    embed.add_field(name="⏰ 現在時刻", value=map_info["time_now"], inline=False)
    embed.add_field(name="🗺️ 現在のマップ", value=map_info["current_map"], inline=False)
    embed.add_field(name="⏳ 残り時間", value=map_info["remaining_time"], inline=False)
    embed.add_field(name="🗺️ 次のマップ", value=map_info["next_map"], inline=False)
    embed.set_image(url=map_info["current_asset"])

    await ctx.send(embed=embed)

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)