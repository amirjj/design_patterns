### Most Popular Design Patterns 
to be used in projects, also popular in interviews


### Adapter
To write a new module to integrate two other incomatible code/ service instead of changing them. 

### Decorator
Adding new functionality to a method (or object) without changing the nature of the object (eg, changin it's code).
decorator pattern is not the same as usual python decorator.
decorator is callable, with function as input and output.


### Factory
Hiding complexity to inherent classes called Factory.
for example you write a shipment class hiding the fact that shipment perform with what kind of vehicle (Ship or Plane).
inhereting class will specify the type of vehicle and method of shipment.

### Observer
Observer pattern will be used when, changing and object is depending on updating
another object.
Most notification modules are in observer pattern scope.


### Proxy
proxy pattern use for access management limiting functionalities of an object.
it's possible that you find a decorator in a framework that uses Proxy design
pattern, meaning python decorator is not related to Decorator design pattern.

### Lazy loading
lazy loading is a Proxy pattern because you are changing the method of how to
access a class.
creating an object from a class exactly the time that is needed.

### Singleton
from any class you need to have only one object
suppose that you have a class which is going to connect to DB, connection to
DB need to be Singleton, it's wrong to have multiple un-necessary connection
other example would be SSH connections
for games, game instances should be Singleton

### State
if your program need to have a couple of states you need to switch between them.
