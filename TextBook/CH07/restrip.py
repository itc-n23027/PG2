def custom_strip(s, chars=None):
    if chars is None:
        chars = ' \t\n\r\x0b\x0c'  

    start = 0
    end = len(s) - 1

    while start <= end and s[start] in chars:
        start += 1

    while end >= start and s[end] in chars:
        end -= 1

    return s[start:end+1]

print(custom_strip("  Hello, World!  "))  
print(custom_strip("xxHello, World!xx", "x"))  
print(custom_strip("  \t\nHello, World!  \t\n"))  
print(custom_strip("abcHello, World!abc", "abc"))  
