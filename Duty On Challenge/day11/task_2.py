def anagrams(str1, str2):
    # Remove leading and trailing whitespaces
    str1 = str1.strip()
    str2 = str2.strip()
    
    # Sort both strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    
    # Compare the sorted strings
    return sorted_str1 == sorted_str2

# Test
str1 = " python"
str2 = " phtony"
print(anagrams(str1, str2)) 

str1 = " Java"
str2 = " apaJ"
print(anagrams(str1, str2))  

str1 = " 1234"
str2 = " 2341"
print(anagrams(str1, str2)) 