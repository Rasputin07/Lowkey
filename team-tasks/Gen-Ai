Primary Responsibility

Implement the GenAI capabilities that turn academic information into understandable explanations, practical study recommendations, and human-reviewed intervention suggestions.

***A. Tasks to Complete***

**1. Set Up the GenAI Integration**

Choose an available LLM API or another suitable model.

The team must verify the provider's current API documentation and model availability before implementation.

Keep API keys in environment variables or an appropriate secrets manager.

Never place an API key in frontend JavaScript or commit it to GitHub.

**2. Build the Student Study Plan Generator**

Develop a feature that accepts authorized academic information, such as:

Current attendance indicators.

Missed assignments.

Upcoming academic deadlines, if available.

Recent assessment performance.

The student's stated academic goals.

Generate a practical study plan that may include:

Suggested study priorities.

A weekly schedule.

Revision recommendations.

Assignment catch-up steps.

Suggested questions for a teacher or mentor.

The generated plan should reflect the available information and avoid making unsupported promises about marks or CGPA.

**3. Build the GenAI Risk Narrator**

Create a function that converts structured backend indicators into a short, understandable summary.

Example input:

{
  "attendance_trend": "declining",
  "attendance_current": 61,
  "missed_recent_assignments": 3
}

Illustrative output:

Attendance has declined, and several recent assignments remain incomplete. Consider reviewing the missed work and discussing any difficulties with an academic mentor.

The final output must be generated from the actual authorized record. The system must not invent additional reasons for the student's difficulties.

**4. Build the Mentor Message Draft Generator**

Allow an authorized mentor to request a supportive outreach-message draft.

The draft should:

Use respectful language.

Describe relevant academic concerns without shaming the student.

Invite the student to discuss difficulties.

Suggest reasonable next steps.

Avoid exposing unnecessary personal information.

A human must review the draft before sending it.

**5. Develop the Agentic Workflow Prototype**

Implement a simple workflow that can:

Receive a risk assessment from the backend.

Prepare a summary of the supporting evidence.

Suggest an appropriate support action.

Prepare a mentor task.

Set a proposed follow-up date.

Track whether the task is reviewed, approved, completed, or overdue.

For the first prototype, a Python workflow or state machine is sufficient.

Do not add autonomous actions that contact students, disclose sensitive information, or make consequential decisions without appropriate human review.

**6. Support the Follow-Up Process**

After an intervention is recorded, the system may prepare a summary of relevant academic changes.

For example:

Attendance increased between the recorded assessment dates, while assignment completion remained unchanged.

The statement must be calculated from the underlying data. GenAI may explain the comparison but should not invent an improvement.

**7. Add Appropriate Fallbacks**

The application must handle:

Missing academic data.

Unsupported questions.

API rate limits.

Network errors.

Invalid model responses.

If GenAI is unavailable, the core dashboard and rule-based risk analysis should continue working.

**8. Keep GenAI Grounded in Approved Information**

The assistant should use authorized academic records and verified institutional rules where available.

If the system does not know a college policy, deadline, or academic requirement, it should state that the information is unavailable rather than guessing.

Student-facing conversations should not automatically be visible to mentors. Any sharing feature must be explicitly designed with appropriate privacy and safeguarding requirements.

***B. Expected Deliverables***

By the departmental round:

One working GenAI feature, preferably the personalized study plan generator.

A risk explanation or mentor-summary feature, if time permits.

A backend function or endpoint that can call the selected model.

Safe API-key handling.

A fallback response when the model cannot be reached.

At least three tested examples using fictional student records.

***C. Files This Member May Own***

genai/
├── study_plan.py
├── risk_narrator.py
├── mentor_assistant.py
└── prompts.py

The team may use a different structure based on the selected backend.

***D. How This Member Works with Others***

With Member 1: Provides the format and interface needed to display GenAI outputs.

With Member 2: Receives validated academic indicators and structured student information.

With Member 4: Integrates GenAI functions into the backend and ensures the API key is handled securely.

***E. Completion Criteria***

Member 3's work is ready when the application can generate at least one useful, data-grounded academic recommendation from a fictional student record, display it in the frontend, and handle errors without breaking the application.
