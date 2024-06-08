# Day 33 - API Endpoints & API Parameters - ISS Overhead Notifier
## Concepts Practised
* API Endpoints and Making API Calls
* Working with Responses: HTTP Codes, Exceptions & JSON Data
* API Parameters: Match Sunset Times with the Current Time

## Learning Points
### Application Programming Interfaces (API)
* An API is a set of commands, functions, protocols and objects that programmers can use to create software or interact with an external system.
* Important terminologies:
  * **API Endpoint:** digital location (e.g. URL) where an API receives requests
  * **API Request/Call:** message sent by an app to the API asking for a specific service, functionality or data
  * **Response Codes**:
    * 1XX: Hold On
    * 2XX: Here You Go
    * 3XX: Go Away
    * 4XX: You Screwed Up
      * 404: Resource does not exist
      * 401: Not authorised to access resource 
    * 5XX: I Screwed Up
    * More response codes and their definition here: https://www.webfx.com/web-development/glossary/http-status-codes/
   * **API Parameters:** variable parts of a resource. They determine the type of action you want to take on the resource.
 
     ```python response = requests.get(url, params=parameters)```
