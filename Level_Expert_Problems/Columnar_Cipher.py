""" Columnar Cipher - Challenge
  Create a function that takes a string and a keyword.
  Return the ciphertext if the string is in plaintext
  (i.e. broken up into normal English words and punctuated),
  or the deciphered message if the string is in ciphertext.
  The resulting deciphered message will not have spaces.
"""


def encrypt(msg, keyword):
    # deformat message
    msg = msg.lower().replace(' ', '').replace('.', '')
    
    # split message into the respective columns
    splt_msg = [msg[i : i + len(keyword)] for i in range(0, len(msg), len(keyword))]

    # add null values to end of message if needed
    if len(splt_msg[-1]) != len(keyword):
        for _ in range(len(keyword) - len(splt_msg[-1])):
            splt_msg[-1] += 'x'
    
    # create alphabetically ordered values from keyword
    ord_num_lst = ['x' for _ in range(len(keyword))]  # add place holders to keep order
    buf_txt = [i for i in keyword]  # used to be able to remove letters
    for idx, let in [j for j in enumerate(sorted([i for i in keyword]))]:
        nidx = buf_txt.index(let)
        ord_num_lst[nidx] = idx
        buf_txt[nidx] = None  # remove letter to account for reoccuring letters (example: tomato)

    # combinding columns and forming new string
    encrypted_msg = ''
    count = 0  # used as index for each row
    for i in ord_num_lst:  # starts building of the message
        idx = ord_num_lst.index(count)
        for j in splt_msg:
            encrypted_msg += j[idx]
        count += 1

    return encrypted_msg


def decrypt(msg, keyword):
    # get alphabetically ordered values from keyword
    ord_num_lst = ['x' for _ in range(len(keyword))]
    buf_txt = [i for i in keyword]
    for idx, let in [j for j in enumerate(sorted([i for i in keyword]))]:
        nidx = buf_txt.index(let)
        ord_num_lst[nidx] = idx
        buf_txt[nidx] = None  # remove letter to account for reoccuring letters

    # number of rows needed
    num_rows = int(len(msg) / len(keyword))
    
    # go through each row and recreate original message
    org_msg = ''
    place_hldr = []
    for _ in ord_num_lst:
        place_hldr.append(msg[:num_rows])
        msg = msg[num_rows:]
    count = 0
    for _ in range(len(place_hldr[0])):
        for col in ord_num_lst:
            org_msg += place_hldr[col][count]
        count += 1

    return org_msg


def c_cipher(msg, keyword):
    # check for spaces in message to determine which method to use
    if len(msg.split()) != 1:
        print('Encrypted message:')
        return encrypt(msg, keyword)
    else:
        print('Decrypted message:')
        return decrypt(msg, keyword)

# Run solution
print(c_cipher('ebvloyjxeelownax', 'pancakes'))
