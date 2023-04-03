from scipy.stats import poisson

#PRACTICO 2 
#4 
# b)
poisson.pmf(1, (8/100)*50) + poisson.pmf(2, (8/100)*50) + poisson.pmf(0, (8/100)*50)

poisson.cdf(2, (8/100)*50)

# c)

1 - poisson.cdf(10, (8/100)*125)
#0.41696024980701485

#7) 
#a)
mu = 1/30 
poisson.pmf(0, mu*2.5)
#0.9200444146293233
poisson.pmf(0, mu*10)
#0.7165313105737893
poisson.pmf(0, mu*20)
#0.513417119032592

# 8)
# a)
mu = 1/30 
poisson.cdf(1, mu*5)
#0.9875620123723831
poisson.cdf(1, mu*10)
#0.9553750807650524
poisson.cdf(1, mu*20)
#0.8556951983876534
poisson.cdf(1, mu*30)
#0.7357588823428847