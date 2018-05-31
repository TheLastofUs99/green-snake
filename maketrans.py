table=str.maketrans("abcdefghijklmnopqrstuvwxyz","zyxwvutsrqponmllkjihgfedcba")
raw=input()
raw.translate(table)
result=raw.translate(table)
print(result)

