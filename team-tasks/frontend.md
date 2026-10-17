**MEMBER 1 — Frontend Developer and Dashboard Designer**

Assigned to: Member 1 — [Name / GitHub Username]

*Primary Responsibility*

Build the user interface of EduGuard AI, including the dashboard, student views, academic charts, and intervention screens.

***A. Tasks to Complete***

**1. Create the Main Dashboard (dark mode light mode)**

Build a dashboard that displays:

Total number of fictional students in the dataset.

Number of students requiring attention.

Overall attendance statistics.

Assignment completion statistics.

Academic performance trends.

Pending intervention counts.

The frontend must retrieve real values from the backend or database rather than relying on permanently hardcoded demonstration numbers.

**2. Build Student Academic Profile Pages**

Create a profile view that displays:

Student identifier.

Department and semester, where appropriate.

Attendance trends.

Assignment submission history.

Internal assessment performance.

LMS engagement indicators.

Explainable risk indicators.

Recommended next steps.

Use fictional identifiers and sample data in the hackathon demonstration.

**3. Implement Visualizations**

Use Chart.js or a similar charting library to create:

Weekly attendance charts.

Academic performance charts.

Assignment completion charts.

LMS engagement trends.

Before-and-after intervention comparisons, where suitable data exists.

Charts must accurately represent the values received from the backend.

**4. Create Intervention Management Screens**

Build screens for authorized mentors to:

View suggested interventions.

View pending tasks.

Review intervention details.

Record intervention status.

View scheduled follow-ups.

View recorded outcomes.

The frontend should not independently approve or execute consequential actions.

**5. Build Student-Friendly Screens**

Create a supportive student interface that displays:

Academic progress.

Study recommendations.

Weekly goals.

Target CGPA planning, if implemented.

Relevant GenAI responses.

Avoid harsh labels, unnecessarily alarming warnings, and unsupported promises.

**6. Integrate the Frontend with the Backend**

Connect the user interface to the agreed API endpoints.

Display appropriate messages when:

Data is loading.

No records are available.

An API request fails.

GenAI is temporarily unavailable.

A submitted form contains invalid information.

**7. Improve Usability**

Ensure that:

Navigation is understandable.

Text is readable.

Important information is easy to locate.

The layout works on common laptop and mobile screen sizes.

Forms have clear labels.

Charts include meaningful titles and labels.

***B. Expected Deliverables***

By the departmental round:

A working dashboard.

At least one student profile view.

Academic trend visualizations.

A basic intervention management screen.

A connected GenAI output screen, if the API integration is ready.

A frontend that works with the shared demonstration data.

***C. Files This Member May Own***

frontend/
├── index.html
├── student.html
├── interventions.html
├── css/
│   └── style.css
└── js/
    ├── dashboard.js
    ├── student.js
    └── interventions.js

This is a suggested structure. The team may use a different structure if agreed upon.

***D. How This Member Works with Others***

With Member 2: Receives the database fields, academic indicators, and risk explanations that need to be displayed.

With Member 3: Displays study plans, GenAI summaries, and generated recommendations.

With Member 4: Connects screens to backend endpoints and reports integration errors.

***E. Completion Criteria***

Member 1's work is ready when a user can open the application, navigate the dashboard, view student information, and see data returned by the backend without relying on manually fabricated results.
