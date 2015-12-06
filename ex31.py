# /usr/bin/python

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print '+ - - - -',

def print_post():
    print '|        ',

def print_beams():
    do_twice(print_beam)
    print '+'

def print_posts():
    do_twice(print_post)
    print '|'

def print_row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_twice(print_row)
    print_beams()
    
def print_4beams():
    do_four(print_beam)
    print '+'

def print_4posts():
    do_four(print_post)
    print '|'

def print_4row():
    print_4beams()
    do_four(print_4posts)

def print_4grid():
    do_four(print_4row)
    print_4beams()
print_grid()    
print_4grid()