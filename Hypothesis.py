"""

Hypothesis Testing

"""

### Hypothesis Testing for Population Mean

def HP_popmean():
    case=input(' Enter 1 for Ha: m > mo\n'
    'Enter 2 for Ha: m < mo\n'
    'Enter 3 for Ha: m != mo\n')

    if case=='1':
        err=input('Enter 1 for alpha or 2 for betta or 3 for sample size: ')
        if err=='1':
            x=float(input('Enter x_bar: '))
            m=float(input('Enter mo: '))
            s=float(input('Enter s or sigma: '))
            n=float(input('Enter n: '))
            z=float(input('Enter Za or ta,n-1: '))
            
            TS=round((x-m)/(s/(n**0.5)),4)
            RR='Z or t > '+str(z)

            print('Test Statistic is '+str(TS)+ ' The RR is '+RR)
        elif err=='2':
            mo=float(input('Enter mo: '))
            m=float(input("Enter m': "))
            s=float(input('Enter s or sigma: '))
            n=float(input('Enter n: '))
            z=float(input('Enter Za or ta,n-1: '))

            B=round((mo-m)/(s/(n**0.5))+z,4)

            print('phi('+str(B)+')')
        
        else:
            s=float(input('Enter s or sigma'))
            mo=float(input('Enter mo: '))
            m=float(input("Enter m': "))
            za=float(input('Enter Za or ta,n-1: '))
            zb=float(input('Enter Zb or tb,n-1: '))

            n=round((s*(za+zb)/(mo-m))**2,4)

            print('Sample size is '+str(n))
    
    elif case=='2':
        err=input('Enter 1 for alpha or 2 for betta or 3 for sample size: ')
        if err=='1':
            x=float(input('Enter x_bar: '))
            m=float(input('Enter mo: '))
            s=float(input('Enter s or sigma: '))
            n=float(input('Enter n: '))
            z=float(input('Enter Za or ta,n-1: '))
            
            TS=round((x-m)/(s/(n**0.5)),4)
            RR='Z or t < '+'-'+str(z)

            print('Test Statistic is '+str(TS)+ ' The RR is '+RR)
        elif err=='2':
            mo=float(input('Enter mo: '))
            m=float(input("Enter m': "))
            s=float(input('Enter s or sigma: '))
            n=float(input('Enter n: '))
            z=float(input('Enter Za or ta,n-1: '))

            B=round((mo-m)/(s/(n**0.5))-z,4)

            print('1 - phi('+str(B)+')')
        
        else:
            s=float(input('Enter s or sigma'))
            mo=float(input('Enter mo: '))
            m=float(input("Enter m': "))
            za=float(input('Enter Za or ta,n-1: '))
            zb=float(input('Enter Zb or tb,n-1: '))

            n=s*(za+zb)/(mo-m)
            n=round(n**2,4)


            print('Sample size is '+str(n))
    
    else:
        err=input('Enter 1 for alpha or 2 for betta or 3 for sample size: ')
        if err=='1':
            x=float(input('Enter x_bar: '))
            m=float(input('Enter mo: '))
            s=float(input('Enter s or sigma: '))
            n=float(input('Enter n: '))
            z=float(input('Enter Za/2 or ta/2,n-1: '))
            
            TS=round((x-m)/(s/(n**0.5)),4)
            RR='Z or t > '+str(z)+ ' and '+'Z or t < -'+str(z)

            print('Test Statistic is '+str(TS)+ ' The RR is '+RR)
        elif err=='2':
            mo=float(input('Enter mo: '))
            m=float(input("Enter m': "))
            s=float(input('Enter s or sigma: '))
            n=float(input('Enter n: '))
            z=float(input('Enter Za/2 or ta/2,n-1: '))

            B1=round((mo-m)/(s/(n**0.5))+z,4)
            B2=round((mo-m)/(s/(n**0.5))-z,4)

            print('phi('+str(B1)+') - phi('+str(B2)+')')
        
        else:
            s=float(input('Enter s or sigma'))
            mo=float(input('Enter mo: '))
            m=float(input("Enter m': "))
            za=float(input('Enter Za/2 or ta/2,n-1: '))
            zb=float(input('Enter Zb or tb,n-1: '))

            n=round((s*(za+zb)/(mo-m))**2,4)

            print('Sample size is '+str(n))


