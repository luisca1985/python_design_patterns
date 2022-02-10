# Python Design Pattern

## Creational Design Pattern
Creational patterns provides essential information regarding the Class instantiation or the object instantiation.

Class Creational Pattern and the Object Creational pattern is the major categorization of the Creational Design Patterns. While class-creation patterns use inheritance effectively in the instantiation process, object-creation patterns use delegation effectively to get the job done.

### Factory Method
Factory Method is a Creational Design Pattern that allows an interface or a class to create an object, but lets subclasses decide which class or object to instantiate. Using the Factory method, we have the best ways to create an object. Here, objects are created without exposing the logic to the client, and for creating the new type of object, the client uses the same common interface.

#### References
- [Factory Method – Python Design Patterns](https://www.geeksforgeeks.org/factory-method-python-design-patterns/)

### Abstract Factory Method
Abstract Factory Method is a Creational Design pattern that allows you to produce the families of related objects without specifying their concrete classes. Using the abstract factory method, we have the easiest ways to produce a similar type of many objects.

It provides a way to encapsulate a group of individual factories. Basically, here we try to abstract the creation of the objects depending on the logic, business, platform choice, etc.

#### References
- [Abstract Factory Method – Python Design Patterns](https://www.geeksforgeeks.org/abstract-factory-method-python-design-patterns/)

### Builder Method
Builder Method is a Creation Design Pattern which aims to “Separate the construction of a complex object from its representation so that the same construction process can create different representations.” It allows you to construct complex objects step by step. Here using the same construction code, we can produce different types and representations of the object easily.

It is basically designed to provide flexibility to the solutions to various object creation problems in object-oriented programming.

#### References
- [Builder Method – Python Design Patterns](https://www.geeksforgeeks.org/builder-method-python-design-patterns/)

### Prototype Method
Prototype Method is a Creational Design Pattern which aims to reduce the number of classes used for an application. It allows you to copy existing objects independent of the concrete implementation of their classes. Generally, here the object is created by copying a prototypical instance during run-time.

It is highly recommended to use Prototype Method when the object creation is an expensive task in terms of time and usage of resources and already there exists a similar object. This method provides a way to copy the original object and then modify it according to our needs.

#### References
- [Prototype Method – Python Design Patterns](https://www.geeksforgeeks.org/prototype-method-python-design-patterns/)

### Singleton Method
Singleton Method is a type of Creational Design pattern and is one of the simplest design pattern available to us. It is a way to provide one and only one object of a particular type. It involves only one class to create methods and specify the objects. 

Singleton Design Pattern can be understood by a very simple example of Database connectivity. When each object creates a unique Database Connection to the Database, it will highly affect the cost and expenses of the project. So, it is always better to make a single connection rather than making extra irrelevant connections which can be easily done by Singleton Design Pattern.

#### References
- [Singleton Method – Python Design Patterns](https://www.geeksforgeeks.org/singleton-method-python-design-patterns/)

## Structural Design Patterns
Structural design patterns are about organizing different classes and objects to form larger structures and provide new functionality while keeping these structures flexible and efficient. Mostly they use Inheritance to compose all the interfaces. It also identifies the relationships which led to the simplification of the structure.

### Adapter Method
Adapter method is a Structural Design Pattern which helps us in making the incompatible objects adaptable to each other. The Adapter method is one of the easiest methods to understand because we have a lot of real-life examples that show the analogy with it. The main purpose of this method is to create a bridge between two incompatible interfaces. This method provides a different interface for a class. We can more easily understand the concept by thinking about the Cable Adapter that allows us to charge a phone somewhere that has outlets in different shapes.

Using this idea, we can integrate the classes that couldn’t be integrated due to interface incompatibility.

#### References
- [Adapter Method – Python Design Patterns](https://www.geeksforgeeks.org/adapter-method-python-design-patterns/)

### Bridge Method
Bridge method is a Structural Design Pattern which allows us to separate the Implementation Specific Abstractions and Implementation Independent Abstractions from each other and can be developed considering as the single entities.

Bridge Method is always considered as one of the best methods to organize the class hierarchy.

#### References
- [Bridge Method – Python Design Patterns](https://www.geeksforgeeks.org/bridge-method-python-design-patterns/)

### Composite Method
Composite Method is a Structural Design Pattern which describes a group of objects that is treated the same way as a single instance of the same type of the objects. The purpose of the Composite Method is to Compose objects into Tree type structures to represent the whole-partial hierarchies.

One of the main advantages of using the Composite Method is that first, it allows you to compose the objects into the Tree Structure and then work with these structures as an individual object or an entity.

#### References
- [Composite Method – Python Design Patterns](https://www.geeksforgeeks.org/composite-method-python-design-patterns/)

### Decorator Method
Decorator Method is a Structural Design Pattern which allows you to dynamically attach new behaviors to objects without changing their implementation by placing these objects inside the wrapper objects that contains the behaviors.

It is much easier to implement Decorator Method in Python because of its built-in feature. It is not equivalent to the Inheritance because the new feature is added only to that particular object, not to the entire subclass.

#### References
- [Decorator Method – Python Design Patterns](https://www.geeksforgeeks.org/decorator-method-python-design-patterns/)

### Facade Method

Facade Method is a Structural Design pattern that provides a simpler unified interface to a more complex system. The word Facade means the face of a building or particularly an outer lying interface of a complex system, consists of several sub-systems. It is an essential part Gang of Four design patterns. It provides an easier way to access methods of the underlying systems by providing a single entry point.

Here, we create a Facade layer that helps in communicating with subsystems easily to the clients.

#### References
- [Facade Method – Python Design Patterns](https://www.geeksforgeeks.org/facade-method-python-design-patterns/)

### Proxy Method
The Proxy method is Structural design pattern that allows you to provide the replacement for an another object. Here, we use different classes to represent the functionalities of another class. The most important part is that here we create an object having original object functionality to provide to the outer world.

The meaning of word Proxy is “in place of” or “on behalf of” that directly explains the Proxy Method.

Proxies are also called surrogates, handles, and wrappers. They are closely related in structure, but not purpose, to Adapters and Decorators.

#### References
- [Proxy Method – Python Design Patterns](https://www.geeksforgeeks.org/proxy-method-python-design-patterns/)


## References
- [Python Design Patterns](https://www.geeksforgeeks.org/python-design-patterns/)