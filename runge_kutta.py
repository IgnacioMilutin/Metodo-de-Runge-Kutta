import sympy as sp

#funcion que ejecuta la funcion dada a traves de la libreria sympy
def ejecucion_funcion(x_val,y_val):
    return funcion.evalf(subs={x: x_val, y: y_val})

#funcion del metodo
def runge_kutta(funcion,x_var,y_var,h,cantidad_x):
    i=1
    while x_var<=cantidad_x:
        k1=ejecucion_funcion(x_var,y_var)
        k2=ejecucion_funcion(x_var+(h/2),y_var+(h/2)*k1)
        k3=ejecucion_funcion(x_var+(h/2),y_var+(h/2)*k2)
        k4=ejecucion_funcion(x_var+h,y_var+h*k3)
        print('ITERACION '+str(i)+':')
        print('X='+str(x_var))
        print('Y='+str(y_var))
        if x_var==cantidad_x: break
        print('k1='+str(k1))
        print('k2='+str(k2))
        print('k3='+str(k3))
        print('k4='+str(k4))
        print('-------------------')
        y_var=y_var+h*(1/6*(k1+2*k2+2*k3+k4))
        x_var+=h
        i+=1

#conversion de la funcion de string a funcion matematica
funcion=input('Escriba la funcion: ')
x,y=sp.symbols('x y')
funcion = sp.sympify(funcion.replace("e", str(sp.E)))

#definicion de variables
x_var=float(input('Escriba la variable X: '))
y_var=float(input('Escriba la variable Y: '))
h=float(input('Escriba el tamaño del paso (h): '))
cantidad_x=float(input('Escriba hasta que valor de X quiere iterar (generalmente 4): '))

#ejecucion del metodo
runge_kutta(funcion,x_var,y_var,h,cantidad_x)
