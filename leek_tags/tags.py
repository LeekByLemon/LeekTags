from aiomysql import Cursor
from discord import Cog, ApplicationContext, slash_command, Option, AutocompleteContext
from leek import DatabaseRequiredError, LeekBot, localize
from pymysql import IntegrityError

CREATE = "CREATE TABLE IF NOT EXISTS tags_%s (id INT NOT NULL auto_increment, name TEXT NOT NULL UNIQUE, " \
         "content TEXT NOT NULL, primary key (id))"
FETCH_ALL = "SELECT (name) FROM tags_%s"
FETCH_SINGLE = "SELECT (content) FROM tags_%s WHERE name=%s"
ADD = "INSERT INTO tags_%s (name, content) VALUES (%s, %s)"


async def get_tag_names(ctx: AutocompleteContext):
    if not isinstance(ctx.bot, LeekBot):
        return []

    bot: LeekBot = ctx.bot

    if not bot.is_pool_available:
        return []

    async with bot.connection as connection:
        cursor: Cursor = await connection.cursor()
        await cursor.execute(CREATE, [ctx.interaction.guild.id])
        await connection.commit()
        await cursor.execute(FETCH_ALL, [ctx.interaction.guild.id])
        tags = await cursor.fetchall()
        await cursor.close()
        return [x[0] for x in tags]


class Tags(Cog):
    def __init__(self, bot: LeekBot):
        self.bot: LeekBot = bot

    async def cog_before_invoke(self, ctx: ApplicationContext):
        if not self.bot.is_pool_available:
            raise DatabaseRequiredError(self)

    @slash_command()
    async def tag(self, ctx: ApplicationContext, name: Option(str, "The tag name", autocomplete=get_tag_names)):
        """
        Views a specific tag.
        """
        async with self.bot.connection as connection:
            cursor: Cursor = await connection.cursor()
            await cursor.execute(CREATE, [ctx.interaction.guild.id])
            await connection.commit()
            await cursor.execute(FETCH_SINGLE, [ctx.interaction.guild.id, name])
            tag = await cursor.fetchone()
            await cursor.close()

        if tag is None:
            await ctx.respond(localize("TAGS_NOT_FOUND", ctx.locale), ephemeral=True)
        else:
            await ctx.respond(tag[0])

    @slash_command()
    async def createtag(self, ctx: ApplicationContext, name: str, content: str):
        """
        Creates a new tag.
        """
        try:
            async with self.bot.connection as connection:
                cursor: Cursor = await connection.cursor()
                await cursor.execute(CREATE, [ctx.interaction.guild.id])
                await cursor.execute(ADD, [ctx.interaction.guild.id, name, content])
                await connection.commit()
                await cursor.close()
                await ctx.respond(localize("TAGS_ADD_OKAY", ctx.locale, name), ephemeral=True)
        except IntegrityError:
            await ctx.respond(localize("TAGS_ADD_DUPE", ctx.locale, name), ephemeral=True)
