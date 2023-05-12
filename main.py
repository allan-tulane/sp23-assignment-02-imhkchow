"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y



def subquadratic_multiply(x, y):
    ### TODO
    return _subquadratic_multiply(x,y).decimal_val

def _subquadratic_multiply(x,y):
    xvec = x.binary_vec
    yvec = y.binary_vec
    xvec, yvec = pad(xvec, yvec)
    
    if x.decimal_val <=1 and y.decimal_val <=1:
        return BinaryNumber(x.decimal_val * y.decimal_val)
    
     #split left and right for recursive call 
    x_left, x_right = split_number(xvec)
    y_left, y_right = split_number(yvec)
    # multiply left sides
    left_product = _quadratic_multiply(x_left, y_left)
    # multiply right sides
    right_product = _quadratic_multiply(x_right, y_right)
    # xl and yr
    left_right_product = _quadratic_multiply(x_left, y_right)
    # vice versa^^^
    right_left_product = _quadratic_multiply(x_right, y_left)
    middle_term = BinaryNumber(left_right_product.decimal_val +
                               right_left_product.decimal_val)
    # 2^n/2 equation middle term
    middle_term = bit_shift(middle_term, len(xvec)//2)
    
    # 2^n (xL * yL)
    left_product = bit_shift(left_product, len(xvec))
    
    # O(n) addition
    return BinaryNumber(left_product.decimal_val +
                        middle_term.decimal_val +
                        right_product.decimal_val)
    
    
    pass
    ###

def quadratic_multiply(x,y): 
    return _quadratic_multiply(x,y).decimal_val

def _quadratic_multiply(x,y)
    xvec = x.binary_vec
    yvec = y.binary_vec
    xvec, yvec = pad(xvec, yvec)
    if x.decimal_val <= 1 and y.decimal_val <= 1:
        return BinaryNumber(x.decimal_val * y.decimal_val)
    #split left and right for recursive call 
    x_left, x_right = split_number(xvec)
    y_left, y_right = split_number(yvec)
    # multiply left sides
    left_product = _quadratic_multiply(x_left, y_left)
    # multiply right sides
    right_product = _quadratic_multiply(x_right, y_right)
    # xl and yr
    left_right_product = _quadratic_multiply(x_left, y_right)
    # vice versa^^^
    right_left_product = _quadratic_multiply(x_right, y_left)
    middle_term = BinaryNumber(left_right_product.decimal_val +
                               right_left_product.decimal_val)
    # 2^n/2 equation middle term
    middle_term = bit_shift(middle_term, len(xvec)//2)
    
    # 2^n (xL * yL)
    left_product = bit_shift(left_product, len(xvec))
    
    # O(n) addition
    return BinaryNumber(left_product.decimal_val +
                        middle_term.decimal_val +
                        right_product.decimal_val)
                        
## Feel free to add your own tests here.
def test_multiply():
    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(4)) == 3*4
    assert quadratic_multiply(BinaryNumber(5), BinaryNumber(6)) == 5*6

def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    result = f(x,y)
    return (time.time() - start)*1000

    
    

