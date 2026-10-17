Primary Responsibility

Build and maintain the application backend, connect the frontend to the database and GenAI components, and implement the core integration and access-control structure.

***A. Tasks to Complete***

**1. Set Up the Backend**

Choose Flask or FastAPI and create a backend that can:

Start locally.

Receive frontend requests.

Validate incoming information.

Call database functions.

Run academic indicator calculations.

Return structured responses.

Handle errors consistently.

The team should agree on one framework rather than developing two separate backends.

**2. Define the API Contract**

Agree on the request and response formats with all team members.

Suggested endpoints include:

Endpoint

Purpose

GET /api/dashboard

Return dashboard statistics

GET /api/students

Return authorized student records

GET /api/students/<id>

Return a student's academic profile

GET /api/students/<id>/risk

Return risk indicators and explanations

POST /api/students/<id>/study-plan

Request a GenAI study plan

GET /api/interventions

Return authorized intervention records

POST /api/interventions

Record a new intervention

PATCH /api/interventions/<id>

Update intervention status

GET /api/students/<id>/timeline

Return weekly academic trends

These are proposed endpoints. Their names and request formats must be finalized by the team before integration.

**3. Connect the Database**

Use the database functions created by Member 2.

The backend should retrieve real records and return them in a consistent JSON format.

Avoid creating duplicate datasets inside different files that gradually become inconsistent.

**4. Integrate the GenAI Component**

Connect Member 3's GenAI functions to the appropriate backend endpoints.

Ensure that:

The API key remains on the backend.

Only necessary academic data is sent to the model.

Requests are validated.

API failures are handled.

Generated content is returned in a predictable format.

**5. Implement Intervention APIs**

Allow authorized users to:

Create an intervention record.

View intervention status.

Update a task after review.

Record completion and follow-up dates.

Add an outcome based on available evidence.

Do not claim that an intervention was successful unless the outcome is supported by recorded data.

**6. Implement Basic Access Controls**

Design the application so that different roles have appropriate permissions.

For a hackathon prototype, the team may demonstrate the role-based structure with a clearly labelled mock login, but it must not claim production-grade authentication if it has not been implemented.

In a deployed version, authentication and authorization must be enforced on the backend, not merely by hiding frontend buttons.

**7. Add Error Handling**

Handle common errors such as:

Invalid student identifiers.

Missing database records.

Invalid request bodies.

Database connection failures.

GenAI API errors.

Unauthorized requests.

Return useful error messages without exposing API keys or sensitive internal information.

**8. Support Local Development and Integration**

Prepare a clear way for team members to run the application locally.

Document:

Required software.

Dependency installation.

Environment-variable configuration.

Database initialization.

How to start the backend.

How to open the frontend.

Common setup problems.

For the hackathon, the application may run locally. Public hosting is not mandatory unless the team decides it is necessary for the demonstration.

**9. Coordinate Integration and Testing**

Ensure that:

The frontend uses the agreed API routes.

The backend retrieves data from the shared database.

GenAI features receive the correct input.

Intervention records persist after the page is refreshed.

The complete demonstration workflow works end to end.

***B. Expected Deliverables***

By the departmental round:

A running backend.

Defined and working API endpoints for core features.

Database integration.

GenAI endpoint integration.

Basic validation and error handling.

Intervention record creation and status updates.

Setup instructions.

An end-to-end working local demonstration.

***C. Files This Member May Own***

backend/
├── app.py
├── routes/
│   ├── dashboard.py
│   ├── students.py
│   ├── study_plans.py
│   └── interventions.py
├── services/
│   └── ...
└── requirements.txt

.env.example
.gitignore

The final structure may differ depending on the framework.

***D. How This Member Works with Others***

With Member 1: Agrees on endpoint names, response formats, and frontend integration.

With Member 2: Connects the backend to the shared database and academic calculations.

With Member 3: Integrates GenAI functions and manages server-side API requests.

***E. Completion Criteria***

Member 4's work is ready when the frontend, database, and GenAI components communicate through the backend and the core demonstration can be completed without manually editing application data during the presentation.
