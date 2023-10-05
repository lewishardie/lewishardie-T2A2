# Lewis Hardie - Fantasy Football API - T2A2

## Link to Github Repository:
My github respository can be found at this **[link](https://github.com/lewishardie/lewishardie-T2A2 "Lewis Hardie Github")**.

# Documentation

## 1. Identification of the problem you are trying to solve by building this particular app.
The primary goal behind building this Fantasy Football API is to address the limitations we've encountered while using platforms like sleeper.com for managing our fantasy football leagues. We've identified a need for more flexibility and customisation in league configurations and settings. Currently, these platforms may not always offer the specific features or unique settings we desire for our league's optimal experience. This API is designed to empower us and others to have greater control over managing and customising our fantasy football leagues, ensuring a tailored and enjoyable experience for all participants.

## 2. Why is it a problem that needs solving?
The issue we face with existing platforms like sleeper.com is that they often lack the flexibility and customisation options needed to tailor our fantasy football leagues to our preferences. This limitation can lead to a less-than-ideal experience for participants who seek specific configurations and unique settings. Our aim with this app is to address this problem by providing a solution that empowers users to have complete control over their league management and settings, ensuring a more satisfying and engaging fantasy football experience.

## 3. Why have you chosen this database system. What are the drawbacks compared to others?

I've selected a relational database system for several reasons. Firstly, relational databases offer a high degree of organisation and structure, which is essential for managing complex data relationships effectively. In the context of fantasy football, where data tends to be regular and predictable, this aligns well with the relational model's ability to maintain data integrity.

Furthermore, relational databases provide the flexibility to define relationships between tables, allowing for a robust representation of data. This flexibility is crucial for accurately tracking player statistics and league-related information.

However, it's worth noting that relational databases may have some drawbacks compared to other database systems. For example, they might face challenges in handling unstructured or semi-structured data efficiently. In scenarios where data is less predictable or requires rapid scalability, NoSQL databases could be more suitable.

In summary, the choice of a relational database for this project is driven by its suitability for structured and interconnected data, while acknowledging that other database systems may excel in different contexts.

## 4. Identify and discuss the key functionalities and benefits of an ORM

ORMs, or Object-Relational Mappers, offer streamlined database interactions through object-oriented code. They abstract away low-level database operations, reducing code complexity and enhancing code readability. ORMs also handle essential database tasks like connections, migrations, and seeds, making application development more efficient.

One significant benefit of ORMs is the simplicity they bring to data manipulation. Developers work with objects instead of raw SQL, allowing for cleaner and more maintainable code. This approach also ensures that code remains adaptable even if the underlying database structure changes.

However, learning and setting up an ORM can be time-consuming, especially for newcomers. Additionally, while ORMs handle many tasks, developers still need a solid understanding of database fundamentals and SQL, as complex queries may require custom SQL statements alongside ORM operations.

## 5. Document all endpoints for the API

### POST /auth/register

#### **HTTPS Request**

- **Method:** `POST`
- **Endpoint:** `/auth/register`

#### **Authentication**

- This endpoint doesn't require authentication. 

#### **Path Parameters**

- There aren't any path parameters

#### **Request Parameters**

```json
{
  "username": "new_username",
  "email": "new_email@example.com",
  "password": "new_password"
}
```

#### **Expected Response**

- **Status Code:** 200 OK
- **Response Body:** JSON object containing user information.

#### **Example Response**

```json
{
  "username": "example_user",
  "message": "Success, you have been registered",
  "token": "access_token"
}
```

#### **Error Responses**

- **Status Code:** 400 Unauthorised
- **Response Body:** JSON object with an error message if the user is not authenticated.

### POST /auth/login

#### **HTTPS Request**

- **Method:** `POST`
- **Endpoint:** `/auth/login`

#### **Authentication**

- This endpoint doesn't require authentication. 

#### **Path Parameters**

- There aren't any path parameters

#### **Request Parameters**

```json
{
  "email": "new_email@example.com",
  "password": "new_password"
}
```

#### **Expected Response**

- **Status Code:** 200 OK
- **Response Body:** JSON object containing user information.

#### **Example Response**

```json
{
  "username": "example_user",
  "message": "You have successfully logged in",
  "token": "access token"
}
```

#### **Error Responses**

- **Status Code:** 401 Unauthorised
- **Response Body:** JSON object with an error message if the user is not authenticated.

---

#### **Get All Leagues**

- **HTTP Request**

  - **Method:** `GET`
  - **Endpoint:** `/leagues`

- **Authentication**

  - This endpoint doesn't require authentication.

- **Path Parameters**

  - There aren't any path parameters.

- **Request Parameters**

  - There aren't any request parameters.

- **Expected Response**

  - **Status Code:** 200 OK
  - **Response Body:** JSON array containing league information.

- **Example Response**

  ```json
  [
    {
      "id": 1,
      "league_name": "Example League",
      "description": "This is an example league.",
      "max_player_per_team": 15,
      "max_teams": 10,
      "admin_id": 1
    }
  ]
  ```

- **Error Responses**

  - None.

---

#### **Create a League**

- **HTTP Request**

  - **Method:** `POST`
  - **Endpoint:** `/leagues`

- **Authentication**

  - This endpoint requires authentication.

- **Path Parameters**

  - There aren't any path parameters.

- **Request Parameters**

  ```json
  {
    "league_name": "New League",
    "description": "This is a new league.",
    "max_player_per_team": 20,
    "max_teams": 8
  }
  ```

- **Expected Response**

  - **Status Code:** 201 Created
  - **Response Body:** JSON object containing league information.

- **Example Response**

  ```json
  {
    "id": 2,
    "league_name": "New League",
    "description": "This is a new league.",
    "max_player_per_team": 20,
    "max_teams": 8,
    "admin_id": 1
  }
  ```

- **Error Responses**

  - None.

---

#### **Get a Specific League by ID**

- **HTTP Request**

  - **Method:** `GET`
  - **Endpoint:** `/leagues/<int:league_id>`

- **Authentication**

  - This endpoint doesn't require authentication.

- **Path Parameters**

  - `league_id`: The ID of the league to retrieve.

- **Request Parameters**

  - There aren't any request parameters.

- **Expected Response**

  - **Status Code:** 200 OK
  - **Response Body:** JSON object containing league information.

- **Example Response**

  ```json
  {
    "id": 1,
    "league_name": "Example League",
    "description": "This is an example league.",
    "max_player_per_team": 15,
    "max_teams": 10,
    "admin_id": 1
  }
  ```

- **Error Responses**

  - **Status Code:** 404 Not Found
  - **Response Body:** JSON object with an error message if the league with the specified ID is not found.

---

#### **Delete a Specific League by ID**

- **HTTP Request**

  - **Method:** `DELETE`
  - **Endpoint:** `/leagues/<int:league_id>`

- **Authentication**

  - This endpoint requires authentication.

- **Path Parameters**

  - `league_id`: The ID of the league to delete.

- **Request Parameters**

  - There aren't any request parameters.

- **Expected Response**

  - **Status Code:** 200 OK
  - **Response Body:** JSON object with a success message.

- **Example Response**

  ```json
  {
    "message": "League with the id='1' has been deleted"
  }
  ```

- **Error Responses**

  - **Status Code:** 401 Unauthorised
  - **Response Body:** JSON object with an error message if the current user is not authorised to delete the league.
  - **Status Code:** 404 Not Found
  - **Response Body:** JSON object with an error message if the league with the specified ID is not found.

---

#### **Update a Specific League by ID**

- **HTTP Request**

  - **Method:** `PUT`
  - **Endpoint:** `/leagues/<int:league_id>`

- **Authentication**

  - This endpoint requires authentication.

- **Path Parameters**

  - `league_id`: The ID of the league to update.

- **Request Parameters**

  ```json
  {
    "league_name": "Updated League Name",
    "description": "Updated league description."
  }
  ```

- **Expected Response**

  - **Status Code:** 200 OK
  - **Response Body:** JSON object containing updated league information.

- **Example Response**

  ```json
  {
    "id": 1,
    "league_name": "Updated League Name",
    "description": "Updated league description.",
    "max_player_per_team": 15,
    "max_teams": 10,
    "admin_id": 1
  }
  ```

- **Error Responses**

  - **Status Code:** 401 Unauthorised
  - **Response Body:** JSON object with an error message if the current user is not authorised to update the league.
  - **Status Code:** 404 Not Found
  - **Response Body:** JSON object with an error message if the league with the specified ID is not found.

---

#### **Join a Specific League**

- **HTTP Request**

  - **Method:** `POST`
  - **Endpoint:** `/leagues/join/<int:league_id>`

- **Authentication**

  - This endpoint requires authentication.

- **Path Parameters**

  - `league_id`: The ID of the league to join.

- **Request Parameters**

  ```json
  {
    "team_name": "My Team",
    "user_id": 1,
    "league_id": 1
  }
  ```

- **Expected Response**

  - **Status Code:** 201 Created
  - **Response Body:** JSON object containing team information.

- **Example Response**

  ```json
  {
    "id": 1,
    "team_name": "My Team",
    "user_id": 1,
    "league_id": 1
  }
  ```

- **Error Responses**

  - **Status Code:** 400 Bad Request
  - **Response Body:** JSON object with an error message if the league is full or the user has already joined the league.

  - **Status Code:** 404 Not Found
  - **Response Body:** JSON object with an error message if the league with the specified ID is not found.

---

#### **Get a Specific Team in a League**

- **HTTP Request**

  - **Method:** `GET`
  - **Endpoint:** `/leagues/<int:league_id>/team/<int:team_id>`

- **Authentication**

  - This endpoint requires authentication.

- **Path Parameters**

  - `league_id`: The ID of the league containing the team.
  - `team_id`: The ID of the team to retrieve.

- **Request Parameters**

  - There aren't any request parameters.

- **Expected Response**

  - **Status Code:** 200 OK
  - **Response Body:** JSON object containing team information.

- **Example Response**

  ```json
  {
    "id": 1,
    "team_name": "My Team",
    "user_id": 1,

---

#### **Get All Players**

- **HTTP Request**

  - **Method:** `GET`
  - **Endpoint:** `/players`

- **Authentication**

  - This endpoint doesn't require authentication.

- **Path Parameters**

  - There aren't any path parameters.

- **Request Parameters**

  - There aren't any request parameters.

- **Expected Response**

  - **Status Code:** 200 OK
  - **Response Body:** JSON array containing player information.

- **Example Response**

  ```json
  [
    {
      "id": 1,
      "first_name": "First Name",
      "last_name": "Last Name",
      "position": "Quarterback",
      "nfl_team": "Football Team",
      "is_available": true
    },
    {
      "id": 2,
      "first_name": "First Name",
      "last_name": "Last Name",
      "position": "Quarterback",
      "nfl_team": "Football Team",
      "is_available": false
    }
  ]
  ```

- **Error Responses**

  - None.

---

#### **Get a Specific Player by ID**

- **HTTP Request**

  - **Method:** `GET`
  - **Endpoint:** `/players/<int:player_id>`

- **Authentication**

  - This endpoint doesn't require authentication.

- **Path Parameters**

  - `player_id`: The ID of the player to retrieve.

- **Request Parameters**

  - There aren't any request parameters.

- **Expected Response**

  - **Status Code:** 200 OK
  - **Response Body:** JSON object containing player information.

- **Example Response**

  ```json
  {
    "id": 1,
    "first_name": "First Name",
    "last_name": "Last Name",
    "position": "Quarterback",
    "nfl_team": "Football Team",
    "is_available": true
  }
  ```

- **Error Responses**

  - **Status Code:** 404 Not Found
  - **Response Body:** JSON object with an error message if the player with the specified ID is not found.

---

#### **Get All Available Players**

- **HTTP Request**

  - **Method:** `GET`
  - **Endpoint:** `/players/available`

- **Authentication**

  - This endpoint doesn't require authentication.

- **Path Parameters**

  - There aren't any path parameters.

- **Request Parameters**

  - There aren't any request parameters.

- **Expected Response**

  - **Status Code:** 200 OK
  - **Response Body:** JSON array containing available player information.

- **Example Response**

  ```json
  [
    {
      "id": 1,
        "first_name": "First Name",
        "last_name": "Last Name",
        "position": "Quarterback",
        "nfl_team": "Football Team",
      "is_available": true
    }
  ]
  ```

- **Error Responses**

  - **Status Code:** 404 Not Found
  - **Response Body:** JSON object with a message if no available players are found.

---

#### **Get All Rosters**

- **HTTP Request**

  - **Method:** `GET`
  - **Endpoint:** `/rosters`

- **Authentication**

  - This endpoint doesn't require authentication.

- **Path Parameters**

  - There aren't any path parameters.

- **Request Parameters**

  - There aren't any request parameters.

- **Expected Response**

  - **Status Code:** 200 OK
  - **Response Body:** JSON array containing roster information.

- **Example Response**

  ```json
  [
    {
      "id": 1,
      "roster_slot": "Forward",
      "player_id": 1
    },
    {
      "id": 2,
      "roster_slot": "Midfielder",
      "player_id": 2
    }
  ]
  ```

- **Error Responses**

  - None.

---

#### **Get a Specific Roster by ID**

- **HTTP Request**

  - **Method:** `GET`
  - **Endpoint:** `/rosters/<int:roster_id>`

- **Authentication**

  - This endpoint doesn't require authentication.

- **Path Parameters**

  - `roster_id`: The ID of the roster to retrieve.

- **Request Parameters**

  - There aren't any request parameters.

- **Expected Response**

  - **Status Code:** 200 OK
  - **Response Body:** JSON object containing roster information.

- **Example Response**

  ```json
  {
    "id": 1,
    "roster_slot": "Forward",
    "player_id": 1
  }
  ```

- **Error Responses**

  - **Status Code:** 404 Not Found
  - **Response Body:** JSON object with an error message if the roster with the specified ID is not found.

---

#### **List All Teams**

- **HTTP Request**

  - **Method:** `GET`
  - **Endpoint:** `/teams/list`

- **Authentication**

  - This endpoint doesn't require authentication.

- **Path Parameters**

  - There aren't any path parameters.

- **Request Parameters**

  - There aren't any request parameters.

- **Expected Response**

  - **Status Code:** 200 OK
  - **Response Body:** JSON array containing team information.

- **Example Response**

  ```json
  [
    {
      "id": 1,
      "team_name": "Team A",
      "league_id": 1
    },
    {
      "id": 2,
      "team_name": "Team B",
      "league_id": 1
    }
  ]
  ```

- **Error Responses**

  - None.

---

#### **Get a Specific Team by ID**

- **HTTP Request**

  - **Method:** `GET`
  - **Endpoint:** `/teams/<int:team_id>`

- **Authentication**

  - This endpoint doesn't require authentication.

- **Path Parameters**

  - `team_id`: The ID of the team to retrieve.

- **Request Parameters**

  - There aren't any request parameters.

- **Expected Response**

  - **Status Code:** 200 OK
  - **Response Body:** JSON object containing team information.

- **Example Response**

  ```json
  {
    "id": 1,
    "team_name": "Team A",
    "league_id": 1
  }
  ```

- **Error Responses**

  - **Status Code:** 404 Not Found
  - **Response Body:** JSON object with an error message if the team with the specified ID is not found.

---

#### **Update a Team**

- **HTTP Request**

  - **Method:** `PUT`
  - **Endpoint:** `/teams/<int:team_id>`

- **Authentication**

  - The user must be authenticated and authorised to update the team.

- **Path Parameters**

  - `team_id`: The ID of the team to update.

- **Request Parameters**

  ```json
  {
    "team_name": "Updated Team Name"
  }
  ```

- **Expected Response**

  - **Status Code:** 200 OK
  - **Response Body:** JSON object containing the updated team information.

- **Example Response**

  ```json
  {
    "id": 1,
    "team_name": "Updated Team Name",
    "league_id": 1
  }
  ```

- **Error Responses**

  - **Status Code:** 401 Unauthorised
  - **Response Body:** JSON object with an error message if the user is not authorised to update the team.
  - **Status Code:** 404 Not Found
  - **Response Body:** JSON object with an error message if the team with the specified ID is not found.

---

#### **Delete a Team**

- **HTTP Request**

  - **Method:** `DELETE`
  - **Endpoint:** `/teams/<int:team_id>`

- **Authentication**

  - The user must be authenticated and authorised to delete the team.

- **Path Parameters**

  - `team_id`: The ID of the team to delete.

- **Request Parameters**

  - There aren't any request parameters.

- **Expected Response**

  - **Status Code:** 200 OK
  - **Response Body:** JSON object with a message confirming the deletion of the team.

- **Example Response**

  ```json
  {
    "message": "Team with the id=`1` has been deleted"
  }
  ```

- **Error Responses**

  - **Status Code:** 401 Unauthorised
  - **Response Body:** JSON object with an error message if the user is not authorised to delete the team.
  - **Status Code:** 404 Not Found
  - **Response Body:** JSON object with an error message if the team with the specified ID is not found.

---

#### **Add a Player to a Team's Roster**

- **HTTP Request**

  - **Method:** `POST`
  - **Endpoint:** `/teams/<int:team_id>/add/<int:player_id>`

- **Authentication**

  - The user must be authenticated and authorised to add a player to the team's roster.

- **Path Parameters**

  - `team_id`: The ID of the team to which the player will be added.
  - `player_id`: The ID of the player to add to the team's roster.

- **Request Parameters**

  - There aren't any request parameters.

- **Expected Response**

  - **Status Code:** 201 Created
  - **Response Body:** JSON object with a message confirming that the player has been added to the team's roster.

- **Example Response**

  ```json
  {
    "message": "Player added to the team's roster"
  }
  ```

- **Error Responses**

  - **Status Code:** 401 Unauthorised
  - **Response Body:** JSON object with an error message if the user is not authorised to add a player to the team's roster.
  - **Status Code:** 404 Not Found
  - **Response Body:** JSON object with an error message if the team or player with the specified IDs is not found.
  - **Status Code:** 400 Bad Request
  - **Response Body:** JSON object with an error message if the player is already in a roster.

---

#### **List All Users**

- **HTTP Request**

  - **Method:** `GET`
  - **Endpoint:** `/user/`

- **Authentication**

  - This endpoint doesn't require authentication.

- **Path Parameters**

  - There aren't any path parameters.

- **Request Parameters**

  - There aren't any request parameters.

- **Expected Response**

  - **Status Code:** 200 OK
  - **Response Body:** JSON array containing user information.

- **Example Response**

  ```json
  [
    {
      "id": 1,
      "username": "user1",
      "email": "user1@example.com"
    },
    {
      "id": 2,
      "username": "user2",
      "email": "user2@example.com"
    }
  ]
  ```

- **Error Responses**

  - None.

---

#### **Get a Specific User by ID**

- **HTTP Request**

  - **Method:** `GET`
  - **Endpoint:** `/user/<int:user_id>`

- **Authentication**

  - The user must be authenticated to access this endpoint, and they can only retrieve their own user information.

- **Path Parameters**

  - `user_id`: The ID of the user to retrieve.

- **Request Parameters**

  - There aren't any request parameters.

- **Expected Response**

  - **Status Code:** 200 OK
  - **Response Body:** JSON object containing user information.

- **Example Response**

  ```json
  {
    "id": 1,
    "username": "user1",
    "email": "user1@example.com"
  }
  ```

- **Error Responses**

  - **Status Code:** 401 Unauthorised
  - **Response Body:** JSON object with an error message if the user is not authorised to access the requested user's information.
  - **Status Code:** 404 Not Found
  - **Response Body:** JSON object with an error message if the user with the specified ID is not found.

---

#### **Update a User**

- **HTTP Request**

  - **Method:** `PUT`
  - **Endpoint:** `/user/<int:user_id>`

- **Authentication**

  - The user must be authenticated to access this endpoint, and they can only update their own user information.

- **Path Parameters**

  - `user_id`: The ID of the user to update.

- **Request Parameters**

  ```json
  {
    "username": "new_username",
    "first_name": "new_first_name",
    "last_name": "new_last_name",
    "email": "new_email@example.com",
    "password": "new_password"
  }
  ```

  - You can include any combination of the above fields you want to update.

- **Expected Response**

  - **Status Code:** 200 OK
  - **Response Body:** JSON object containing the updated user information.

- **Example Response**

  ```json
  {
    "id": 1,
    "username": "new_username",
    "first_name": "new_first_name",
    "last_name": "new_last_name",
    "email": "new_email@example.com"
  }
  ```

- **Error Responses**

  - **Status Code:** 401 Unauthorised
  - **Response Body:** JSON object with an error message if the user is not authorised to update the user information.
  - **Status Code:** 404 Not Found
  - **Response Body:** JSON object with an error message if the user with the specified ID is not found.

---

#### **Delete a User**

- **HTTP Request**

  - **Method:** `DELETE`
  - **Endpoint:** `/user/<int:user_id>`

- **Authentication**

  - The user must be authenticated to access this endpoint, and they can only delete their own user account.

- **Path Parameters**

  - `user_id`: The ID of the user to delete.

- **Request Parameters**

  - There aren't any request parameters.

- **Expected Response**

  - **Status Code:** 200 OK
  - **Response Body:** JSON object with a message confirming the deletion of the user.

- **Example Response**

  ```json
  {
    "message": "User with the id=`1` has been deleted"
  }
  ```

- **Error Responses**

  - **Status Code:** 401 Unauthorised
  - **Response Body:** JSON object with an error message if the user is not authorised to delete the user account.
  - **Status Code:** 404 Not Found
  - **Response Body:** JSON object with an error message if the user with the specified ID is not found.

---

## 6. An ERD for the app

![ERD](/docs/web-api-erd.png)

## 7. Detail any third party services that the app will use

The app relies on several third-party services and libraries to enhance functionality and security:

SQLAlchemy: This powerful ORM simplifies database interactions, making it easier to work with our relational database system.

Flask: Flask is a micro web framework used for creating web applications. It forms the backbone of our app's API and routing system.

Bcrypt: Bcrypt is a password hashing library that enhances security by securely storing user passwords in the database.

JWT Manager: This library manages JSON Web Tokens (JWTs) for user authentication and authorisation, ensuring secure access to protected routes.

Marshmallow: Marshmallow provides serialisation and deserialisation capabilities for transforming complex data types, ensuring smooth data exchange between the frontend and backend of our app.

## 8. Describe the projects models in terms of the relationships they have with each other

In my Fantasy Football web API, the models have the following relationships with each other:

### User Model (User):

A user can create multiple teams (One-to-Many with Team).
A user can be the admin of multiple leagues (One-to-Many with League).

### Team Model (Team):

A team belongs to one user (Many-to-One with User).
A team is part of one league (Many-to-One with League).
A team has one roster (One-to-One with Roster).
A team can have multiple players on its roster (One-to-Many with Player).

### League Model (League):

A league can have multiple teams (One-to-Many with Team).
A league has one admin user (Many-to-One with User).

### Player Model (Player):

A player can be on multiple rosters (Many-to-Many with Roster through PlayerRoster).

### Roster Model (Roster):

A roster belongs to one team (Many-to-Many with Team). (This is intended, but I the code I've produced doesn't add up)
A roster can have multiple players (One-to-Many with Player).
A roster can have multiple players through PlayerRoster (Many-to-Many with Player).

These relationships allow the web api to represent the structure of the Fantasy Football application, where users can create teams, join leagues, and manage rosters with players. Teams are associated with users and leagues, and rosters are associated with teams, enabling the organisation of player data within the context of each team. Players can be part of multiple rosters, facilitating their inclusion on different teams in various leagues.

## 9. Discuss the database relations to be implemented in your application

In my Fantasy Football web API, I have several database relations to be implemented to effectively model the relationships between various entities. Here's how these relations can be described using my models:

### User - Team Relation:

- A user can create multiple teams, which establishes a one-to-many relationship between the User model and the Team model.
- This means that each user can have multiple teams, but each team is associated with only one user.

### User - League Relation:

- A user can be the admin of multiple leagues, creating another one-to-many relationship between the User model and the League model.
- Each user can be associated with multiple leagues, but each league has one admin user.

### Team - User Relation:

- Each team belongs to one user, establishing a many-to-one relationship between the Team model and the User model.
- This means that many teams can belong to a single user.

### Team - League Relation:

- Each team is part of one league, creating a many-to-one relationship between the Team model and the League model.
- Multiple teams can be part of the same league.

### Team - Roster Relation:

- Each team has one roster, establishing a one-to-one relationship between the Team model and the Roster model.
- This ensures that each team has a single roster associated with it.

### Team - Player Relation:

- A team can have multiple players on its roster, creating a one-to-many relationship between the Team model and the Player model.
- Each team can have multiple players, but each player belongs to only one team.

### League - Team Relation:

- A league can have multiple teams, resulting in a one-to-many relationship between the League model and the Team model.
- This allows multiple teams to participate in the same league.

### League - User Relation:

- Each league has one admin user, establishing a many-to-one relationship between the League model and the User model.
- Each league has a single admin user.

### Player - Roster Relation:

- A player can be on multiple rosters, creating a many-to-many relationship between the Player model and the Roster model through an intermediary table (PlayerRoster).
- This allows players to be part of different teams' rosters.

## 10. Describe the way tasks are allocated and tracked in your project

In my project, I unfortunately had a bit of personal problems getting started, so my tracking of tasks and allocations really didnt exist.

### Version Control: 
I utilised Git and services like GitHub to maintain a versioned codebase.

### Project Management Tools: 
I had intended to use a project management tool like Trello, but the last minute nature of the last week or so has forced me to really brute force my workflow.

### Workflow:

My development workflow typically followed these steps:

1. Start coding
- Start on an aspect of the app, i.e. "leagues", working through the schema, model and controllers until it seemed functional

2. Trial and Error
- Make adjustsment to app if there were errors running flask or if there were HTTP request errors

3. Delete all code that wasn't working and start again
- Spend hours on a bit of code, only for some small error to be blocking my progress

4. Test Manually
- Manual tests conducted at every milestone, which envolved going through and checking each http request

### Documentation
- Tried to be digilgent about commenting, probably the best commenting I've done so far.
- Documented all the end points

## After thoughts
