from utils.imports import *
from utils.func import *

#meta name: LoliHentai
#meta description: Забавная шутчка
#meta developer: @lscmods
#meta img: https://cs7.pikabu.ru/post_img/big/2018/06/08/7/1528456651121933364.jpg

@app.on_message(filters.command('lh', prefixes=prefix) & filters.user(allow))
async def secret(client, message):
  await message.delete()
  await client.send_message('ferganteusbot', '/lh')
  await asyncio.sleep(0.5)
  async for msg in client.get_chat_history('ferganteusbot', limit=1):
    file_id = msg.photo.file_id

  await answer(message, photo=True, response=file_id)


modules_help['LoliHentai'] = {
  "lh": "Получить фото [LH]"
}
