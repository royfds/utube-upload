import logging

from pyrogram import filters as Filters

from ..utubebot import UtubeBot
from ..config import Config


log = logging.getLogger(__name__)


@UtubeBot.on_message(
    Filters.private 
    & Filters.incoming
    & ~Filters.user(Config.AUTH_USERS)
)
async def _non_auth_usr_msg(c, m):
    await m.delete(false)
    log.info(f"{Config.AUTH_USERS} Unauthorised user {m.chat} contacted. Message {m} deleted!!")
