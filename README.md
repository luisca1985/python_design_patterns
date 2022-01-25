# Python Design Pattern
## Factory Method
Factory Method is a Creational Design Pattern that allows an interface or a class to create an object, but lets subclasses decide which class or object to instantiate. Using the Factory method, we have the best ways to create an object. Here, objects are created without exposing the logic to the client, and for creating the new type of object, the client uses the same common interface.

## Abstract Factory Method
Abstract Factory Method is a Creational Design pattern that allows you to produce the families of related objects without specifying their concrete classes. Using the abstract factory method, we have the easiest ways to produce a similar type of many objects.

It provides a way to encapsulate a group of individual factories. Basically, here we try to abstract the creation of the objects depending on the logic, business, platform choice, etc.

## Builder Method
Builder Method is a Creation Design Pattern which aims to “Separate the construction of a complex object from its representation so that the same construction process can create different representations.” It allows you to construct complex objects step by step. Here using the same construction code, we can produce different types and representations of the object easily.

It is basically designed to provide flexibility to the solutions to various object creation problems in object-oriented programming.

## Prototype Method
Prototype Method is a Creational Design Pattern which aims to reduce the number of classes used for an application. It allows you to copy existing objects independent of the concrete implementation of their classes. Generally, here the object is created by copying a prototypical instance during run-time.

It is highly recommended to use Prototype Method when the object creation is an expensive task in terms of time and usage of resources and already there exists a similar object. This method provides a way to copy the original object and then modify it according to our needs.

## Singleton Method
Singleton Method is a type of Creational Design pattern and is one of the simplest design pattern available to us. It is a way to provide one and only one object of a particular type. It involves only one class to create methods and specify the objects. 

Singleton Design Pattern can be understood by a very simple example of Database connectivity. When each object creates a unique Database Connection to the Database, it will highly affect the cost and expenses of the project. So, it is always better to make a single connection rather than making extra irrelevant connections which can be easily done by Singleton Design Pattern.

## References
- [Python Design Patterns](https://www.geeksforgeeks.org/python-design-patterns/)