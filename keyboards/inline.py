from aiogram.utils.keyboard import InlineKeyboardBuilder


def getInlineStartKeyBoard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Выбор города', callback_data='getUsersSettings')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup(one_time_keyboard=True)


def getInlineUserSettingsKeyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Москва', callback_data='Moscow')
    keyboard_builder.button(text='Санкт-Петербург', callback_data='SP')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup(one_time_keyboard=True)



def getInlinePointSettingsKeyboard_M():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='BI Developer', callback_data='BI_M')
    keyboard_builder.button(text='Business Development Manager', callback_data='BDM_M')
    keyboard_builder.button(text='Community Manager', callback_data='CM_M')
    keyboard_builder.button(text='Computer vision', callback_data='CV_M')
    keyboard_builder.button(text='Data Analyst', callback_data='DA_M')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup(one_time_keyboard=True)


def getInlinePointSettingsKeyboard_SP():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='BI Developer', callback_data='BI_SP')
    keyboard_builder.button(text='Business Development Manager', callback_data='BDM_SP')
    keyboard_builder.button(text='Community Manager', callback_data='CM_SP')
    keyboard_builder.button(text='Computer vision', callback_data='CV_SP')
    keyboard_builder.button(text='Data Analyst', callback_data='DA_SP')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup(one_time_keyboard=True)