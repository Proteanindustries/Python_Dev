a = 'hello'

if (len(a) > 3):
    print(f'Too long {len(a)} elements')

if ((n := len(a)) >3):
    print(f'Too long {n} elements')
while ((n := len(a)) > 2):
    print(n)
    a = a[:-1]
