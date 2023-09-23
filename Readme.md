# Project 4 Backend

- **Project Name:** Personal Best
- **Project By:** Jonathan Casasola
- [**Link To  Frontend GITHUB**](https://github.com/Jonathan1295-09/Project_3Frontend)
- [**LINK TO DEPLOYED WEBSITE**]
- **List of technologies used** Python, django, neon, javascript
- [**Link to Trello**]

## Description

Users will be able to track there personal best max weight lift at they hit at the gym allowing them keep track of how much they improved at the gym.

## List of Backend Endpoints

|     ENDPOINT      | Method |          Purpose          |
| ----------------- | ------ | ------------------------- |
| /personalbest     | GET    | Display of personal best  |
| /perosalbest/new  | POST   | Create a new PB card      |
| /personalbest/:id | DELETE | Delete an existing Card   |
| /personalbest/:id | PUT    | Update an existing Pb     |
| /personalbest/:id | GET    | Display new pb card       |

## ERD (ENTITY RELATIONSHIP DIAGRAM)

```mermaid
erDiagram

USER ||--O{ HOME : indexPage

    HOME || --O{ SHOW : showPb
    SHOW{
        string benchpress
        string shoulderpress
        string deadlift
        string squat
        number cardio
    }

    HOME || --o{ CREATE : createPb
    CREATE {
        string benchpress
        string shoulderpress
        string deadlift
        string squat
        number cardio
    }
    SHOW || --o{ DELETE : deletePb
    DELETE {

    }
    SHOW || --o{ EDIT : editPb
    EDIT {
        string benchpress
        string shoulderpress
        string deadlift
        string squat
        number cardio
    }
