# • la suma y la resta funcionan para 2 vectores de la misma forma,
# • la multiplicación (mul and rmul) funcionan para un vector y un escalar,
# • la división (truediv) funciona con un vector y un escalar,
# • la división (rtruediv) produce un error aritmético (esta prueba puede comentarse para las demás pruebas y descomentarse para mostrar esta)

from vector import Vector

# v1 = Vector([[3.], [0.]], (2, 1))
# v2 = Vector([[5.], ['a.']], (2, 1))
# v1.dot(v2)
# v1.T()

# v1 = Vector([[0.0], [1.0], [2.0], [3.0]]) 
# v2 = v1 * 5
# print(v2)

# v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
# print(v1.shape)
# print(v1.T())


v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = Vector([[0.0], [1.0], [2.0], [3.0]])

# v3 = v1 + v2
# print(v3.values)

v3  = v1 - v2
print(str(v3))