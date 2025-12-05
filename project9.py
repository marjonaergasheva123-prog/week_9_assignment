def parse_tag(tag_string, required_labels):
    if not tag_string[-1]=='*':
        return 'Error:Read error'
    clean = tag_string[:-1]
    parts = clean.split("/")

    found_labels = []
    found_values = []
    for part in parts:
        if '#' not in part:
            return f"Error: Invalid format in part '{part}'"
        else:
         label, value = part.split("#", 1)
         found_labels.append(label)
         found_values.append(value)
         
    for req in required_labels:
        if req not in found_labels:
            return f"Error: Missing Labels:{req} "
    
    result = []
    for req in required_labels:
        index = found_labels.index(req)
        result.append(found_values[index])
    return result

scan1 = "SKU#TX-99/LOC#Row3/BATCH#B7*"
req1 = ["SKU", "LOC", "BATCH"]
print(parse_tag(scan1, req1))

# Test Case 2: Valid scan but missing batch info
scan2 = "SKU#RX-11/LOC#Row1*"
req2 = ["SKU", "LOC", "BATCH"]
print(parse_tag(scan2, req2))

# Test Case 3: Invalid format (missing asterisk)
scan3 = "SKU#ZZ-00/LOC#Dock"
req3 = ["SKU"]
print(parse_tag(scan3, req3))

# Test Case 4: Different order
scan4 = "EXP#2024/SKU#MILK/LOC#Fridge*"
req4 = ["SKU", "LOC", "EXP"]
print(parse_tag(scan4, req4))


