from src import masks


def mask_account_card(card_inf:str) -> str:
    '''Обрабатывает информацию как о картах, так и о счетах
    Возвращает строку с замаскированным номером'''
    index = 0
    for i in card_inf:
        if i.isdigit():
            break
        else:
            index += 1

    name = card_inf[:index-1]
    number = card_inf[index:]
    if name == 'Счет':
        number = masks.get_mask_account(number)
    else:
        number = masks.get_mask_card_number(number)
    return name+' '+number


print(mask_account_card('Maestro 1596837868705199'))
print(mask_account_card('Visa Classic 6831982476737658'))
print(mask_account_card('Visa Gold 5999414228426353'))
print(mask_account_card('Счет 73654108430135874305'))
