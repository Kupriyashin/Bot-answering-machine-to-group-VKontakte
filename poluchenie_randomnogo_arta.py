import random

import requests
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api


def random_art_ids(object):
    try:

        token_kupriyashin = '0112358132134'
        session_kupriyashin = vk_api.VkApi(token_kupriyashin)

        token_group = '0112358132134'
        session_group = vk_api.VkApi(token=token_group)

        group_id = 203978422

        # получаем айди последних тысячи артов из группы
        keybord = VkKeyboard(inline=True)
        keybord.add_button('Хочу еще арт!', color=VkKeyboardColor.POSITIVE)

        # отправляем рандомный арт юзеру
        session_group.method('messages.send', {
            'user_id': str(object['from_id']),
            'random_id': random.randint(0, 4294967295),
            'peer_id': str(object['peer_id']),
            'attachment': random_art_all(),
            'message': 'Держи арт🖼',
            'reply_to': str(object['id']),
            'keyboard': keybord.get_keyboard()
        })
        del keybord
    except Exception as error:
        print('Ошибка в блоке отправки рандомного арта: ', error)


def random_art_all():
    try:
        token_kupriyashin = '0112358132134'
        session_kupriyashin = vk_api.VkApi(token_kupriyashin)

        group_id = 203978422

        ids_fotos = []

        # fotos = session_kupriyashin.method('photos.get', {
        #     'owner_id': str(-group_id),
        #     'album_id': '278906770',
        #     'rev': '1',
        #     'count': '500'
        # })['items']

        METHOD_NAME = "photos.get"
        PARAMETERS = f"owner_id=-203978422&album_id=278906770&rev=1&count=500"
        ACCESS_TOKEN = token_kupriyashin
        V = 5.131

        url = f"https://api.vk.com/method/{METHOD_NAME}?{PARAMETERS}&access_token={ACCESS_TOKEN}&v={V}"
        print(url)
        print('-----------------')

        fotos = requests.get(url=url)

        print(fotos.json())
        print('-----------------')

        for elem in fotos.json()['response']['items']:
            ids_fotos.append(elem['id'])

        del fotos

        ids_fotos = ids_fotos[random.randint(0, len(ids_fotos) - 1)]

        return f"photo-203978422_{ids_fotos}"

    except Exception as error_all_art:
        print(f"Произошла ошибка при выборе рандомного арта: {error_all_art}")

