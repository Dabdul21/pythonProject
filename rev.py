#write a short recursive function that takes a character string s and outputs its reverse.
#for ex, the reverse of pots&pans would be snap&stop.

def reverse (s: str) -> str:
    n = len(s)
    if n == 1:
        return s
    else:
        return reverse(s[1:]) + s[-n]
print(reverse("abcd"))
