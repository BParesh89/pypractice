# Q2. Create a package name "car", containing sub-packages as "BMW", "Audi", "Nissan", each containing different modules
# representing the different models of cars where each module will provide the features and functionalities for those
# car models. For example, BMW package contains modules for car model X1, Z4, X7, I8, where each model will be having
# some features like car variants, price,color etc. Now in the end, create a file app.py in the root directory and
# invoke the method of the above created modules, to create an object of a car(any of your choice)
from car.bmw.x1 import X1
car1 = X1("Bmw X1", 500000)
car1.module_features()