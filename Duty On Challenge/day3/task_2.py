def palindromic(num):
    return str(num) == str(num)[::-1]

def largest_palindromic(start, end):
    max_palindromic = 0
    for i in range(end, start - 1, -1):
        if palindromic(i):
            max_palindromic = max(max_palindromic, i)
    return max_palindromic

start = 100  
end = 200
largest = largest_palindromic(start, end)
print(largest)
