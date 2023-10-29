def solve(s:str)-> list[str]:
    if len(s) in range(1,1000):
        list_words = s.split(' ')
        new_list =[]
        for word in list_words:
            if word.isalpha():
                new_list.append(f'{word[0].upper()}{word[1:len(word)]}')
            else:
                new_list.append(word)
        final_list = (" ".join(new_list))
        return final_list
print(solve('12AA ala ma kota 22Af d33'))
