import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
#code for vk bot that read and replies


def main():

    vk_session = vk_api.VkApi(token='3a85a87e67593dfcd7c510c723033452179c8a89c7ff7abfd6cab9791bca941bece25dfce19bf88d13d30')

    longpoll = VkBotLongPoll(vk_session, '194642179')
    vk = vk_session.get_api()
    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            print('Новое сообщение:')

            print('Для меня от: ', end='')

            print(event.obj.from_id)

            print('Текст:', event.obj.text)
            print()

            vk.messages.send(
                user_id=event.obj.from_id,

                random_id=get_random_id(),
                message=("Ответ")
            )

            print('ok')

        elif event.type == VkBotEventType.MESSAGE_REPLY:
            print('Новое сообщение:')

            print('От меня для: ', end='')

            print(event.obj.peer_id)

            print('Текст:', event.obj.text)
            print()

        elif event.type == VkBotEventType.MESSAGE_TYPING_STATE:
            print('Печатает ', end='')

            print(event.obj.from_id, end=' ')

            print('для ', end='')

            print(event.obj.to_id)
            print()

if __name__ == '__main__':
    main()

