from utils.imports import *
from utils.func import *

from pathlib import Path

#meta name: FileTool
#meta description: Инструменты для работы с файлами и папками
#meta developer: @zxcsolomka
#meta img: https://cdn-icons-png.flaticon.com/512/2587/2587054.png

def generate_random_folder_name(length=8):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def get_file_language(filename):
    extensions = {
        '.py': 'python',
        '.js': 'javascript',
        '.java': 'java',
        '.cpp': 'cpp',
        '.c': 'c',
        '.cs': 'csharp',
        '.php': 'php',
        '.rb': 'ruby',
        '.go': 'go',
        '.rs': 'rust',
        '.swift': 'swift',
        '.kt': 'kotlin',
        '.ts': 'typescript',
        '.sh': 'bash',
        '.html': 'html',
        '.css': 'css',
        '.sql': 'sql',
        '.json': 'json',
        '.xml': 'xml',
        '.md': 'markdown',
        '.txt': 'text'
    }
    ext = os.path.splitext(filename)[1].lower()
    return extensions.get(ext, 'text')

def format_file_tree(path, prefix='', is_full=False):
    if not os.path.isdir(path):
        return "❌ Указанный путь не является папкой"
    
    entries = sorted(os.listdir(path))
    output = []
    
    for i, entry in enumerate(entries):
        is_last = i == len(entries) - 1
        full_path = os.path.join(path, entry)
        
        if os.path.isdir(full_path):
            line = f"{prefix}{'└── ' if is_last else '├── '}{entry}/"
            output.append(line)
            
            if is_full:
                new_prefix = prefix + ('    ' if is_last else '│   ')
                output.append(format_file_tree(full_path, new_prefix, is_full))
        else:
            if entry == os.path.basename(__file__):
                line = f"{prefix}{'└── ' if is_last else '├── '}{entry} [main]"
            else:
                line = f"{prefix}{'└── ' if is_last else '├── '}{entry}"
            output.append(line)
    
    return '\n'.join(output)

@app.on_message(filters.command("cf", prefix) & filters.user(allow))
async def code_file(client: Client, message: Message):
    if len(message.command) < 2:
        await message.edit_text("❌ Укажите путь к файлу")
        return
    
    file_path = message.command[1]
    if not os.path.exists(file_path):
        await message.edit_text("❌ Файл не найден")
        return
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        lang = get_file_language(file_path)
        file_name = os.path.basename(file_path)
        
        if len(content) > 4000:
            await message.reply_document(
                file_path,
                caption=f"📄 Содержимое файла <code>{file_name}</code> слишком большое, отправляю файлом"
            )
        else:
            formatted_content = f"```{lang}\n{content}\n```"
            await message.edit_text(
                f"📄 Содержимое файла <code>{file_name}</code>:\n{formatted_content}"
            )
    except Exception as e:
        await message.edit_text(f"❌ Ошибка: {str(e)}")

@app.on_message(filters.command("ttc", prefix) & filters.user(allow) & filters.reply)
async def text_to_code(client: Client, message: Message):
    if not message.reply_to_message.text:
        await message.edit_text("❌ Ответьте на сообщение с текстом")
        return
    
    if len(message.command) < 2:
        await message.edit_text("❌ Укажите имя файла")
        return
    
    file_name = message.command[1]
    if not file_name.endswith('.py'):
        file_name += '.py'
    
    filetool_dir = os.path.join(".", "FileTool")
    if not os.path.exists(filetool_dir):
        os.makedirs(filetool_dir)
    
    random_folder = generate_random_folder_name()
    save_dir = os.path.join(filetool_dir, random_folder)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    file_path = os.path.join(save_dir, file_name)
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(message.reply_to_message.text)
        
        await message.edit_text(
            f"✅ Текст успешно был сохранен в файл <code>{file_name}</code>!\n"
            f"<blockquote>📂<i>Файл бы сохранен по пути: <code>{file_path}</i></blockquote>"
        )
    except Exception as e:
        await message.edit_text(f"❌ Ошибка при сохранении файла: {str(e)}")

