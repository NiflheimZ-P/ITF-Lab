"""Pre - Blackjack"""
def main():
    """Pre - Blackjack"""
    Total_card = int(input())
    point = 0
    ace = 0
    for _ in range(Total_card):
        get_card = input().lower()
        if get_card in "jqk":
            point += 10
        elif get_card == "a":
            ace += 1
        else:
            point += int(get_card)
    while ace:
        ace -= 1
        if point + 11 > 21 or (point == 10 and ace == 1):
            point += 1
        else:
            point += 11
    print(point)
main()
