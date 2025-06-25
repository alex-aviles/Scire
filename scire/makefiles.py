# make_test_files.py
test_data = "192.168.1.1\n192.168.1.2\ngoogle.com"

# UTF-8
with open("utf8_targets.txt", "w", encoding="utf-8") as f:
    f.write(test_data)

# UTF-16
with open("utf16_targets.txt", "w", encoding="utf-16") as f:
    f.write(test_data)

print("Test files created.")