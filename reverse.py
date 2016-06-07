def reverse(s)
s=good
if len(s)<1:
return s
return reverse(s[1:])+s[0]
