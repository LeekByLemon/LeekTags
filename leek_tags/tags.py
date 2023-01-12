from discord import Cog, ApplicationContext
from leek import DatabaseRequiredError, LeekBot


class Tags(Cog):
    def __init__(self, bot: LeekBot):
        self.bot: LeekBot = bot

    async def cog_before_invoke(self, ctx: ApplicationContext):
        if not self.bot.is_pool_available:
            raise DatabaseRequiredError(self)
