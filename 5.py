def triangle(a):
    b=0
    while a>0 or b<a:
        print(' '*(a-1), '*'*(b+1))
        a= a-1
        b= b+1

triangle(5)
