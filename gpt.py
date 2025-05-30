from utils.imports import *
from utils.func import *
from g4f.client import Client as GPTClient

#meta name: AI
#meta description: Легкий карманный AI который поможет вам с вашими задачами!
#meta developer: @lscmods
#meta img: https://research.aimultiple.com/wp-content/uploads/2023/03/chatgpt.webp
#meta libs: g4f

gpt_client = GPTClient()

GPT_PROMPT = "\n" #тут можно добалять конкретике для запросов в GPT

def generate_gpt_response(query):
    try:
        response = gpt_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": GPT_PROMPT + query}],
            web_search=False
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Ошибка: {str(e)}"

@app.on_message(filters.command(["gpt"], prefixes=prefix) & filters.user(allow))
async def gpt_command(client, message):
    if len(message.text.split()) < 2:
        await message.edit(f"[❗️] <b>Укажите текст после</b> <code>{prefix}gpt</code>\n<blockquote><b>Пример: <code>{prefix}gpt как дела?</code></b></blockquote>")
        return

    user_query = message.text[4:].strip()
    await message.edit("<b>[🧠] <i>Думаю</i>...</b>")

    reply = generate_gpt_response(user_query)
    await message.edit(f"[✏️] Ваш запрос: <code>{user_query}</code>\n\n[🤖] Ответ: <b>{reply[:4096]}</b>")

modules_help['AI'] = {
  "gpt": "Задать вопрос"
}