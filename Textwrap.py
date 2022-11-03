import textwrap

def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))

if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print(result)
    
    
##Samle Input 
  
    ABCDEFGHIJKLIMNOQRSTUVWXYZ
    4

##Sample Output 0

    ABCD
    EFGH
    IJKL
    IMNO
    QRST
    UVWX
    YZ