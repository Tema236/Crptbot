import math

def n212(y,m,a,b):
    gamma = []
    otvet = []
    gammastr = ""
    otvetstr = ""
    n = len(y)

    for i in range(n):
        gamma.append((int(y[i]) - int(a[i])) % m)  # pribavlyaem k massivy elements

    for i in range(n):
        otvet.append((int(b[i]) + int(gamma[i])) % m)  # pribavlyaem k massivy elements

    for i in range(n):
        gammastr += str(gamma[i])
        otvetstr += str(otvet[i])

    #print('gamma = ', gamma)
    #print('otvet = ', otvet)
    #print('gamma = ', gammastr)
    #print('otvet = ', otvetstr)
    answer = str('Gamma = ') + str(gammastr) + str(' Otvet = ') + str(otvetstr)
    return answer

def fnok(a, b):
    def lcm(a, b):
        lcm.multiple = lcm.multiple + b
        if ((lcm.multiple % a == 0) and (lcm.multiple % b == 0)):
            return lcm.multiple;
        else:
            lcm(a, b)
        return lcm.multiple

    lcm.multiple = 0
    if (a > b):
        LCM = lcm(b, a)
    else:
        LCM = lcm(a, b)

    return LCM

def zd33(limbda, degf):
    n = 1
    summa = 0
    #limbda = int(input('Vvedite /| : '))
    #degf = int(input('Vvedite degf : '))
    numbers = []
    for i in range(degf + 1):
        numbers.append(i)

    while summa < limbda:
        for i in range(degf + 1):
            summa += math.factorial(n) / (math.factorial(numbers[i]) * math.factorial(n - numbers[i]))
            n += 1

    otvet = n + 1
    answer = str('otvet : ') + str('n>= ') + str(otvet)
    return answer

def n43(b, tay, n, m, t):
    tn = 2 ** n - 1
    tm = 2 ** m - 1
    n1 = 2 ** (n - 1)
    n0 = 2 ** (n - 1) - 1
    s = int(((b * n0 + tay * n1) * (t/tn)) % tm)
    nok = (s * tm) // math.gcd(s, tm)
    tbig = (tn * nok) / s
    otvet = str('otvet = ') + str(tbig)
    return otvet

def fi(n):
    f = n;
    if n%2 == 0:
        while n%2 == 0:
            n = n // 2;
        f = f // 2;
    i = 3
    while i*i <= n:
        if n%i == 0:
            while n%i == 0:
                n = n // i;
            f = f // i;
            f = f * (i-1);
        i = i + 2;
    if n > 1:
        f = f // n;
        f = f * (n-1);
    return f;
#print(n43(1,2,11,10,2047))

def egcd1(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)


# x = mulinv(b) mod n, (x * b) % n == 1
def mulinv(b, n):
    g, x, _ = egcd1(b, n)
    #print(g, x, _)
    if g == 1:
        return x % n
    else:
        abc = 'Не существует обратного элемента'
        return abc

from functools import reduce


def egcd(a, b):
    "" "Расширенный Евклид" ""
    if 0 == b:
        return 1, 0, a
    x, y, q = egcd(b, a % b)
    x, y = y, (x - a // b * y)
    return x, y, q


def chinese_remainder(pairs):
    "" "Китайская теорема об остатках" ""
    mod_list, remainder_list = [p[0] for p in pairs], [p[1] for p in pairs]
    mod_product = reduce(lambda x, y: x * y, mod_list)
    mi_list = [mod_product // x for x in mod_list]
    mi_inverse = [egcd(mi_list[i], mod_list[i])[0] for i in range(len(mi_list))]
    x = 0
    for i in range(len(remainder_list)):
        x += mi_list[i] * mi_inverse[i] * remainder_list[i]
        x %= mod_product
    return x

def primfacs(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       primfac.append(n)
   return primfac

def wz_pr_chisla(n):
    otv = []
    for i in range(1,n):
        if math.gcd(n, i) == 1:
            otv.append(i)
    return otv

def t_ferma(p,m):
    otv = 2**(p%(m-1)) % m
    return otv

def sl_el(a,p,m):
    otv = a**(p%fi(m)) % m
    return otv