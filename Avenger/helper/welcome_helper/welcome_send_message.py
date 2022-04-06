import pyrogram
from pyrogram.types import InlineKeyboardMarkup
from Avenger import AvengerCli
from Avenger.helper.welcome_helper.welcome_fillings import Welcomefillings

async def SendWelcomeMessage(message, NewUserJson, content, text, data_type, reply_markup):
    message_id = message.message_id
    chat_id = message.chat.id
    text = Welcomefillings(message, text, NewUserJson)
    SentMessage = None
    
    if (
        data_type == 1
    ):
        SentMessage = await AvengerCli.send_message(
            chat_id=chat_id,
            text=text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )
    
    elif (
        data_type == 2
    ):
        SentMessage = await AvengerCli.send_sticker(
            chat_id=chat_id,
            sticker=content,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )
    
    elif (
        data_type == 3
    ):
        SentMessage = await AvengerCli.send_animation(
            chat_id=chat_id,
            animation=content,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )

    elif (
        data_type == 4
    ):
        
        SentMessage = await AvengerCli.send_document(
            chat_id=chat_id,
            document=content,
            caption=text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )

    elif (
        data_type == 5
    ):
        SentMessage = await AvengerCli.send_photo(
          chat_id=chat_id,
          photo=content,
          caption=text,
          reply_to_message_id=message_id,
          reply_markup=reply_markup
      )  
    
    elif (
        data_type == 6
    ):
        SentMessage = await AvengerCli.send_audio(
            chat_id=chat_id,
            audio=content,
            caption=text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )
    elif (
        data_type == 7
    ):
        SentMessage = await AvengerCli.send_voice(
            chat_id=chat_id,
            voice=content,
            caption=text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )
    
    elif (
        data_type == 8
    ):
        SentMessage = await AvengerCli.send_video(
            chat_id=chat_id,
            video=content,
            caption=text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )
    
    elif (
        data_type == 9
    ):
        SentMessage = await AvengerCli.send_video_note(
            chat_id=chat_id,
            video_note=content,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )
    
    return SentMessage
