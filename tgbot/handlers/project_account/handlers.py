from telegram import Update
from telegram.ext import (CallbackContext, CallbackQueryHandler,
                          ConversationHandler, CommandHandler,
                          MessageHandler,Filters)

from tgbot.handlers.project_account.keyboards import send_proj_mode_keyboard, yes_no_mode_keyboard
from tgbot.models import User
from account.models import AccountModel
# from tgbot.handlers.currency import utils

CHECK_PRA_NAME, START_PRA, SELECTION_PRA_MODE, LINK_RECIEVED, PHOTO_RECIEVED, SUMM_RECIEVED = range(6)
account_object = AccountModel()


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
    account_object.user = u
    account_object.project_name = update.message.text
    debug_flag=True
    if AccountModel.objects.filter(user=u, project_name=account_object.project_name).exists():
        text = f'Проект {account_object.project_name} найден. Дополнить его?'
    else:
        text = f'Проект {account_object.project_name} не найден. Создать новый?'
    return stand_message(update, context, output=START_PRA, text=text, keyboard=yes_no_mode_keyboard())


def proj_name_request(update: Update, context: CallbackContext):
    # u = User.get_user(update, context)
    return stand_message(update, context, output=SELECTION_PRA_MODE, text='Как сохранить чек?', keyboard=send_proj_mode_keyboard())


def proj_input_link(update: Update, context: CallbackContext) -> None:
    return stand_message(update, context, output=LINK_RECIEVED, text='вставьте ссылку на электронный чек')


def proj_acc_add_link(update: Update, context: CallbackContext) -> None:
    account_object.bill_link = update.message.text
    return stand_message(update, context, output=SUMM_RECIEVED, text='добавьте сумму по чеку')


def proj_input_photo(update: Update, context: CallbackContext) -> None:
    return stand_message(update, context, output=PHOTO_RECIEVED, text='сделайте фото чека')


def proj_acc_add_photo(update: Update, context: CallbackContext) -> None:
    return stand_message(update, context, output=SUMM_RECIEVED, text='добавьте сумму по чеку')


def proj_acc_add_summ(update: Update, context: CallbackContext) -> None:
    account_object.user = User.get_user(update, context)
    account_object.sum_value = float(update.message.text)
    account_object.save()
    return stand_message(update, context, output=ConversationHandler.END, text='Данные сохранены в базе. До встречи.')


def cancel(update: Update, context: CallbackContext):
    return stand_message(update, context, output=ConversationHandler.END, text='операция отменена')


project_acc_conversation = ConversationHandler(
    entry_points=[CommandHandler('proj_acc', proj_acc_start)],
    states={
        CHECK_PRA_NAME: [MessageHandler(Filters.text, proj_name_check),
                    ],
        START_PRA: [CallbackQueryHandler(proj_name_request, pattern = 'да' ),
                    CallbackQueryHandler(proj_acc_start, pattern = 'нет'),
                    CallbackQueryHandler(cancel, pattern = 'отмена')
        ],
        SELECTION_PRA_MODE: [CallbackQueryHandler(proj_input_link, pattern = 'ссылка' ),
                             CallbackQueryHandler(proj_input_photo, pattern = 'фото'),
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

