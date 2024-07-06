def is_pangram(text):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    letters = set(text.lower())
    
    return alphabet.issubset(letters)

# Test
print(is_pangram('Jackdaws love my big sphinx of quartz'))  
print(is_pangram('The jay pig fox zebra and my wolves quack')) 
print(is_pangram('Hello world'))