import json
import random


def menu(game):
    while True:
        action = input("Выберите действие: \n"
                       "1 - Посмотреть характеристики \n"
                       "2 - Купить предметы \n"
                       "3 - Сражаться \n"
                       "0 - Выход \n\n")
        if action == '1':
            print("\nПросмотр характеристик")
            view(game)
        elif action == '2':
            print("\nТорговля")
            trade(game)
        elif action == '3':
            print("\nСражение")
            fight(game)
        elif action == '0':
            print("\nИгра завершена. \n")
            exit()
        else:
            print("Неправильный ввод. Попробуйте ещё раз")


def view(state_dict):
    character = state_dict['character']
    all_items = state_dict['items']
    print(f"Ваше имя: {character['name']};")
    print(f"Остаток хп: {character['hp']};")
    print(f"Ваш урон: {character['damage']};")
    print(f"Количество денег: {character['money']} монет;")
    available_items = list()
    for available_item in character['items']:
        for item in all_items:
            if item['name'] == available_item and item['damage'] > 0:
                available_items.append(str(item['name']) + " (даёт +" + str(item['damage']) + " к урону)")
            elif item['name'] == available_item and item['hp'] > 0:
                available_items.append(str(item['name']) + " (даёт +" + str(item['hp']) + " к хп)")
    items_str = ", ".join(available_items)
    print(f"Предметы: {items_str}.\n")


def trade(state_dict):
    character = state_dict['character']
    all_items = state_dict['items']
    available_items = list()
    action = input("Выберите действие: \n"
                   "1 - Купить предметы\n"
                   "0 - Выйти из магазина\n\n")
    print("\n")
    if action == '1':
        print("Выберите предмет:\n")
        for item in state_dict['seller']['items']:
            print(str(item))
            for i in all_items:
                if i['name'] == item:
                    available_items.append(i)
        print("\nВведите название предмета:")
        choice = str(input())
        print("\n")
        for item in available_items:
            if choice.lower() == item['name'].lower():
                action = input(choice+" стоит "+str(item['cost'])+" монет.\n"
                      "1 - Купить предмет\n"
                      "2 - Назад\n")
                print("\n")
                if action == "1":
                    if character['money'] >= item['cost']:
                        character['money'] -= item['cost']
                        character['damage'] += item['damage']
                        character['hp'] += item['hp']
                        character['items'].append(item['name'])
                        state_dict['seller']['items'].remove(item['name'])
                        state_dict['seller']['money'] += item['cost']
                        trade(state_dict)
                    else:
                        print("У тебя недостаточно денег! Иди отсюда!")
                        menu(state_dict)

                elif action =="2":
                    trade(state_dict)
            else:
                print("Неправильный ввод. Попробуйте ещё раз\n")
                trade(state_dict)
    elif action == '0':
        menu(game)
    else:
        print("Неправильный ввод. Попробуйте ещё раз\n")


def fight(state_dict):
    character = state_dict['character']
    all_enemy = state_dict['enemy']
    all_items = state_dict['items']
    if not all_enemy:
        print("Вы победили всех врагов! \n")
        menu(state_dict)
    else:
        enemy = random.choice(all_enemy)
        print("Против вас " + str(enemy['name']))
        cube = random.randint(1, 6)
        if cube == 6:  # критический удар
            print("Критический удар!")
            all_enemy.remove(enemy)
            if enemy['items'] != []:
                for item in enemy['items']:
                    for i in all_items:
                        if i['name']==item:
                            character['items'].append(item)
                            character ['hp'] += i['hp']
                            character['damage'] += i['damage']
            character['money'] += enemy['money']
            print("Победа!\n")
            menu(state_dict)
        elif cube > 3:
            print("Вы нанесли удар! \n")
            enemy['hp'] -= character['damage']
            if enemy['hp'] <= 0:
                all_enemy.remove(enemy)
                if enemy['items'] != []:
                    for item in enemy['items']:
                        for i in all_items:
                            if i['name'] == item:
                                character['items'].append(item)
                                character['hp'] += i['hp']
                                character['damage'] += i['damage']
                character['money'] += enemy['money']
                print("Победа!")
                menu(state_dict)
        else:
            character['hp'] -= enemy['damage']
            print("По вам нанесли удар \n")
            if character['hp'] <= 0:
                print("Вы проиграли!")
                exit()


f = open('game.json', encoding='UTF8')
game = json.load(f)
print("\nНовая игра! \n")
menu(game)
