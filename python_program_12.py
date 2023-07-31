def fib_function(term) :

    a,b,fibonacci_series=0,1,[]

    for x in range(term):
        fibonacci_series.append(a)
        a,b=a+b,a
        
    print("fibonacci series : ",end="")

    fibonacci_series=str(fibonacci_series)

    for x in range(1,len(fibonacci_series)-1):
        print(fibonacci_series[x],end="")

fib_function(int(input("Enter the term till which fibonacci series will be print : ")))

