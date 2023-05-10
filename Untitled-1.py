string = "001234500"
unpadded_string = string.rstrip('0')  # '0000012345' -> '12345'
print(unpadded_string)