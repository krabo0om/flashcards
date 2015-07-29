# flashcards
a simple client/server for creating and learning with flashcards

the server (found under source) handles simple **push** and **get** requests made by the client. one can get the api from a **get** on the root (i.e http://localhost:8000/).

1. **get** a card with "/nxtc" (next card)
  * the response (as json) contains the question, an answer, a hint and an id
2. do your learning thing and decide how good it was with the following *level*s
  * 0 = not even seen before ... no idea
  * 1 = barely correct
  * ...
  * 5 = knew that before i was born
3. **post** on path "/learned" with a json answer ("id" and "*level*")
4. the server will return the new level
5. **get** the next question


Used [Page](http://page.sourceforge.net/) by Don Rozenberg for initial GUI design for the manager. 
