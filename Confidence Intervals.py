"""

Confidence Interval

"""

# Confidence Interval For Popullation Mean

# This works for all 3 cases just make sure you put the input correct

def CI_popmean():
    bla=int(input('Enter 1 for one sided or 2 for two sided C-I: '))
    if bla==1:
        x_bar=float(input('Enter x_bar: '))
        s=float(input('Enter pop or sample standard deviation: '))
        n=float(input('Enter sample size: '))
        Z=float(input('Enter t a,n-1 or Z a  value: '))
        lower_bound= round(x_bar-Z*s/(n**0.5),4)
        upper_bound= round(x_bar+Z*s/(n**0.5),4)
        print('The upper CI with lower bound is '+str(lower_bound)+ ' < m < inf\n'
        'The lower CI with upper bound is -inf< m < '+str(upper_bound))
    
    else:
        x_bar=float(input('Enter x_bar: '))
        s=float(input('Enter pop or sample standard deviation: '))
        n=float(input('Enter sample size: '))
        Z=float(input('Enter t a/2,n-1 or Z a/2 value: '))
        lower_bound= round(x_bar-Z*s/(n**0.5),4)
        upper_bound= round(x_bar+Z*s/(n**0.5),4)
        width=round(2*Z*s/(n**0.5),4)
        error=round(Z*s/(n**0.5),4)
        print('The two sided CI is ('+str(lower_bound)+' , '+str(upper_bound)+')\n'
        'The Error and Width are '+str(error)+ ' '+ str(width))

# Condfidence Interval for Population Variance

def CI_popvar():
    bla=int(input('Enter 1 for one sided or 2 for two sided C-I: '))
    if bla==1:
        bla2=int(input('Enter 1 for Upper CI and 2 for Lower CI: '))
        if bla2 == 1:
            n=float(input('Enter sample size: '))
            s=float(input('Enter sample standard deviation: '))
            Chi=float(input('Enter Chi Square a: '))
            lower_bound=round((n-1)*(s**2)/Chi,4)
            print('The Upper CI with lower bound is '+ str(lower_bound)+ ' < sigma < inf')
        else:
            n=float(input('Enter sample size: '))
            s=float(input('Enter sample standard deviation: '))
            Chi=float(input('Enter Chi Square 1-a: '))
            upper_bound=round((n-1)*(s**2)/Chi,4)
            print('The Lower CI with upper bound is 0 < sigma< '+ str(upper_bound))
    else:
        n=float(input('Enter sample size: '))
        s=float(input('Enter sample standard deviation: '))
        Chi=float(input('Enter Chi Square a/2: '))
        Chi2= float(input('Enter Chi Square 1-a/2'))
        lower_bound=round((n-1)*(s**2)/Chi,4)
        upper_bound=round((n-1)*(s**2)/Chi2,4)
        print('The two sided CI is ('+str(lower_bound)+' , '+str(upper_bound)+')')


# Confidence Interval for Population Propartion

def CI_popprob():
    bla= int(input('Enter 1 for sample size or 2 for CI: '))
    if bla==1:
        bla2=int(input('Enter 1 for no initial esitimate and 2 with initial esitmate: '))

        if bla2==1:
            z=float(input('Enter Z test value: '))
            w=float(input('Enter width: '))
            n=round((z**2)*(1/(w**2)-1),4)
            print('The sample size is '+str(n))

        else:
            z=float(input('Enter Z test value: '))
            w=float(input('Enter width: '))
            p=float(input('Enter p_hat: '))
            a=p*(1-p)
            n=round((z**2 + 2*a - w**2 + (4*a*(a - w**2) + w**2)**0.5)/(w**2),4)
            print('The same size is '+str(n))

    else:
        bla2=int(input('Enter 1 for one sided and 2 for two sided: '))

        if bla2==2:
            z=float(input('Enter Z a/2 value: '))
            p=float(input('Enter p_hat value: '))
            n=float(input('Enter n value: '))

            a=(z*(p*(1-p)/n+(z**2)/(4*n**2))**0.5)/(1+(z**2)/n)
            b=(p+(z**2)/(2*n))/(1+(z**2)/n)

            lower_bound=round(b-a,4)
            upper_bound=round(a+b,4)
            error=round(b,4)
            width=round(2*b,4)

            print('The two sided CI is ('+str(lower_bound)+' , '+ str(upper_bound)+')\n'
            'The Error and width are '+str(error)+' '+ str(width))

        else:
            z=float(input('Enter Z a/2 value: '))
            p=float(input('Enter p_hat value: '))
            n=float(input('Enter n value: '))

            a=((z)*(p*(1-p)/n+(z**2)/(4*n**2))**0.5)/(1+(z**2)/n)
            b=(p+(z**2)/(2*n))/(1+(z**2)/n)

            lower_bound=round(b-a,4)
            upper_bound=round(a+b,4)

            print('The upper bound is '+ str(upper_bound)+'\n'
            'The lower bound is '+ str(lower_bound))

CI_popvar()





        







