from typing import Optional
from typing import Dict

import chainlit as cl
from chainlit.types import ThreadDict

import cohere

from prompts.question_answering_prompt import QUESTION_ANSWERING_PROMPT
from config.cohere import Cohere_Config


cohere_cfg = Cohere_Config()
cohere_api_key = cohere_cfg.get_api_key()
cohere_model_name = cohere_cfg.get_model_name()

co = cohere.ClientV2(api_key=cohere_api_key, log_warning_experimental_features=False)


# @cl.oauth_callback
# def oauth_callback(
#     provider_id: str,
#     token: str,
#     raw_user_date: Dict[str, str],
#     default_user: cl.User,
# ) -> Optional[cl.User]:
#     return default_user

    
# @cl.password_auth_callback
# def auth_callback(username: str, password: str):
#     # Lấy tên người dùng khớp với tên người dùng từ cơ sở dữ liệu của bạn
#     # và so sánh mật khẩu đã băm với giá trị được lưu trữ trong cơ sở dữ liệu
#     # IMPORTANT: Hãy băm mật khẩu trước khi lưu trữ chúng
#     if (username, password) == ("admin", "admin"):
#         return cl.User(
#             identifier="admin",
#             metadata={"role": "admin", "provider": "credentials"}
#         )
#     else:
#         return None


@cl.set_starters
async def set_starters():
    return [
        cl.Starter(
            label="Morning routine ideation",
            message="Can you help me create a personalized morning routine?",
            icon="public/idea.svg",
        ),

        cl.Starter(
            label="Explain superconductors",
            message="Explain superconductors like I'm 5 years old.",
            icon="public/learn.svg",
        ),

        cl.Starter(
            label="Python script for daily email reports",
            message="Write a Python script that sends daily email reports.",
            icon="public/terminal.svg",
        ),

        cl.Starter(
            label="Text inviting friend to wedding",
            message="Write a text asking a friend to be my plus-one at the wedding next month.",
            icon="public/write.svg",
        )
    ]


@cl.on_chat_start
async def on_chat_start():
    print("A new chat session has started!")


@cl.on_message
async def on_message(message: cl.Message):
    msg = cl.Message(content="")

    response = co.chat_stream(
        model=cohere_model_name,
        messages=[
            {"role": "system", "content": QUESTION_ANSWERING_PROMPT.format(bot_name="trợ lý bác sĩ AI")},
            {"role": "user", "content": message.content}
        ]
    )

    for event in response:
        if event:
            if event.type == "content-delta":
                await msg.stream_token(event.delta.message.content.text)
    
    # messages = cl.chat_context.to_openai()

    # newest_message = messages[-1]
    # newest_message = message.content

    # Send response to the user
    # response = f"Hello, you just sent: {message.content}!"
    # await cl.Message(response).send()
    print("User: ", cl.user_session.get("user"))

@cl.on_stop
def on_stop():
    print("The user want to stop the task!")


@cl.on_chat_end
def on_chat_end():
    print("The user disconnected!")


# # On Chat Resume
# # Khi người dùng tiếp tục phiên trò chuyện trước đó, 
# # điều này chỉ xảy ra khi chức năng xác thực và lưu trữ dữ liệu được bật
# @cl.on_chat_resume
# async def on_chat_resume():
#     print("The user resumed the previous chat session!")