from utils.imports import *
from utils.func import *

import numpy as np
from dateutil.relativedelta import relativedelta

#meta name: LscInfo
#meta developer: @lscmods
#meta description: Команды связанные с информацией о пользователях/группах/сообщениях и т.д.
#meta img: https://github.com/LscUserBot/modules/blob/main/img/lscinfo.png?raw=true
#meta libs: numpy, python-dateutil

data = {
    "1000000": 1380326400, 
    "2768409": 1383264000,
    "7679610": 1388448000,
    "11538514": 1391212000,  
    "15835244": 1392940000,
    "23646077": 1393459000,
    "38015510": 1393632000,
    "44634663": 1399334000,
    "46145305": 1400198000,
    "54845238": 1411257000,
    "63263518": 1414454000,
    "101260938": 1425600000,  
    "101323197": 1426204000,
    "103151531": 1433376000,
    "103258382": 1432771000,
    "109393468": 1439078000,
    "111220210": 1429574000,
    "112594714": 1439683000,
    "116812045": 1437696000,
    "122600695": 1437782000,
    "124872445": 1439856000,
    "125828524": 1444003000,
    "130029930": 1441324000,
    "133909606": 1444176000,
    "143445125": 1448928000,
    "148670295": 1452211000,  
    "152079341": 1453420000,
    "157242073": 1446768000,
    "171295414": 1457481000,
    "181783990": 1460246000,
    "222021233": 1465344000,
    "225034354": 1466208000,
    "278941742": 1473465000,
    "285253072": 1476835000,
    "294851037": 1479600000,
    "297621225": 1481846000,
    "328594461": 1482969000,
    "337808429": 1487707000, 
    "341546272": 1487782000,
    "352940995": 1487894000,
    "369669043": 1490918000,
    "400169472": 1501459000,
    "616816630": 1529625600,  
    "681896077": 1532821500,
    "727572658": 1543708800,
    "796147074": 1541371800,
    "925078064": 1563290000,  
    "928636984": 1581513420,  
    "1054883348": 1585674420,
    "1057704545": 1580393640,
    "1145856008": 1586342040,
    "1227964864": 1596127860,
    "1382531194": 1600188120,
    "1658586909": 1613148540,  
    "1660971491": 1613329440,
    "1692464211": 1615402500,
    "1719536397": 1619293500,
    "1721844091": 1620224820,
    "1772991138": 1617540360,
    "1807942741": 1625520300,
    "1893429550": 1622040000,
    "1972424006": 1631669400,
    "1974255900": 1634000000,
    "2030606431": 1631992680,
    "2041327411": 1631989620,
    "2078711279": 1634321820,
    "2104178931": 1638353220,
    "2120496865": 1636714020,
    "2123596685": 1636503180,
    "2138472342": 1637590800,
    "3318845111": 1618028800,
    "4317845111": 1620028800,
    "5162494923": 1652449800,  
    "5186883095": 1648764360,
    "5304951856": 1656718440,
    "5317829834": 1653152820,
    "5318092331": 1652024220,
    "5336336790": 1646368100,
    "5362593868": 1652024520,
    "5387234031": 1662137700,
    "5396587273": 1648014800,
    "5409444610": 1659025020,
    "5416026704": 1660925460,
    "5465223076": 1661710860,
    "5480654757": 1660926300,
    "5499934702": 1662130740,
    "5513192189": 1659626400,
    "5522237606": 1654167240,
    "5537251684": 1664269800,
    "5559167331": 1656718560,
    "5568348673": 1654642200,
    "5591759222": 1659025500,
    "5608562550": 1664012820,
    "5614111200": 1661780160,
    "5666819340": 1664112240,
    "5684254605": 1662134040,
    "5684689868": 1661304720,
    "5707112959": 1663803300,
    "5756095415": 1660925940,
    "5772670706": 1661539140,
    "5778063231": 1667477640,
    "5802242180": 1671821040,
    "5853442730": 1674866100,  
    "5859878513": 1673117760,
    "5885964106": 1671081840,
    "5982648124": 1686941700,
    "6020888206": 1675534800,
    "6032606998": 1686998640,
    "6057123350": 1676198350,
    "6058560984": 1686907980,
    "6101607245": 1686830760,
    "6108011341": 1681032060,
    "6132325730": 1692033840,
    "6182056052": 1687870740,
    "6279839148": 1688399160,
    "6306077724": 1692442920,
    "6321562426": 1688486760,
    "6364973680": 1696349340,
    "6386727079": 1691696880,
    "6429580803": 1692082680,
    "6527226055": 1690289160,
    "6813121418": 1698489600,
    "6865576492": 1699052400,
    "6925870357": 1701192327,
    "7000000000": 1711889200,  
    "7100000000": 1719772800,  
    "7200000000": 1725148800,
    "7350000000": 1730454400,
    "7500000000": 1735776000,
    "7700000000": 1740960000,
    "7850000000": 1743638400,
    "8000000000": 1746316800,
    "8200000000": 1748995200,
    "8350000000": 1751673600,
    "8500000000": 1754352000,
}

