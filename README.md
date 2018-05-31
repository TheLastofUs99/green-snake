# maketrans
این کد برای تعریف یک مترجم استفاده میشود
به طور مثال کد زیر حروف انگلیسی را معکوس میکند 
table=str.maketrans("abcdefghijklmnopqrstuvwxyz","zyxwvutsrqponmllkjihgfedcba")
raw=input()
raw.translate(table)
result=raw.translate(table)
print(result)
یعنی اگر کاربر حرف a را وارد کند
خروجی z است
یا اگر c را وارد کند
خروجی x است
