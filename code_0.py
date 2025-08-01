def count_words(phrase):
	words = phrase.split()
	return len(words)
	
user_input = input("Digite uma frase: ")
total = count_words(user_input)
print(f"A frase tem um total de {total} palavras. ")
