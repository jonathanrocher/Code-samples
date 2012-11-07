""" Demo scipy curve_fit
"""
from scipy.optimize import curve_fit
from scipy.stats import norm

from numpy import exp, sin, pi, linspace, abs

def function(x, a , b, f, phi):
    result = a * exp(-b * sin(f * x + phi))
    return result

# Create a noisy data set.
actual_params = [3, 2, 1, pi/4]
x = linspace(0,2*pi,25)
exact = function(x, *actual_params)
noisy = exact + 0.3*norm.rvs(size=len(x)) 
# Use curve_fit to estimate the function parameters from the noisy data.
initial_guess = [1,1,1,1]
estimated_params, err_est = curve_fit(function, x, noisy, p0=initial_guess) 
print "params", estimated_params
#array([3.1705, 1.9501, 1.0206, 0.7034])
# err_est is an estimate of the covariance matrix of the estimates
#  (i.e. how good of a fit is it)
print "Estimated covariance diagonal:", err_est.diagonal()
print "Real errors:", abs(actual_params-estimated_params)