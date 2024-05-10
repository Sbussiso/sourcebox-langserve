import uuid
from langserve import RemoteRunnable

chat = RemoteRunnable("http://localhost:8000/")
session_id = str(uuid.uuid4())
print(f"session_id: {session_id} \n")

response = chat.invoke({"human_input": "my name is eugene. i like cats. what is your name?"}, {'configurable': { 'session_id': session_id } })
print(response + '\n')

response = chat.invoke({"human_input": "what was my name?"}, {'configurable': { 'session_id': session_id } })
print(response + '\n')

response = chat.invoke({"human_input": "What animal do i like?"}, {'configurable': { 'session_id': session_id } })
print(response + '\n')