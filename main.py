import os
from pathlib import Path
from time import sleep

import hikari as hk
import lightbulb as lb
from dotenv import load_dotenv
from termcolor import colored

load_dotenv()
TOKEN = os.getenv("TOKEN")
PREFIX = "!"
CSV_HEADER = ["QUOTE", "SPEAKER", "WRITER", "TIME"]

bot = lb.BotApp(
    token=TOKEN,
    prefix=PREFIX,
    help_class=None,
    default_enabled_guilds=(
        580384337044701185, # test server
        1009416096891289651 # SSIS TE22B
        )
)

@bot.listen()
async def ping(ctx: hk.GuildMessageCreateEvent) -> None:
    sleep(60*60)

    with open("quote_book.txt", "w") as f:
        #writer = csv.writer(f, delimiter="|")
        #writer.writerow(CSV_HEADER)
        async for msg in bot.rest.fetch_messages(1009940494828183704):
            f.write(str(msg.content) + "\n")
            #try:
            #    writer.writerow([
            #        str(msg.content).split("*\"")[1].split("\"")[0],
            #        str(msg.content).split(" - "),
            #        str(msg.author),
            #        str(msg.timestamp)
            #        ])
            #except:
            #    writer.writerow([
            #        str(msg.content)
            #    ])
        
        f.close()
    
    await bot.rest.create_message(
        1030014621291126827,
        attachment=hk.File(Path("quote_book.txt"))
    )


bot.run(activity=hk.Activity(type=hk.ActivityType.WATCHING, name="Reading"))
