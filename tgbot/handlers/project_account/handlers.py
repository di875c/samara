from telegram import Update
from telegram.ext import (CallbackContext, CallbackQueryHandler,
                          ConversationHandler, CommandHandler,
                          MessageHandler,Filters)

from tgbot.handlers.project_account.keyboards import send_proj_mode_keyboard
from tgbot.models import User
# from account.models import AccountModel
# from tgbot.handlers.currency import utils

CHECK_PRA_NAME, START_PRA, SELECTION_PRA_MODE, LINK_RECIEVED, PHOTO_RECIEVED, SUMM_RECIEVED= range(6)


def stand_message(update, context, output, text='', keyboard=None):
    u = User.get_user(update, context)
    # text = update.message.text
    context.bot.send_message(
        chat_id=u.user_id,
        text=text,
        reply_markup=keyboard if keyboard else None
    )
    return output


def proj_acc_start(update: Update, context: CallbackContext):
    return stand_message(update, context, text = 'Введите название нового проекта или существующего', output=CHECK_PRA_NAME)


def proj_name_check(update: Update, context: CallbackContext):
    u = User.get_user(update, context)
    proj_name = update.message.text
    debug_flag=True
    text = f'Проект {proj_name} найден. Дополнить его?' if debug_flag else f'Проект {proj_name} найден. Дополнить его?'
    #TODO добавить модель и ссылку на нее
    # text = f'Проект {proj_name} найден. Дополнить его?' if AccountModel.objects.filter(user=u.user_id,
    #     project_name=proj_name) else f'Проект {proj_name} найден. Дополнить его?'
    return stand_message(update, context, output=START_PRA, text=text)

def proj_name_request(update: Update, context: CallbackContext):
    u = User.get_user(update, context)
    text = update.message.text
    print(text)
    #забрать имя проекта из пред. сессии и сохранить в базе
    return stand_message(update, context, output=SELECTION_PRA_MODE, text='Как сохранить чек?', keyboard=send_proj_mode_keyboard())


def proj_input_link(update: Update, context: CallbackContext) -> None:
    return stand_message(update, context, output=SELECTION_PRA_MODE, text='вставьте ссылку на электронный чек')


def proj_acc_add_link(update: Update, context: CallbackContext) -> None:
    u = User.get_user(update, context)
    # TODO добавить чек в базу
    return stand_message(update, context, output=ConversationHandler.END, text='чек добавлен в базу')


def proj_input_photo(update: Update, context: CallbackContext) -> None:
    return stand_message(update, context, output=PHOTO_RECIEVED, text='сделайте фото чека')


def proj_acc_add_photo(update: Update, context: CallbackContext) -> None:
    return stand_message(update, context, output=SUMM_RECIEVED, text='добавьте сумму по чеку')


def proj_acc_add_summ(update: Update, context: CallbackContext) -> None:
    return stand_message(update, context, output=ConversationHandler.END, text='Фото и сумма сохранены в базе')


def cancel(update: Update, context: CallbackContext):
    return stand_message(update, context, output=ConversationHandler.END, text='операция отменена')


project_acc_conversation = ConversationHandler(
    entry_points=[CommandHandler('proj_acc', proj_acc_start)],
    states={
        CHECK_PRA_NAME: [MessageHandler(Filters.text, proj_name_check),
                    ],
        START_PRA: [MessageHandler(Filters.text, proj_name_request),
        ],
        SELECTION_PRA_MODE: [CallbackQueryHandler(proj_input_link, pattern = 'ссылка на чек' ),
                             CallbackQueryHandler(proj_input_photo, pattern = 'добавить фото'),
                             CallbackQueryHandler(cancel, pattern = 'отмена')
                             ],
        LINK_RECIEVED: [
            MessageHandler(Filters.text, proj_acc_add_link)
        ],
        PHOTO_RECIEVED: [MessageHandler(Filters.photo, proj_acc_add_photo),
                             CommandHandler('cancel', cancel)],

        SUMM_RECIEVED: [MessageHandler(Filters.text, proj_acc_add_summ),
                         CommandHandler('cancel', cancel)],
    },
    fallbacks=[CommandHandler('cancel', cancel)]
)

