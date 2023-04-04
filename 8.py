def count_vowels_consonants(text):
 vowels = 0
consonants = 0
for char in text:
if char.lower() in 'aeiou':
  vowels += 1
 elif char.isalpha():
    consonants += 1
    return vowels, consonants

input_text = input("Введіть рядок: ")
vowels_count, consonants_count = count_vowels_consonants(input_text)

print("Кількість голосних літер: ", vowels_count)
print("Кількість приголосних літер: ", consonants_count)