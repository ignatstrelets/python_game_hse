import json

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

# TODO: def trade(state_dict):
# торговля использует change_game_values

# TODO: def fight(state_dict):
# сражение использует change_game_values

# TODO: def change_game_values(state_dict)


f = open('game.json', encoding='UTF8')
game = json.load(f)

menu(game)
