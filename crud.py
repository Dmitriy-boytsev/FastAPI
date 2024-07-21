from fastapi import Body, FastAPI,status

from db import messages_db

app = FastAPI()


@app.get("/")
async def get_all_messages() -> dict:
    """Функция для вывода всех записей из словаря message_db"""
    return messages_db


@app.get("/message/{message_id}")
async def get_message(message_id: str) -> str:
    """Функция для вывода записи из словаря message_db с принятым message_id"""
    return messages_db[message_id]


@app.post("/message", status_code=status.HTTP_201_CREATED)
async def create_message(message: str = Body()) -> str:
    """Функция для добавляения новых записей при запросе на /message"""
    current_index = len(messages_db)
    messages_db[current_index] = message #Длинна словаря на 1 будет больше, чем индексы внутри нее и таким образом мы добавляем новый индекс в словарь
    return f'Message created'


@app.put("/message/{message_id}")
async def update_message(message_id: str, message: str = Body()) -> str:
    """Изменение записи, получая message_id и message из параметра пути и запроса"""
    messages_db[message_id] = message
    return f'Message update!'


@app.delete("/message/{message_id}")
async def delete_message(message_id: str) -> str:
    """Удаляет записи из словаря message_db с принятым message_id"""
    messages_db.pop(message_id)
    return f'Message {message_id } delete!'


@app.delete("/")
async def kill_message_all() -> str:
    """При запросе к этой функции полностью удалит словарь message_db"""
    messages_db.clear()
    return f'All message delete! Your bd clear!'