### Conceptual Exercise
Answer the following questions below:

- What are important differences between Python and JavaScript?

  * Python is strongly type vs JS is weakly typed
  * Unlike JS, Python does not run in a browser
  * They are no variable declaration keywords in Python
  * No unrebindables in Python unlike in JS
  * Indentation in Python vs brackets in JS
  * There is no instance inheritance in Python
  * Passing incorrect number of arguments will cause an error in Python
  * Python has mutable and immutable data types, whereas JS does not
- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you 
  can try to get a missing key (like "c") *without* your programming 
  crashing.
   * We can prevent KeyError in most cases by using the get()
   * Also, we could try-except block

- What is a unit test?
  * Tests one function or method

- What is an integration test?
  * Tests integration between components and the interactions between
  different parts of the system

- What is the role of web application framework, like Flask?
  * Its purpose is similar as that of the library. Flask is much more definite 
  in terms of how it handles web requests. Its function is to facilitate 
  requests and responses on a server, allow for dynamic HTML production, manage 
  form submissions, user authentication, connection and interaction with 
  databases. 

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query params (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  * Query params is more often used if coming from form, as it provides more 
  info about the page. Query params allow to get details or filter the 
  requested info. 
  * URL params used to get a specific resource. 

- How do you collect data from a URL placeholder parameter using Flask?
  * The URL parameters are available in request.args

- How do you collect data from the query string using Flask?
  * We can do this by using request.query_string

- How do you collect data from the body of the request using Flask?
  * It can be done by using request.data

- What is a cookie and what kinds of things are they commonly used for?
  * Cookies are small pieces of information that a web server stores on a 
  computer. That info is a text. It can be a user Id or a session Id, etc.
  When user requests webpage, a cookie is being sent back to server with the 
  info that was stored on it. 

- What is the session object in Flask?
  * In the Flask, a session object is used to track the session data.  
  Session data is a dictionary object that contains a key-value pair of the 
  session variables and their associated values.

- What does Flask's `jsonify()` do?
  * It serializes the data or translates data structure into format 
  that can be stored or transmitted.

- What was the hardest part of this past week for you?
  * I am struggling to digest enormous amount of new commands and functions.
  Although, concepts are quite clear and well delivered, it is applied skill
  area that is the most problematic for me.

  What was the most interesting?
  * I was able to learn many new details about how web and internet works,
  as well as, new tools and techniques to add to my skill set. 
