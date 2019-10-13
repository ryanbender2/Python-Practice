""" Bit Rotation
  Python offers some bit operations but not bit rotation. To complete that, create a function that takes three parameters:

  number: Integer, which in binary representaion should be rotated.
  rotations: Number of rotation steps that should be performed.
  l_or_r: Boolean value; True = rotation right, False = rotation left.
  Your function should return an integer as a result of its rotated binary representation.
"""


def bit_rotate(number, rotations, l_or_r):
    # convert number into into binary
    bin_num = bin(number)[2:]
    
    # location position to split number
    pos = len(bin_num) - rotations if l_or_r else rotations
    
    # flip bits at split position and convert back to base 10
    return int(bin_num[pos:] + bin_num[:pos], 2)


print(bit_rotate(58, 9, True))