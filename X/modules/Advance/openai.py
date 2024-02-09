from random import choice

from pyX import X, CMD_HELP

from . import *


@X(["openai", "ai", "ask"], langs=True)
async def open_ai(_, message, xd):
    if len(message.command) == 1:
        return await message.reply(f"Type <code>{choice(hndlr)}ai [question]</code> Questions for use OpenAI")
    question = yins.get_cmd(message)
    msg = await message.reply(xd["p"])
    try:
        ai_answer = await yins.ask_ai(question)
        await msg.edit(ai_answer)
    except BaseException as e:
        await msg.edit(xd["err"].format(e))


CMD_HELP.update(
    {"openai": (
        "openai",
        {
            "ai": "Give your question and AI will answer it",
        }
        )
    }
)
