from typing import TypeVar
from datetime import datetime
from functools import cached_property

import discord
from discord.ext import commands, Context

from loguru import logger

T = TypeVar("T", bound="Context")

class Emin3m(commands.Bot):
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self._start = datetime.now()
        
    async def on_ready(self):
        logger.info(f"[ {self.user} ( {self.user.id} ) ] logged into Discord...")
        
    async def on_error(self, event, *args, **kwargs):
        logger.error(f"{event=}{args}{kwargs}")
        
    async def on_guild_join(self, guild: discord.Guild):
        pass
    
    async def on_guild_remove(self, guild: discord.Guild):
        pass
    
    async def get_context(self, message: discord.Message, *, cls=Context) -> T:
        return await super().get_context(message, cls=cls)
    
    @property
    def start_time(self):
        return self._start
    
    @cached_property
    def members_count(self) -> int:
        return len(set(self.get_all_members()))
    
    @cached_property
    def guilds_count(self) -> int:
        return len(self.guilds)