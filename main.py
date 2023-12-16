import json
import random

def menu(game):
    print("\nНовая игра! \n")
    while True:
        action = input("Выберите действие: \n" 
              "1 - Посмотреть характеристики \n"
              "2 - Купить предмет \n"
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
            break
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
            if item['name'] == available_item:
                available_items.append(str(item['name']) + " (даёт +" + str(item['damage']) + " урон)")
    items_str = ", ".join(available_items)
    print(f"Предметы: {items_str}.\n")

# торговля использует change_game_values
def trade(state_dict):
    character = state_dict['character']
    all_items = state_dict['items']
    cash_shop = 0
    #available_items = list()
    print("МАГАЗИН")
    action = input("Выберите действие: \n"
                   "1 - Купить предметы\n"
                   "0 - Выйти из магазина \n\n")
    if action == '1':
        print("Выберите предмет:")
        for item in all_items['items']:
            print(item['name'])
            #available_items.append(str(item['name']))
        choice = str(input())
        for item in all_items:
            if choice in item['name']:
                action = input(choice+" стоит "+item['cost']+" монет.\n"
                      "1 - Купить предмет\n"
                      "2 - Назад")
                if action == "1":
                    if character['money'] >= item['cost']:
                        change_game_values()
                        #character['money'] -= item['cost']
                        #character['damage'] += item['damage']
                        #character['hp'] += item['hp']
                        #character['items'].append(item['name'])
                        #cash_shop += item['cost']
                    else:
                        print("У тебя недостаточно денег! Иди отсюда!")
                        menu(game)

                elif action =="2":
                    trade(state_dict)
                else:
                    print("Неправильный ввод. Попробуйте ещё раз")
                    trade(state_dict)
    elif action == '2':
        menu(game)
    else:
        print("Неправильный ввод. Попробуйте ещё раз")
        

def fight(state_dict):
    character = state_dict['character']
    all_enemy = state_dict['enemy']
    enemy = random.choice(all_enemy)
    cube = random.randint(1, 6)
    if cube == 6: #критический удар
        print("Критический удар!") 
        all_enemy.remove(enemy)
        change_game_values()
    elif cube > 3:
        enemy['hp'] -= character['damage']
        if enemy['hp']<=0:
            all_enemy.remove(enemy)
            change_game_values()
    else:
        character['hp'] -= enemy['damage']
        if character['hp'] <= 0:
            print("Вы проиграли!")
            exit()


# сражение использует change_game_values

# TODO: def change_game_values(state_dict)



f = open('game.json', encoding='UTF8')
game = json.load(f)
while True: #чтобы пользователю высвечивалось меню не один раз
    menu(game)
