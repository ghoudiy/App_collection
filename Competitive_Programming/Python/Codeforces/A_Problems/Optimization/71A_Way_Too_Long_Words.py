for _ in range(int(input())):
	s = input()
	print(f"{s[0]}{len(s[1:-1])}{s[-1]}" if len(s) > 10 else s)
	
# input
"""
4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis
"""

# output
"""
word
l10n
i18n
p43s
"""
