import timeit
import string_reverse
s=string_reverse.reverse_slicing("ABç∂EF"*10)
print(s)
# def reverse_for_loop(s):
    # s1 = ''
    # for c in s:
        # s1 = c + s1  # appending chars in reverse order
    # return s1

# input_str = 'ABç∂EF'

# if __name__ == "__main__":
    # print('Reverse String using for loop =', reverse_for_loop(input_str))