### Hypothesis Testinf for Population Proportion

def HP_poprob():
    case=input(' Enter 1 for Ha: p > po\n'
    'Enter 2 for Ha: p < po\n'
    'Enter 3 for Ha: p != po\n')

    if case=='1':
        err=input('Enter 1 for alpha or 2 for betta or 3 for sample size: ')
        if err=='1':
            p=float(input('Enter p_hat: '))
            po=float(input('Enter po: '))
            n=float(input('Enter n: '))
            z=float(input('Enter Za: '))

            a=po*(1-po)/n
            a=a**0.5
            TS=round((p-po)/a,4)
            RR='Z > '+str(z)

            print('Test Statistic is '+str(TS)+ ' The RR is '+RR)

        elif err=='2':
            p=float(input("Enter p': "))
            po=float(input('Enter po: '))
            n=float(input('Enter n: '))
            z=float(input('Enter Za: '))

            a=po*(1-po)/n
            a=a**0.5

            b=p*(1-p)/n
            b=b**0.5

            B=round((po-p+z*a)/b,4)
            print('phi('+str(B)+')')

        else:
            p=float(input("Enter p': "))
            po=float(input('Enter po: '))
            zb=float(input('Enter zb: '))
            za=float(input('Enter za: '))

            a=po*(1-po)
            a=a**0.5

            b=p*(1-p)
            b=b**0.5

            n=round(((za*a+zb*b)/(po-p))**2,4)
            print('Sample size is '+str(n))

    elif case=='2':
        err=input('Enter 1 for alpha or 2 for betta or 3 for sample size: ')
        if err=='1':
            p=float(input('Enter p_hat: '))
            po=float(input('Enter po: '))
            n=float(input('Enter n: '))
            z=float(input('Enter za: '))

            a=po*(1-po)/n
            a=a**0.5
            TS=round((p-po)/a,4)
            RR='Z < '+'-'+str(z)

            print('Test Statistic is '+str(TS)+ ' The RR is '+RR)

        elif err=='2':
            p=float(input("Enter p': "))
            po=float(input('Enter po: '))
            n=float(input('Enter n: '))
            z=float(input('Enter za: '))

            a=po*(1-po)/n
            a=a**0.5

            b=p*(1-p)/n
            b=b**0.5

            B=round((po-p-z*a)/b,4)
            print('1 - phi('+str(B)+')')

        else:
            p=float(input("Enter p': "))
            po=float(input('Enter po: '))
            zb=float(input('Enter zb: '))
            za=float(input('Enter za: '))

            a=po*(1-po)
            a=a**0.5

            b=p*(1-p)
            b=b**0.5

            n=round(((za*a+zb*b)/(po-p))**2,4)
            print('Sample size is '+str(n))

    else:
        err=input('Enter 1 for alpha or 2 for betta or 3 for sample size: ')
        if err=='1':
            p=float(input('Enter p_hat: '))
            po=float(input('Enter po: '))
            n=float(input('Enter n: '))
            z=float(input('Enter za: '))

            a=po*(1-po)/n
            a=a**0.5
            TS=round((p-po)/a,4)
            RR='Z > '+str(z)+ ' and '+'Z < -'+str(z)

            print('Test Statistic is '+str(TS)+ ' The RR is '+RR)

        elif err=='2':
            p=float(input("Enter p': "))
            po=float(input('Enter po: '))
            n=float(input('Enter n: '))
            z=float(input('Enter Za/2: '))

            a=po*(1-po)/n
            a=a**0.5

            b=p*(1-p)/n
            b=b**0.5
            B1=round((po-p+z*a)/b,4)
            B2=round((po-p-z*a)/b,4)
            print('phi('+str(B1)+') - phi('+str(B2)+')')

        else:
            p=float(input("Enter p': "))
            po=float(input('Enter po: '))
            zb=float(input('Enter zb: '))
            za=float(input('Enter za: '))

            a=po*(1-po)
            a=a**0.5

            b=p*(1-p)
            b=b**0.5

            n=round(((za*a+zb*b)/(po-p))**2,4)
            print('Sample size is '+str(n))

        


options= input('Enter 1 for population proportion\n'
'Enter 2 for population mean')

if options=='1':
    HP_poprob()

else:
    HP_popmean()
