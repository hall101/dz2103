def itc_revnbr(num):
    a = num % 10
    b = (num % 100) // 10
    c = num // 100
    return(a + b + c)
    
