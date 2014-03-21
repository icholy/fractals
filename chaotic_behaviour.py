
def limit(it, n):
    count = 0
    for x in it:
        if count is n:
            break
        count += 1
        yield x

def z_generator(x):
    c = x
    while True:
        x = x*x + c
        yield x

def main():
    c = -1.5
    for x in limit(z_generator(c), 100):
        print x

if __name__ == '__main__':
    main()
    
  
