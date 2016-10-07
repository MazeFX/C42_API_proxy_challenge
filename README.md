# C42_API_proxy_challenge
Repository for the C42 code challenge to create a proxy for the C42 REST API.

In this assignment I'm asked to create a GET endpoint /events-with-subscriptions/ that combines two separate calls towards the C42 API into one response that contains the event title and the first names of its attendees.

### Assignment outlining
First things first, read the assigment, read through the API docs to get a basic understanding of the workings of the API and identify parts of the assigment where my current knowledge is lacking and get additional information through docs or inquiry.

So far as based on my current experience I don't see a reason to go outside the standard libraries of Python and Django. I need the json module from Python and need a correct module from Django to return a json object to the GET request (never done this before). Caching of the json object can probably be done with *django.core.cache* but I'm not sure. Only used caching for static files so far so this will possibly be a 'Aha!' moment for me.

To keep things reusable I'm going to make an django app for just returning the json object based on the request. I want to build a view for displaying the request just so that I can get the MVC structure right. The view is not part of the app since it is likely that the proxy will be used by multiple webapps.

When during development the outlining changes, things will be noted here.

And now the first step: Write a test, obey the testing goat!

05-10-2016: For offline testing of the request towards the C42 REST API I will use the *unittest.mock* module. I have no experience yet with this testing module and trying to find a way to wrap my head around this Magicmock object.
Found some examples but there is not really much that I can find that gives a good handle for testing external requests.

### Personal thoughts
I am very excited about doing this challenge. It's my first piece of coding based on a 'real' type of assigment. I'm already having a sence of drive to accomplish the challenge. I have a few concerns though, will my code quality be good enough? Will it matter that things will take a bit longer to accomplish since I don't have that much of spare time.
Will my code work in the end? I had my fair share of problems with working in different environments already and since my windows laptop desided to die on me only 2 weeks ago I'm having trouble setting up a new environment on my old desktop pc at such short notice. Also will it work if someone else tries to use it?

Because of my current personal situation I'm afraid for needing to much time to complete this challenge. On a normal working day I have about 1 hour of time to spend on this challenge if all goes well and I already spent 2 days migrating my development environment to my older 32bit desktop. There is no time frame provided with the challenge so I'm setting one for myself just to keep the pressure on.
I have until next friday (7-10-2016) to work on this challenge before turning in the code I have. Until that time it is important for myself that I keep things nice and tidy and don't take shortcuts just to make the deadline.

Just finished building the tests for Babelfish, I have doubts that tests are adequate. They test the functions and they all pass but I'm uncertain if the test make the right assertions.

## Awesome! Unit testing completed
07-10-2016: I'm thrilled about writing code for this challenge, so far I have accomplished 13 passing unit tests!
I'm still got some time for this is the last evening and I really want to get the proxy deployed. The cherry on the cake, just to spoil myself.