class Function:
    def __init__(self, order: int = 3):
        self.order = order
        self.x, self.y = self._unpack_data()
        self._func = self._fit_data()

    def _unpack_data(self):
        x_data = np.array(list(map(int, data.keys())))
        y_data = np.array(list(data.values()))
        return (x_data, y_data)

    def _fit_data(self):
        fitted = np.polyfit(self.x, self.y, self.order)
        return np.poly1d(fitted)

    def func(self, tg_id: int):
        value = self._func(tg_id)
        return min(value, time.time())

def estimate_registration_date(user_id):
    interpolation = Function()
    registration_time = round(interpolation.func(user_id))
    registration_date = datetime.utcfromtimestamp(registration_time).strftime("%d.%m.%Y")
    return registration_date

def calculate_age(date_str):

    try:
        reg_date = datetime.strptime(date_str, "%d.%m.%Y")
        current_date = datetime.now()
        diff = relativedelta(current_date, reg_date)

        years = diff.years
        months = diff.months
        days = diff.days

        def years_str(n):
            if n % 10 == 1 and n % 100 != 11:
                return "год"
            elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
                return "года"
            else:
                return "лет"

        def months_str(n):
            if n % 10 == 1 and n % 100 != 11:
                return "месяц"
            elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
                return "месяца"
            else:
                return "месяцев"

        def days_str(n):
            if n % 10 == 1 and n % 100 != 11:
                return "день"
            elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
                return "дня"
            else:
                return "дней"

        return f"{years} {years_str(years)}, {months} {months_str(months)}, {days} {days_str(days)}"
    except Exception as e:
        return f"Ошибка расчета возраста: {date_str} -> {str(e)}"
    
async def get_chat_members_count(client, chat_id):
    try:
        if str(chat_id).startswith('-100'):
            chat = await client.get_chat(chat_id)
            return getattr(chat, 'members_count', 'Неизвестно')
        else:
            count = 0
            async for _ in client.get_chat_members(chat_id):
                count += 1
            return count
    except Exception as e:
        print(f"Ошибка при получении участников: {e}")
        return "Неизвестно"


@app.on_message(filters.command("user", prefixes=prefix) & filters.user(allow))
async def user_info(client: Client, message: Message):
    try:
        target_user = None
        user_arg = None

        if len(message.command) > 1:
            user_arg = message.command[1]
            try:
                target_user = await client.get_users(user_arg)
            except Exception as e:
                await message.edit_text("❌ Пользователь не найден!")
                return
        elif message.reply_to_message and message.reply_to_message.from_user:
            target_user = message.reply_to_message.from_user
        else:
            await message.edit_text("❌ Укажите пользователя (ID/username) или ответьте на сообщение!")
            return

        target_user1 = await client.get_chat(target_user.id)

        await message.edit_text('[👀] Ищу информацию...')

        reg_date = estimate_registration_date(target_user.id)
        age_str = calculate_age(reg_date)

        dc_id = target_user.dc_id if hasattr(target_user, 'dc_id') and target_user.dc_id else "Неизвестно"

        info_text = f"""<b><emoji id=6030563507299160824>❗️</emoji> Информация о пользователе:
» ID: <code>{target_user.id}</code>
» Имя: <code>{target_user.first_name} {target_user.last_name or ''}</code>
» Premium: <code>{'✅' if target_user.is_premium else '❌'}</code>
» DC ID: <code>{dc_id}</code>
» Дата регистрации: <code>{reg_date}</code>
» Возраст аккаунта: <code>{age_str}</code>"""

        if target_user.username:
            info_text += f"\n» Username: @{target_user.username}"

        if hasattr(target_user1, 'bio') and target_user1.bio:
            info_text += f"\n» Bio: <code>{target_user1.bio}</code>"

        info_text += "</b>"

        photo_path = None
        async for p in client.get_chat_photos(target_user.id, limit=1):
            photo_path = await client.download_media(p.file_id)
            break

        if photo_path:
            await client.send_photo(
                message.chat.id,
                photo_path,
                caption=info_text
            )
            await message.delete()
            os.remove(photo_path)
        else:
            await message.edit_text(info_text)

    except Exception as e:
        print(f"⚠️ Ошибка в .user: {e}")
        try:
            await message.edit_text(f"❌ Произошла ошибка: <code>{str(e)}</code>")
        except:
            await message.reply_text(f"❌ Произошла ошибка: <code>{str(e)}</code>")


