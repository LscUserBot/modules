from utils.imports import *
from utils.func import *
from g4f.client import Client as GPTClient

#meta name: AI
#meta description: Легкий карманный AI который поможет вам с вашими задачами!
#meta developer: @lscmods
#meta img: https://research.aimultiple.com/wp-content/uploads/2023/03/chatgpt.webp
#meta libs: g4f

gpt_client = GPTClient()

def generate_gpt_response(query):
    try:
        response = gpt_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {'role': 'system', 'content': 'Ты должен всегда помогать с чем угодно'},
                {'role': 'user', 'content': query}
            ],
            web_search=False
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Ошибка: {str(e)}"

def generate_random_string(length=5):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

@app.on_message(filters.command("gpt", prefix) & filters.user(allow))
async def gpt_command(client, message):
    if len(message.text.split()) < 2:
        await message.edit(f"[❗️] <b>Укажите текст после</b> <code>{prefix}gpt</code>\n<blockquote><b>Пример: <code>{prefix}gpt как дела?</code></b></blockquote>")
        return

    user_query = message.text[len(prefix)+4:].strip()
    await message.edit("<b>[🧠] <i>Думаю</i>...</b>")

    reply = generate_gpt_response(user_query)

    full_text = f"[✏️] Ваш запрос: <code>{user_query}</code>\n\n[🤖] Ответ: <b>{reply}</b>"
    
    if len(full_text) > 4096:
        file = io.BytesIO(reply.encode())
        file.name = f"gpt_answer_{generate_random_string(5)}.txt"
        
        await client.send_document(
            chat_id=message.chat.id,
            document=file,
            caption=f"[✏️] Ваш запрос: <code>{user_query}</code>\n\n[🤖] Ответ слишком длинный, поэтому я записал его в файл."
        )
        await message.delete()
    else:
        await message.edit(full_text[:4096])

modules_help['AI'] = {
  "gpt": "Задать вопрос"
}
