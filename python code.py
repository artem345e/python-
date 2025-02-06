def process_string(input_str):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    # Вибір голосних
    vowels_in_str = [char for char in input_str if char in vowels]
    vowels_in_str.sort(reverse=True)  # Зворотній алфавітний порядок
    vowels_str = ''.join(vowels_in_str)

    # Вибір приголосних
    consonants_in_str = [char for char in input_str if char in consonants]
    consonants_in_str.sort(reverse=True)  # Зворотній алфавітний порядок
    consonants_str = ''.join(consonants_in_str)

    # Перевірка на кількість приголосних
    more_than_three_consonants = len(consonants_in_str) > 3

    return (vowels_str, more_than_three_consonants, consonants_str)

# Приклад 
input_string = "abcdefg"
output = process_string(input_string)
print(output)
