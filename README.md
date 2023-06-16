# API Notes
## What are APIs?

APIs (Application Programming Interfaces) are a set of rules and protocols that allow different software applications to communicate and interact with each other.
APIs define the methods and data formats that applications can use to request and exchange information, services, or functionality.

## How are APIs used and why are they popular?

* Used to enable communication and integration between different software systems, allowing them to share data and functionality.
* Provide a standardized and structured way for applications to interact, reducing the complexity and effort required for integration.
* They are popular because they enable developers to leverage existing services and functionalities without having to build everything from scratch.
* Promote modularity, re-usability, and collaboration by allowing developers to build on top of existing APIs and create new applications.

## What is a REST API? What makes an API RESTful?

REST (Representational State Transfer) is an architectural style for designing networked applications.

A REST API is an API that adheres to the principles and constraints of the REST architectural style.

To be RESTful, an API should:
* Use standard HTTP methods (GET, POST, PUT, PATCH, DELETE) to perform operations on resources.
* Follow a stateless client-server communication model.
* Have a uniform interface with resource-based URLs and consistent data representations (e.g., JSON or XML).
* Support caching and allow for scalability and performance optimization.

## What is HTTP?

* HTTP (Hypertext Transfer Protocol) is a protocol used for communication on the web.
* It defines the format and semantics of messages exchanged between web browsers (clients) and web servers.
* HTTP is a request-response protocol, where clients send requests to servers, and servers respond with the requested data or status information.

## HTTP vs. HTTPS

* HTTP stands for Hypertext Transfer Protocol.
* HTTPS stands for Hypertext Transfer Protocol Secure.
* HTTPS is a secure version of HTTP that encrypts the communication between the client and server using SSL/TLS protocols.
* HTTPS is commonly used for secure transactions, such as online banking, e-commerce, and sensitive data transfers.

* ## The 5 HTTP Verbs and their functions

    GET: Retrieves a representation of a resource without modifying it.
    POST: Submits data to be processed or stored by the server.
    PUT: Replaces or updates an existing resource with the provided data.
    PATCH: Partially updates a resource with the provided data.
    DELETE: Deletes a specified resource.

## Statelessness

Statelessness refers to the design principle in which each HTTP request from a client to a server is independent and does not rely on past interactions.
In a stateless system, the server does not store client session data, and each request must contain all the necessary information for the server to process it.
Stateless APIs are easier to scale, as there is no need to manage and synchronize session state across multiple servers.

## Caching

Caching is the process of storing copies of frequently accessed data in a cache to improve performance and reduce the load on the server.
In the context of APIs, caching involves storing API responses on the client-side or in intermediate servers (e.g., proxy servers or content delivery networks).
Caching can reduce the number of requests sent to the server and improve the responsiveness of applications.

