"""
file     rstats.py
desc     renaming of Python Scipy functions to match with R.
author   Dr. Ernesto P. Adorio
         UPDEPP at Clark Field
         Pampanga, the Philippines
email    ernesto.adorio@gmail.com
version  mar 29, 2009 initial release. (basic probability distributions)
"""
 
import scipy
import scipy.stats as stat
 
t     = scipy.transpose     # transpose of a matrix.
mean  = stat.mean
var   = stat.var
sd    = stat.std
 
dnorm = stat.norm.pdf
pnorm = stat.norm.cdf
qnorm = stat.norm.ppf
rnorm = stat.norm.rvs
 
dt = stat.t.pdf
pt = stat.t.cdf
qt = stat.t.ppf
rt = stat.t.rvs
 
df = stat.f.pdf
pf = stat.f.cdf
qf = stat.f.ppf
rf = stat.f.rvs
 
dchisq = stat.chi2.pdf
pchisq = stat.chi2.cdf
qchisq = stat.chi2.ppf
rchisq = stat.chi2.rvs
 
# added mar 29, 2009 8:40
dunif = stat.uniform.pdf
punif = stat.uniform.cdf
qunif = stat.uniform.ppf
runif = stat.uniform.rvs
 
 
def Test():
  X = range(1,10)
  print X
  print mean(X)
  print sd(X)
  print var(X)
 
if __name__ == "__main__":
  Test()
