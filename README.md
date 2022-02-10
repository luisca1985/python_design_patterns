# Python Design Pattern

## Indice
- [Creational Design Pattern](#creational-design-pattern)
    - [Factory Method](#factory-method)
    - [Abstract Factory Method](#abstract-factory-method)
    - [Builder Method](#builder-method)
    - [Prototype Method](#prototype-method)
    - [Singleton Method](#singleton-method)
- [Structural Design Patterns](#structural-design-patterns)
    - [Adapter Method](#adapter-method)
    - [Bridge Method](#bridge-method)
    - [Composite Method](#composite-method)
    - [Decorator Method](#decorator-method)
    - [Facade Method](#facade-method)
    - [Proxy Method](#proxy-method)

## Creational Design Pattern
Los patrones creacionales proporcionan información esencial sobre la creación de instancias de clase o la creación de instancias de objetos.

El patrón creacional de clases y el patrón creacional de objetos es la categorización principal de los patrones de diseño creacionales.

Mientras que los patrones creacionales de clases usan la herencia de manera efectiva en el proceso de creación de instancias, los patrones creacionales de objetos usan la delegación de manera efectiva para realizar el trabajo.

### Factory Method
Factory Method es un patrón de diseño creacional que permite que una interfaz o una clase creen un objeto, pero permite que las subclases decidan qué clase u objeto instanciar. 

Usando el Factory Method, tenemos las mejores formas de crear un objeto. Aquí, los objetos se crean sin exponer la lógica al cliente y, para crear el nuevo tipo de objeto, el cliente utiliza la misma interfaz común.

#### References
- [Factory Method – Python Design Patterns](https://www.geeksforgeeks.org/factory-method-python-design-patterns/)

### Abstract Factory Method
Abstract Factory Method es un patrón de Diseño Creacional que permite producir las familias de objetos relacionados sin especificar sus clases concretas. 

Usando el Abstract Factory Method, tenemos la forma más fácil de producir un tipo similar de muchos objetos.

Proporciona una forma de encapsular un grupo de fábricas individuales. Básicamente, aquí tratamos de abstraer la creación de los objetos según la lógica, el negocio, la elección de la plataforma, etc.

#### References
- [Abstract Factory Method – Python Design Patterns](https://www.geeksforgeeks.org/abstract-factory-method-python-design-patterns/)

### Builder Method
Builder Method es un patrón de diseño creacional que tiene como objetivo "separar la construcción de un objeto complejo de su representación para que el mismo proceso de construcción pueda crear diferentes representaciones". 

Permite construir objetos complejos paso a paso. Aquí, usando el mismo código de construcción, podemos producir fácilmente diferentes tipos y representaciones del objeto.

Básicamente está diseñado para proporcionar flexibilidad a las soluciones a varios problemas de creación de objetos en la programación orientada a objetos.

#### References
- [Builder Method – Python Design Patterns](https://www.geeksforgeeks.org/builder-method-python-design-patterns/)

### Prototype Method
Prototype Method is a Creational Design Pattern which aims to reduce the number of classes used for an application. It allows you to copy existing objects independent of the concrete implementation of their classes. Generally, here the object is created by copying a prototypical instance during run-time.

It is highly recommended to use Prototype Method when the object creation is an expensive task in terms of time and usage of resources and already there exists a similar object. This method provides a way to copy the original object and then modify it according to our needs.

Prototype Method es un patrón de diseño creacional que tiene como objetivo reducir el número de clases utilizadas para una aplicación. Le permite copiar objetos existentes independientemente de la implementación concreta de sus clases. Generalmente, aquí el objeto se crea copiando una instancia prototípica durante el tiempo de ejecución.

Se recomienda utilizar el Prototype Method cuando la creación del objeto es una tarea costosa en términos de tiempo y uso de recursos y ya existe un objeto similar. Este método proporciona una forma de copiar el objeto original y luego modificarlo según nuestras necesidades.

#### References
- [Prototype Method – Python Design Patterns](https://www.geeksforgeeks.org/prototype-method-python-design-patterns/)

### Singleton Method
El Singleton Method es un tipo de patrón de Diseño Creacional y es uno de los patrones de diseño más simples disponibles para nosotros. Es una forma de proporcionar uno y solo un objeto de un tipo particular. Se trata de una sola clase para crear métodos y especificar los objetos.

El patrón de diseño Singleton se puede entender con un ejemplo muy simple de conectividad de base de datos. Cuando cada objeto crea una conexión de base de datos única a la base de datos, afectará en gran medida el costo y los gastos del proyecto. Por lo tanto, siempre es mejor hacer una sola conexión en lugar de hacer conexiones adicionales irrelevantes, lo que se puede hacer fácilmente con Singleton Design Pattern.

#### References
- [Singleton Method – Python Design Patterns](https://www.geeksforgeeks.org/singleton-method-python-design-patterns/)

## Structural Design Patterns
Los Structural design patterns consisten en organizar diferentes clases y objetos para formar estructuras más grandes y brindar nuevas funcionalidades, manteniendo estas estructuras flexibles y eficientes. En su mayoría, usan Herencia para componer todas las interfaces. 

También identifica las relaciones que llevaron a la simplificación de la estructura.

### Adapter Method
Adapter method is a Structural Design Pattern which helps us in making the incompatible objects adaptable to each other. The Adapter method is one of the easiest methods to understand because we have a lot of real-life examples that show the analogy with it. The main purpose of this method is to create a bridge between two incompatible interfaces. This method provides a different interface for a class. We can more easily understand the concept by thinking about the Cable Adapter that allows us to charge a phone somewhere that has outlets in different shapes.

Using this idea, we can integrate the classes that couldn’t be integrated due to interface incompatibility.

El Adapter Method es un patrón de diseño estructural que nos ayuda a hacer que los objetos incompatibles se adapten entre sí. El método Adapter es uno de los métodos más fáciles de entender porque tenemos muchos ejemplos de la vida real que muestran la analogía con él. El objetivo principal de este método es crear un puente entre dos interfaces incompatibles. 

Este método proporciona una interfaz diferente para una clase. Podemos entender más fácilmente el concepto si pensamos en el Cable Adaptador que nos permite cargar un teléfono en algún lugar que tenga enchufes de diferentes formas.

Usando esta idea, podemos integrar las clases que no pudieron integrarse debido a la incompatibilidad de la interfaz.

#### References
- [Adapter Method – Python Design Patterns](https://www.geeksforgeeks.org/adapter-method-python-design-patterns/)

### Bridge Method
El Bridge Method es un patrón de diseño estructural que nos permite separar las abstracciones específicas de la implementación y las abstracciones independientes de la implementación entre sí y se pueden desarrollar considerando como entidades únicas.

Bridge Method siempre se considera como uno de los mejores métodos para organizar la jerarquía de clases.

#### References
- [Bridge Method – Python Design Patterns](https://www.geeksforgeeks.org/bridge-method-python-design-patterns/)

### Composite Method
El Composite Method es un patrón de diseño estructural que describe un grupo de objetos que se tratan de la misma manera que una sola instancia del mismo tipo de objetos. El propósito del método compuesto es componer objetos en estructuras de tipo árbol para representar las jerarquías total-parcial.

Una de las principales ventajas de usar el Composite Method es que, en primer lugar, le permite componer los objetos en la estructura de árbol y luego trabajar con estas estructuras como un objeto individual o una entidad.

#### References
- [Composite Method – Python Design Patterns](https://www.geeksforgeeks.org/composite-method-python-design-patterns/)

### Decorator Method
El Decorator Method es un patrón de diseño estructural que le permite adjuntar dinámicamente nuevos comportamientos a los objetos sin cambiar su implementación al colocar estos objetos dentro de los objetos de envoltura que contienen los comportamientos.

Es mucho más fácil implementar el Decorator Method en Python debido a su función integrada. No es equivalente a Herencia porque la nueva característica se agrega solo a ese objeto en particular, no a toda la subclase.

#### References
- [Decorator Method – Python Design Patterns](https://www.geeksforgeeks.org/decorator-method-python-design-patterns/)

### Facade Method

Facade Method is a Structural Design pattern that provides a simpler unified interface to a more complex system. The word Facade means the face of a building or particularly an outer lying interface of a complex system, consists of several sub-systems. It is an essential part Gang of Four design patterns. It provides an easier way to access methods of the underlying systems by providing a single entry point.

Here, we create a Facade layer that helps in communicating with subsystems easily to the clients.

El Facade Method es un patrón de diseño estructural que proporciona una interfaz unificada más simple para un sistema más complejo. La palabra Fachada significa la cara de un edificio o, en particular, una interfaz exterior de un sistema complejo, que consta de varios subsistemas. Es una parte esencial de los patrones de diseño de Gang of Four. 

Proporciona una forma más fácil de acceder a los métodos de los sistemas subyacentes al proporcionar un único punto de entrada.

Aquí, creamos una capa de fachada que ayuda a comunicarse fácilmente con los subsistemas para los clientes.

#### References
- [Facade Method – Python Design Patterns](https://www.geeksforgeeks.org/facade-method-python-design-patterns/)

### Proxy Method
El Proxy Method es un patrón de diseño estructural que le permite proporcionar el reemplazo de otro objeto. 

Se utiliza diferentes clases para representar las funcionalidades de otra clase. La parte más importante es que aquí creamos un objeto que tiene una funcionalidad de objeto original para proporcionar al mundo exterior.

El significado de la palabra Proxy es "en lugar de" o "en nombre de" que explica directamente el Método Proxy.

Los proxies también se denominan sustitutos, identificadores y envoltorios. Están estrechamente relacionados en estructura, pero no en propósito, con los adaptadores y decoradores.

#### References
- [Proxy Method – Python Design Patterns](https://www.geeksforgeeks.org/proxy-method-python-design-patterns/)


## References
- [Python Design Patterns](https://www.geeksforgeeks.org/python-design-patterns/)