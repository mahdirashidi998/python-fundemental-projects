prefixes = "JKLMNOPQ"
suffix = "ack"
for letter in prefixes:
    if letter=='O' :
        print('Oack')
    elif letter=='Q':
        print('Quack')
    else:
        print(letter + suffix)