@app.on_message(filters.command("cinfo", prefix) & filters.user(allow))
async def chat_info(client: Client, message: Message):
    
    try:
        if len(message.command) > 1:
            chat_arg = message.command[1]
            chat = await client.get_chat(chat_arg)
        else:
            chat = message.chat

        chat_type = str(chat.type).lower()
        if "channel" in chat_type:
            chat_type_str = "Канал"
            members_text = "подписчиков"
        elif "supergroup" in chat_type:
            chat_type_str = "Супергруппа"
            members_text = "участников"
        elif "group" in chat_type:
            chat_type_str = "Группа"
            members_text = "участников"
        elif "private" in chat_type:
            await message.edit_text("❌ Это личный чат, используйте команду !user")
            return
        else:
            chat_type_str = "Неизвестный тип"
            members_text = "участников"

        members_count = await get_chat_members_count(client, chat.id)
        await message.edit_text('[👀] Ищу информацию...')

        chat_info_text = f"""<b>[🐊] Информация о {'канале' if 'channel' in chat_type else 'чате'}:
» ID: <code>{chat.id}</code>
» Название: <i><code>{chat.title or 'Нет названия'}</code></i>
» Тип: {chat_type_str}
» Видимость: <code>{"Публичный" if chat.username else "Приватный"}</code>"""

        if chat.username:
            chat_info_text += f"\n» Username: @{chat.username}"
        chat_info_text += f"\n» Количество {members_text}: <code>{members_count}</code>"
        if chat.description:
            chat_info_text += f"\n» Описание:\n<pre>{chat.description}</pre>"

        chat_info_text += "</b>"

        photo = None
        if chat.photo:
            photo = await client.download_media(chat.photo.big_file_id)

        if photo:
            try:
                await message.delete()
                await client.send_photo(
                    chat_id=message.chat.id,
                    photo=photo,
                    caption=chat_info_text
                )
                os.remove(photo)
            except Exception as e:
                print(f"Ошибка при отправке фото: {e}")
                await message.edit_text(chat_info_text)
        else:
            await message.edit_text(chat_info_text)

    except Exception as e:
        await message.edit_text(f"❌ Ошибка: {str(e)}")


@app.on_message(filters.command("minfo", prefix) & filters.user(allow))
async def message_info(client: Client, message: Message):
    try:
        replied_message = message.reply_to_message
        if not replied_message:
            await message.edit_text("Вы должны ответить на сообщение!")
            return

        message_info = f'```json\n{replied_message}```'

        if len(message_info) > 4096:
            await message.delete()
            with open("result.txt", "w", encoding="utf-8") as file:
                file.write(str(replied_message))

            try:
                await client.send_document(chat_id=message.chat.id, document="result.txt", caption="Информация о сообщении")
            except Exception as e:
                if "CHAT_SEND_DOCS_FORBIDDEN" in str(e):
                    await message.reply("❌ Отправка документов запрещена в этом чате.")
                else:
                    await message.reply(f"❌ Произошла ошибка: {e}")
            finally:
                os.remove("result.txt")
        else:
            await message.edit_text(message_info)

    except Exception as e:
        await message.edit_text(f"❌ Ошибка при получении информации: {e}")

@app.on_message(filters.command("ctype", prefix) & filters.user(allow))
async def chat_type(client: Client, message: Message):
    try:
        if len(message.command) > 1:
            chat_arg = message.command[1]
            chat = await client.get_chat(chat_arg)
        else:
            chat = message.chat

        if hasattr(chat, "is_premium"):
            await message.edit_text("❌ Это пользователь, а не чат/канал.")
            return

        chat_type = str(chat.type).lower()
        if "channel" in chat_type:
            chat_type_str = "Канал"
        elif "supergroup" in chat_type:
            chat_type_str = "Супергруппа"
        elif "group" in chat_type:
            chat_type_str = "Группа"
        elif "private" in chat_type:
            chat_type_str = "Личный чат"
        else:
            chat_type_str = f"Неизвестный тип ({chat.type})"

        response = (
            f"[🐊] LSC INFO\n"
            f"{chat_type_str}\n"
            f"» ID: <code>{chat.id}</code>\n"
            f"» Название: <code>{chat.title if hasattr(chat, 'title') else 'Нет'}</code>"
        )
        
        if hasattr(chat, 'username') and chat.username:
            response += f"\n» Username: @{chat.username}"

        await message.edit_text(response)

    except Exception as e:
        await message.edit_text(f"❌ Ошибка: {str(e)}")

modules_help['LscInfo'] = {
  "user": "Информация о пользователе",
  "сinfo": "Информация о чате/канале",
  "minfo": "Информация о сообщении",
}
