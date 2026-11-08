# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

value_text = "87"
value = value_text.strip()
cleaned = float(value_text)


print(cleaned)
# we can't strip 'float'
# we have to strip it before we change it.