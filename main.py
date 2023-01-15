import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

token_kupriyashin = '0112358132134'
session_kupriyashin = vk_api.VkApi(token_kupriyashin)
session_kupriyashin.get_api()

token_group = '0112358132134'
session_group = vk_api.VkApi(token=token_group)
session_group.get_api()

group_id = 203978422


def otvet_comments(object):
    try:
        print(object)
        if 'скрипт' in str(object['text']).lower():  # если чувак хочет получить скрипт
            try:
                info_user = session_group.method('users.get', {
                    'user_ids': str(object['from_id']),
                    'fields': 'screen_name'
                })

                info_user = '@' + info_user[0]['screen_name'] + '(' + info_user[0][
                    'first_name'] + ')' + ', '  # получение обращения к пользователю
                # отправка комментария

                session_group.method('wall.createComment', {
                    'owner_id': str(object['owner_id']),
                    'post_id': str(object['post_id']),
                    'from_group': group_id,
                    'reply_to_comment': str(object['id']),
                    'message': info_user + "Вот ссылочка для доступа:\n"
                                           "__________________________________________\n"
                                           " https://disk.yandex.ru/d/zms3GkrvzmHplw🖥\n"
                                           "__________________________________________\n"
                })
                del info_user
            except Exception as err_script:
                print(f"Ошибка в получении скрипта в комментариях: {err_script}")

        elif object['text'] == '':  # если чувак просто написал коммент без текста

            with open('stikers_id.txt', 'r', encoding='UTF-8') as stikers_ids:
                lines = stikers_ids.readlines()
                import random
                stiker_id = int(lines[random.randint(0, len(lines))].replace('\n', ''))
                del lines

            session_group.method('wall.createComment', {
                'owner_id': str(object['owner_id']),
                'post_id': str(object['post_id']),
                'from_group': group_id,
                'reply_to_comment': str(object['id']),
                'sticker_id': str(stiker_id)
            })
            del stiker_id

        elif 'фот' in str(object['text']).lower() or 'арт' in str(object['text']).lower() or 'крас' in str(
                object['text']).lower():  # если кто-то написал упоминание картинки
            info_user = session_group.method('users.get', {
                'user_ids': str(object['from_id']),
                'fields': 'screen_name'
            })
            info_user = '@' + info_user[0]['screen_name'] + '(' + info_user[0][
                'first_name'] + ')' + ', '  # получение обращения к пользователю

            import poluchenie_randomnogo_arta
            session_group.method('wall.createComment', {
                'owner_id': str(object['owner_id']),
                'post_id': str(object['post_id']),
                'from_group': group_id,
                'reply_to_comment': str(object['id']),
                'message': info_user + 'Держи картиночку😏',
                'attachments': poluchenie_randomnogo_arta.random_art_all()
            })
            del info_user
        else:  # если чувак написал какой то текст, ему должен ответить бот

            with open('stikers_id.txt', 'r', encoding='UTF-8') as stikers_ids:
                lines = stikers_ids.readlines()
                import random
                stiker_id = int(lines[random.randint(0, len(lines))].replace('\n', ''))
                del lines

            session_group.method('wall.createComment', {
                'owner_id': str(object['owner_id']),
                'post_id': str(object['post_id']),
                'from_group': group_id,
                'reply_to_comment': str(object['id']),
                'sticker_id': str(stiker_id)
            })
            del stiker_id
    except Exception as error:
        print('Ошибка в функции ответа на комментарии: ', error)


def otvet_ls(object):
    try:
        if str(object['text']).lower() == 'начать':  # если пользвоатель пишет впервые

            text_ls_privet = "Дарова✋\n Я умный бот *teawithkaguya (かぐや茶 Чай с Кагуей) и я умею следующее: \n" \
                             "\n" \
                             "1⃣ Ты можешь получить рандомную картинку командой - Чай дай арт\n" \
                             "2⃣ Если ты за скриптами, то вот ссылка - https://vk.com/@teawithkaguya-skript-dlya-massovogo-dobavleniya-druzei-v-besedu2022\n" \
                             "3⃣ Можешь со мной просто пообщаться, однако я отвечаю только стикерами(\n" \
                             "\nУдачи😏!"
            import random
            session_group.method('messages.send', {
                'user_id': str(object['from_id']),
                'random_id': random.randint(0, 4294967295),
                'peer_id': str(object['peer_id']),
                'message': text_ls_privet,
                'reply_to': str(object['id'])
            })
            del text_ls_privet

        elif object['text'] == '':  # если в сообщении нет текст кидает стикер
            import random
            with open('stikers_id.txt', 'r', encoding='UTF-8') as stikers_ids:
                lines = stikers_ids.readlines()
                stiker_id = int(lines[random.randint(0, len(lines))].replace('\n', ''))
                del lines
            session_group.method('messages.send', {
                'user_id': str(object['from_id']),
                'random_id': random.randint(0, 4294967295),
                'peer_id': str(object['peer_id']),
                'sticker_id': stiker_id,
                'reply_to': str(object['id'])
            })
            del stiker_id

        elif 'арт' in str(object['text']).lower() or 'картин' in str(object['text']).lower() or 'фот' in str(
                object['text']).lower():  # если пользователь просит рандомный арт
            import poluchenie_randomnogo_arta
            poluchenie_randomnogo_arta.random_art_ids(object)

        else:  # если в сообщении имеется текст отвечает бот

            import random
            with open('stikers_id.txt', 'r', encoding='UTF-8') as stikers_ids:
                lines = stikers_ids.readlines()
                stiker_id = int(lines[random.randint(0, len(lines))].replace('\n', ''))
                del lines
            session_group.method('messages.send', {
                'user_id': str(object['from_id']),
                'random_id': random.randint(0, 4294967295),
                'peer_id': str(object['peer_id']),
                'sticker_id': stiker_id,
                'reply_to': str(object['id'])
            })
            del stiker_id
    except Exception as error:
        print('Произошла ошибка в блоке ответа на личное сообщение: ', error)


while True:
    # Слушаем сервер на предмет событий
    for event in VkBotLongPoll(session_group, group_id=group_id, wait=30).listen():

        if event.type == VkBotEventType.WALL_REPLY_NEW:  # комментарий на стене
            if event.object['from_id'] > 0:  # оставляет комментарий человек, а не группа
                otvet_comments(event.object)  # переходим в файл для ответа на комментарий в сообществе

        if event.type == VkBotEventType.MESSAGE_NEW:  # сообщение в сообществе или беседе
            if event.object['message']['from_id'] > 0:  # пишет не группа, а пользователь
                if event.object['message']['peer_id'] > 2000000000:  # значит пришло сообщение из беседы
                    pass
                else:  # пришло сообщение в лс
                    otvet_ls(
                        event.object['message'])  # переходим в файл otvet_v_ls_gruppi.py и выполняем функцию ответа
