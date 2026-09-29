def counter(text: str) -> int:
    total1 = text.split()
    total2 = len(total1)
    return total2

def characters(text: str) -> dict[str, int]:
    final = {}
    for character in text:
        finalC = character.lower()
        if finalC in final:
            final[finalC] = final[finalC] + 1
        else:
            final[finalC] = 1
    return final

def sort_on(daTuple: tuple[str, int]) -> int:
    return daTuple[1]

def chars_dict_to_sorted_list(daDict: dict[str, int]) -> list[tuple[str, int]]:
    lister = []
    counter = 0
    for temp in daDict:
        counter = daDict[temp]
        lister.append((temp, counter))
    sorter = sorted(lister, reverse=True, key=sort_on)
    return sorter
