# Title: 
- Why web-server rest-api frontend structure?

### Date:
- 2023-01-02

### Status:
- Accepted
- 
### Context and Problem Statement
- Our team is building a new software application that will need to serve a large number of users over the web. We are considering several different architectures for the application, including a monolithic architecture and a frontend-server-API architecture.


### Decision:
- We will be using web-server rest-api frontend structure. The structure of having a web server, a REST API, and a frontend is a common architecture for web-based systems because it allows for separation of concerns and modularization of the system.
### Reasons for the decision:

There are several reasons why we believe that a frontend-server-API architecture is the best choice for our application:

A frontend-server-API architecture allows us to build and deploy the frontend and backend components of the application independently, which makes it easier to scale and maintain the application over time.

A frontend-server-API architecture allows us to use different technologies and programming languages for the frontend and backend components of the application, which can make it easier to find the right tool for the job.

A frontend-server-API architecture can improve the security of the application, as the frontend and backend components can be isolated from each other and the API can be used to enforce security controls.

A frontend-server-API architecture can improve the performance of the application, as the frontend and backend components can be optimized separately and the API can be used to minimize the amount of data transferred between the two components.

### Consequences:

- Using a frontend-server-API architecture will require us to put more effort into designing and building the application, as we will need to carefully consider how to divide the application into frontend and backend components and how to communicate between those components via an API. We will also need to invest in infrastructure and tooling to support this architecture. However, we believe that the benefits of using a frontend-server-API architecture will outweigh the additional effort required to implement this architecture.
