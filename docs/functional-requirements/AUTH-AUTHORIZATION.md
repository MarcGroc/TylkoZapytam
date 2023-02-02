The API and front-end are on the same domain, e.g:
api.domain.net
www.domain.net

# Login
1.  Type in your login and password and send a request to the API
2. the API checks if there is a cookie (#authentication), but it is not there yet
3. the API checks in the database to see if the user with the given login and password hash[1] exists
3.1 If it does not exist -> 404
3.2 If the password is invalid -> 404[2]
3.3 If it exists then continue....
4. the API generates a token. It can use any method for this, e.g. https://stackoverflow.com/a/8856177/704894
5. the API saves the token and the associated user in the database. The session expiry time is also set.
6. the API sets a cookie with this token. Necessarily Domain=.domain.net, HttpOnly and SameSite=Lax. And Secure if you have https (you must have on production)
7. the API sends a response along with this cookie. From this point on, every request from www.domain.net to api.domain.net will contain this cookie.

# Authentication
1. the user makes any request, the cookie is automatically included.
2. the API checks if there is a cookie and a token in it.
3. the API checks if the token is in the database.
3.1 If it is, the API checks if the token is valid (has not expired)
3.1.1. If no -> 401
3.1.2. If yes -> the associated user is retrieved -> then the request can be served on this basis (#authorisation)
3.2 If not and the route in question requires a login -> 401

# Authorisation
1. determine if the user should have access here at all, etc.
1.1 If no -> 403
1.2 If yes -> handle request

*always hash passwords e.g. bcrypt*
 *04 even if such a login exists, this improves the security of the application, because you cannot use login to check if an account already exists*