@app.on_message(filters.command("df", prefix) & filters.user(allow) & filters.reply)
async def download_file(client: Client, message: Message):
    if not message.reply_to_message.document:
        await message.edit_text("❌ Ответьте на сообщение с файлом")
        return
    
    save_path = os.path.join(".", "FileTool", "downloads")
    if len(message.command) > 1:
        custom_path = message.command[1]
        if custom_path.startswith("./"):
            save_path = custom_path[2:]
        elif custom_path.startswith(".\\"):
            save_path = custom_path[2:]
        else:
            save_path = custom_path
    
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    document = message.reply_to_message.document
    file_name = document.file_name
    file_path = os.path.join(save_path, file_name)
    
    try:
        await message.reply_to_message.download(file_path)
        await message.edit_text(
            f"✅ Файл <code>{file_name}</code> успешно сохранён!\n"
            f"<blockquote>📂<i>Файл бы сохранен по пути: <code>{file_path}</i></blockquote>"
        )
    except Exception as e:
        await message.edit_text(f"❌ Ошибка при сохранении файла: {str(e)}")

@app.on_message(filters.command("sps", prefix) & filters.user(allow))
async def start_python_script(client: Client, message: Message):
    if len(message.command) < 2:
        await message.edit_text("❌ Укажите путь к скрипту")
        return
    
    script_path = message.command[1]
    if script_path.startswith("./"):
        script_path = script_path[2:]
    elif script_path.startswith(".\\"):
        script_path = script_path[2:]
    
    if not os.path.exists(script_path):
        await message.edit_text("❌ Файл не найден")
        return
    
    if not script_path.endswith('.py'):
        await message.edit_text("❌ Можно запускать только .py файлы")
        return
    
    try:
        subprocess.Popen([sys.executable, script_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
        
        await message.edit_text(
            f"🐍 <i>Python-скрипт</i> <code>{os.path.basename(script_path)}</code> "
            f"(<code>{script_path}</code>) успешно запущен!\n"
            f"<blockquote>🖥 <i>Дополнительная информация в консоли</i></blockquote>"
        )
    except Exception as e:
        await message.edit_text(f"❌ Ошибка при запуске скрипта: {str(e)}")

@app.on_message(filters.command("uf", prefix) & filters.user(allow))
async def unload_file(client: Client, message: Message):
    if len(message.command) < 2:
        await message.edit_text("❌ Укажите путь к файлу")
        return
    
    file_path = message.command[1]
    if file_path.startswith("./"):
        file_path = file_path[2:]
    elif file_path.startswith(".\\"):
        file_path = file_path[2:]
    
    if not os.path.exists(file_path):
        await message.edit_text("❌ Файл не найден")
        return
    
    try:
        await message.delete()
        await message.reply_document(
            file_path,
            caption=f"✅ Файл <code>{os.path.basename(file_path)}</code> успешно выгружен!\n"
                    f"<blockquote>📂<i>Путь до файла: <code>{file_path}</i></blockquote>"
        )
    except Exception as e:
        await message.edit_text(f"❌ Ошибка при выгрузке файла: {str(e)}")

@app.on_message(filters.command("vf", prefix) & filters.user(allow))
async def view_folder(client: Client, message: Message):
    if len(message.command) < 1:
        await message.edit_text("❌ Укажите путь к папке")
        return
    
    path = "."
    is_full = False
    
    if len(message.command) > 1:
        path = message.command[1]
        if len(message.command) > 2 and message.command[2].lower() == "full":
            is_full = True
    
    if path.startswith("./"):
        path = path[2:]
    elif path.startswith(".\\"):
        path = path[2:]
    
    if not os.path.exists(path):
        await message.edit_text("❌ Папка не существует")
        return
    
    if not os.path.isdir(path):
        await message.edit_text("❌ Указанный путь не является папкой")
        return
    
    try:
        tree = format_file_tree(path, is_full=is_full)
        await message.edit_text(
            f"📂 Содержимое папки <code>{path}</code>:\n\n"
            f"<pre>{tree}</pre>"
        )
    except Exception as e:
        await message.edit_text(f"❌ Ошибка: {str(e)}")

modules_help['FileTool'] = {
    "cf": "Показать содержимое файла с кодом",
    "ttc": "Сохранить текст в файл (в ответ на сообщение)",
    "df": "Скачать файл (в ответ на сообщение с файлом)",
    "sps": "Запустить Python скрипт",
    "uf": "Выгрузить любой файл",
    "vf": "Просмотреть содержимое папки"
}