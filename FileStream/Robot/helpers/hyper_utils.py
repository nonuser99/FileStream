from pyrogram import Client
from HyperDL import HyperTGDownloader
from config import API_ID, API_HASH, BOT_TOKEN, CHUNK_SIZE, HYPERDL_DIR, HYPER_THREADS, HELPER_BOTS


helper_bots = {}
for i, token in enumerate(HELPER_BOTS.split()):
    helper_bots[i] = Client(
        f"helper_{i}",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=token,
        in_memory=True,
        max_concurrent_transmissions=5
    )
helper_loads = {i: 0 for i in helper_bots}

hyperdl = HyperTGDownloader(
    helper_bots=helper_bots,
    helper_loads=helper_loads,
    num_parts=HYPER_THREADS,
    chunk_size=CHUNK_SIZE,
    download_dir=HYPERDL_DIR,
)
