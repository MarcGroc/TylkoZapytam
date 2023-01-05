# Title: 
- Why web-server rest-api frontend structure?

### Date:
- 2023-01-02

### Status:
 - Accepted

### Context and Problem Statement
- This is Saas project, which will allow users to share codding projects they made with other students.
- To achieve this we need frontend-server-rest-api structure

### Decision:
- We will be using web-server rest-api frontend structure. The structure of having a web server, a REST API, and a frontend is a common architecture for web-based systems because it allows for separation of concerns and modularization of the system.

### Reasons for the decision:

#### There are several reasons why we believe that a microservices architecture is the best choice for our system:

- Microservices allow us to build and deploy individual components of the system independently, which makes it easier to scale and maintain the system over time.

- Microservices encourage modular, reusable code, which can make it easier to build and deploy new features and functionality.

- Microservices allow us to use different technologies and programming languages for different components of the system, which can make it easier to find the right tool for the job.

- Microservices can improve the reliability and fault tolerance of the system, as each component can fail independently without bringing down the entire system.


### Consequences:

Using a microservices architecture will require us to put more effort into designing and building the system, as we will need to carefully consider how to divide the system into independent components and how to communicate between those components. We will also need to invest in infrastructure and tooling to support a distributed system. However, we believe that the benefits of using microservices will outweigh the additional effort required to implement this architecture.