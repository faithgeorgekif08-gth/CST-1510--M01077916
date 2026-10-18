# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

record = {"label": "R-001", "value": 87.0, "limit": 100.0}

# 'status' was not included in the list
record ["status"] = "OK"
# we have to include it
print(record["status"])