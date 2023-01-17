#!/usr/bin python3

def rk4(func, tk, _yk, _dt, **kwargs):
	"""
	single-step fourth-order numerical integration (RK4) method
	func: system of first order ODEs
	tk: current time step
	_yk: current state vector [y1, y2, y3, ...]
	_dt: discrete time step size
	**kwargs: additional parameters for ODE system
	returns: y evaluated at time k+1
	"""

	# evaluate derivative at several stages within time interval
	f1 = func(tk, _yk, **kwargs)
	f2 = func(tk + _dt / 2, _yk + (f1 * (_dt / 2)), **kwargs)
	f3 = func(tk + _dt / 2, _yk + (f2 * (_dt / 2)), **kwargs)
	f4 = func(tk + _dt, _yk + (f3 * _dt), **kwargs)

	# return an average of the derivative over tk, tk + dt
	return _yk + (_dt / 6) * (f1 + (2 * f2) + (2 * f3) + f4)
