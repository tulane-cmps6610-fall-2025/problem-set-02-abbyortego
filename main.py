"""
CMPS 6610  Problem Set 2
See problemset-02.pdf for details.
"""
import time
import tabulate

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

# some useful utility functions to manipulate bit vectors
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y
    
def quadratic_multiply(x, y):
    # print("x: ", x, "\ty: ", y)

    # base case: single digit >>> if one is 0 then 0, if both are 1 then 1
    if x.decimal_val == 0 or y.decimal_val == 0:
        return 0
    if x.decimal_val == 1 and y.decimal_val == 1:
        return 1
    #

    x.binary_vec, y.binary_vec = pad(x.binary_vec, y.binary_vec)    # pad
    (x_l, x_r), (y_l, y_r) = split_number(x.binary_vec), split_number(y.binary_vec)     # split in two

    # recursion 
    rec_mult_1 = quadratic_multiply(x_l, y_l)
    rec_mult_2 = quadratic_multiply(x_l, y_r)
    rec_mult_3 = quadratic_multiply(x_r, y_l)
    rec_mult_4 = quadratic_multiply(x_r, y_r)
    # print(rec_mult_1, rec_mult_2, rec_mult_3, rec_mult_4)

    return bit_shift(BinaryNumber(rec_mult_1), len(x.binary_vec)).decimal_val + bit_shift(BinaryNumber(rec_mult_2 + rec_mult_3), len(x.binary_vec)//2).decimal_val + rec_mult_4
# quadratic_multiply
print(f"Quadratic Multiply of {BinaryNumber(9)} and {BinaryNumber(13)} is", quadratic_multiply(BinaryNumber(9), BinaryNumber(13)))

def subquadratic_multiply(x, y):
    # print("x: ", x, "\ty: ", y)

    # base case: single digit >>> if one is 0 then 0, if both are 1 then 1
    if x.decimal_val == 0 or y.decimal_val == 0:
        return 0
    if x.decimal_val == 1 and y.decimal_val == 1:
        return 1
    #

    x.binary_vec, y.binary_vec = pad(x.binary_vec, y.binary_vec)    # pad
    (x_l, x_r), (y_l, y_r) = split_number(x.binary_vec), split_number(y.binary_vec)     # split in two

    # recursion 
    rec_mult_1 = subquadratic_multiply(x_l, y_l)
    rec_mult_2 = subquadratic_multiply(BinaryNumber(x_l.decimal_val + x_r.decimal_val), BinaryNumber(y_l.decimal_val + y_r.decimal_val))
    rec_mult_3 = subquadratic_multiply(x_r, y_r)
    # print(rec_mult_1, rec_mult_2, rec_mult_3)

    return bit_shift(BinaryNumber(rec_mult_1), len(x.binary_vec)).decimal_val + bit_shift(BinaryNumber(rec_mult_2-rec_mult_1-rec_mult_3), len(x.binary_vec)//2).decimal_val + rec_mult_3
# subquadratic_multiply
print(f"Subquadratic Multiply of {BinaryNumber(9)} and {BinaryNumber(13)} is", subquadratic_multiply(BinaryNumber(9), BinaryNumber(13)))

## Feel free to add your own tests here.
def test_multiply():
    assert binary2int(quadratic_multiply(BinaryNumber(2), BinaryNumber(2))) == 2*2

# some timing functions here that will make comparisons easy    
def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    f(x,y)
    return (time.time() - start)*1000

def print_results(results):
    print("\n")
    print(
        tabulate.tabulate(
            results,
            headers=['n', 'quadratic', 'subquadratic'],
            floatfmt=".3f",
            tablefmt="github"))

def compare_multiply():
    res = []
    for n in [10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]:
        qtime = time_multiply(BinaryNumber(n), BinaryNumber(n), quadratic_multiply)
        subqtime = time_multiply(BinaryNumber(n), BinaryNumber(n), subquadratic_multiply)        
        res.append((n, qtime, subqtime))
    print_results(res)
compare_multiply()
