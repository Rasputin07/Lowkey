# Lowkey 🎓
### AI-Powered Early Dropout Prediction, Academic Risk Analysis & Intelligent Intervention Platform

**Lowkey** is a student success platform designed to identify students who may be experiencing academic difficulties at an early stage. It combines academic data analysis, LMS activity monitoring, Explainable AI, Generative AI (GenAI), and Agentic AI to help students and mentors take timely, informed action.

Instead of simply flagging students as being at risk, EduGuard AI aims to explain the underlying academic patterns, generate personalized learning support, coordinate interventions, and track whether students' academic indicators improve over time.

> **Our mission:** Identify academic difficulties early, generate meaningful learning support, and help educational institutions support students before their problems become more serious.

---



## 🔴 Problem

Universities and colleges often identify struggling students only after poor examination results, repeated failures, or withdrawal from a course.

However, early warning signals may already exist across different systems, including:

- Declining class attendance.
- Reduced activity on Learning Management Systems (LMS).
- Missed assignments and approaching deadlines.
- Declining quiz and internal assessment scores.
- Difficulty maintaining a desired CGPA.
- Other relevant academic engagement indicators.

These signals are frequently scattered across different platforms, making it difficult for mentors and institutions to develop a complete understanding of a student's academic situation.

Existing monitoring approaches may identify a problem without explaining its causes, recommending suitable support, or tracking whether the intervention was effective.

### Our Challenge

How can we combine academic data, AI-driven insights, personalized learning assistance, and structured intervention workflows to help identify and support students experiencing academic difficulties at an early stage?

---

## 💡 Our Solution

Lowkey proposes a centralized dashboard that combines student academic information and LMS-related activity to identify concerning patterns and support timely interventions.

The platform is designed around five connected capabilities:

1. **Academic Data Integration:** Organize student records, attendance, subjects, assignments, assessment marks, semester results, and LMS engagement.
2. **Early-Warning Analytics:** Identify concerning academic trends and explain the indicators behind each warning.
3. **Generative AI Assistance:** Generate personalized study plans, revision material, practice quizzes, mentor summaries, and supportive messages.
4. **Agentic AI Workflow:** Coordinate mentor alerts, recommended interventions, follow-up tasks, and progress reviews.
5. **Closed-Loop Monitoring:** Record interventions and examine whether relevant academic indicators improve afterward.

For the initial prototype, fictional student records will be used to demonstrate the system without requiring direct access to a college's private ERP or LMS.

---

## 🎯 Project Objectives

- Identify potential academic difficulties before major academic setbacks occur.
- Consolidate academic and LMS-related information into one dashboard.
- Make risk assessments understandable through explainable indicators.
- Generate personalized learning recommendations using GenAI.
- Help students work toward realistic academic goals, including a target CGPA.
- Coordinate mentor-led interventions through an AI-assisted workflow.
- Track intervention completion and subsequent academic progress.
- Examine model performance and potential differences in outcomes across student groups.
- Protect student privacy and ensure AI supports rather than penalizes students.

---

## 🚀 Key Features

### 1. Unified Student Academic Dashboard

A centralized dashboard displaying relevant student academic information.

**Planned capabilities:**

- Student profile and semester information.
- Subject-wise academic performance.
- Attendance percentages and trends.
- Assignment submission and completion status.
- Quiz and internal assessment results.
- Current CGPA and target CGPA.
- LMS activity and course completion indicators.
- Weekly academic progress visualization.

The dashboard will help students and authorized mentors understand academic progress without switching between multiple systems.

### 2. Early Academic Risk Detection

The system will analyze available academic indicators to identify patterns that may warrant attention.

**Example warning signals:**

- Attendance decreased from 82% to 61% over three weeks.
- Three of the last four assignments were missed.
- Quiz performance declined compared with the student's earlier results.
- LMS engagement decreased significantly.
- Performance in a particular subject has deteriorated.

The initial prototype may use transparent, rule-based indicators. A trained machine-learning model can be introduced when suitable historical data and reliable outcome labels are available.

**Important:** A risk indicator is a reason to investigate and offer support, not proof that a student will fail or drop out.

### 3. Explainable Risk Analysis

Rather than displaying a risk category without context, the system will explain which observed indicators contributed to the warning.

**Planned capabilities:**

- Display the academic indicators behind a warning.
- Highlight changes in attendance, assignment completion, and assessment performance.
- Show weekly risk and engagement trends.
- Explain why a case was flagged.
- Provide actionable suggestions based on the available evidence.

For example:

> Attendance has declined over the last three weeks, and several recent assignments remain incomplete. Consider reviewing the student's current workload and discussing whether academic support would be helpful.

The system will distinguish verified data from generated explanations and avoid presenting unsupported conclusions as facts.

### 4. GenAI Student Learning Copilot

The Generative AI component will help students understand their academic situation and create practical learning resources.

**Planned capabilities:**

- Personalized weekly study plans.
- Topic explanations based on a student's learning needs.
- Revision notes from approved course material.
- Subject-specific practice questions and quizzes.
- Assignment and assessment preparation plans.
- Recommendations for improving learning habits.
- Academic progress summaries.
- Study plans designed around a student's target CGPA.

#### Example

A student currently has a CGPA of 7.1 and wants to work toward a target of 8.0.

The system can use available academic records to identify subjects needing attention and generate a structured study plan.

Python-based calculations will handle numerical academic requirements. GenAI will explain the results and generate practical recommendations.

The system will not guarantee a particular CGPA or invent grades required to achieve a target.

### 5. GenAI Risk Narrator and Mentor Assistant

GenAI will transform verified academic indicators into concise, understandable summaries.

**Planned capabilities:**

- Summarize why a student was flagged for review.
- Draft supportive messages for students.
- Prepare mentor meeting briefs.
- Suggest constructive questions for academic discussions.
- Recommend possible academic support options.
- Summarize completed interventions and available progress data.

Generated summaries and messages will be reviewed by authorized staff before sensitive communication or intervention.

### 6. Agentic AI Intervention Workflow

The Agentic AI component will help coordinate multi-step academic support workflows.

**Planned workflow:**

1. Review updated academic indicators on a scheduled basis.
2. Identify cases meeting defined review criteria.
3. Prepare an explanation of the observed changes.
4. Recommend possible interventions, such as remedial classes or mentor meetings.
5. Prepare a mentor notification for review.
6. Record an approved intervention.
7. Create a follow-up task and due date.
8. Review updated academic indicators after the follow-up interval.
9. Flag cases that may require further human review.

For the prototype, this workflow may use a scheduled Python process or a controlled state machine.

Sensitive decisions, including counseling referrals and escalations, will remain subject to appropriate human review.

### 7. Closed-Loop Intervention Tracking

Unlike systems that stop after generating a warning, EduGuard AI aims to track what happens after support is offered.

**Planned capabilities:**

- Record the type of intervention.
- Record when it was assigned and whether it was completed.
- Store follow-up dates and status.
- Compare relevant academic indicators before and after an intervention.
- Display intervention completion and outcome summaries.
- Identify cases that may need additional support.

For example, the dashboard may eventually display:

**"48 interventions recorded this semester; 31 were followed by improved risk indicators."**

Such figures will only be presented as actual results when calculated from recorded data. Demonstration figures will be clearly labelled as illustrative.

Improvement after an intervention does not, by itself, prove that the intervention caused the improvement.

### 8. Silent Disengagement Detection

Attendance alone cannot capture every academic difficulty.

A student may continue attending classes while struggling to complete assignments or engage with course material.

EduGuard AI will therefore combine available signals, such as:

- Attendance trends.
- Assignment submission patterns.
- LMS logins and activity.
- Course module completion.
- Quiz participation.
- Subject-wise academic performance.

The goal is to identify patterns that may warrant a supportive check-in rather than relying on a single metric.

### 9. Target CGPA Planner

Students will be able to explore academic goals and receive practical guidance on improving or maintaining their performance.

**Planned capabilities:**

- Enter a target CGPA.
- View current academic performance.
- Identify subjects requiring additional attention.
- Review upcoming assignments and assessments.
- Generate a personalized study schedule.
- Track progress toward academic goals.

CGPA calculations will use the institution's grading rules and credit information when available.

The application will distinguish between a calculated academic result and an AI-generated recommendation.

### 10. Fairness and Bias Monitoring

The platform will include safeguards to examine whether risk assessments may produce uneven outcomes across relevant student groups.

**Planned capabilities:**

- Compare flagging rates across appropriate groups where lawful and justified.
- Examine false-positive and false-negative rates when reliable outcome labels are available.
- Document model limitations and potential sources of bias.
- Restrict sensitive attributes from prediction inputs.
- Investigate proxy effects and other unintended biases.

Excluding sensitive attributes from a model does not automatically eliminate bias. Fairness checks must consider both the data and the model's actual outcomes.

### 11. Weekly Academic Risk Timeline

The system will track changes in academic indicators over time.

**Planned capabilities:**

- Weekly attendance trends.
- Assignment completion history.
- Assessment performance changes.
- LMS engagement trends.
- Historical risk indicators.
- Intervention dates and subsequent progress.

This helps mentors distinguish between a recent decline and a stable pattern that requires a different kind of support.

### 12. Role-Based Access and Student Privacy

Different users should only access information appropriate to their role.

**Planned roles:**

- Students can view their own academic information and learning support.
- Mentors can view relevant information for their assigned students.
- Department administrators can access authorized aggregate reports.
- Authorized staff can manage intervention workflows.

The system will aim to maintain appropriate consent records, access restrictions, and audit logs.

Students' AI conversations will not be visible to mentors by default. Any sharing functionality will be designed around clearly explained permissions and applicable safeguarding requirements.

---

## 🔄 How the System Works

The intended end-to-end workflow is:

1. Academic information is imported or retrieved from available sources.
2. The backend validates and organizes the data.
3. The analytics component calculates relevant academic indicators.
4. The risk engine identifies patterns that may warrant review.
5. The dashboard presents the evidence and its historical trends.
6. GenAI generates a personalized study plan or mentor summary.
7. The intervention workflow prepares appropriate actions for human review.
8. Authorized staff record and complete interventions.
9. The system tracks follow-ups and subsequent academic indicators.
10. The dashboard summarizes progress and intervention outcomes.

This creates a continuous support cycle rather than a one-time warning system.

---

## 🤖 Role of AI in EduGuard AI

EduGuard AI combines several distinct capabilities.

| Component | Responsibility |
|---|---|
| Rule-based analytics | Identify defined patterns, such as repeated missed assignments. |
| Machine Learning | Estimate academic risk when suitable training data is available. |
| Explainable AI | Help users understand which indicators contributed to a model prediction. |
| Generative AI | Create study plans, quizzes, explanations, summaries, and message drafts. |
| Agentic AI | Coordinate defined workflows, prepare tasks, and track follow-ups. |
| Data analytics | Monitor academic trends and summarize intervention outcomes. |

These components complement one another rather than replacing one another.

**GenAI generates content. Agentic AI coordinates actions. The analytics or ML component examines academic data. The backend controls calculations, data access, and persistence.**

---


### Important Implementation Note

The prototype will initially use sample data and controlled workflows. Real ERP/LMS integrations, validated predictive models, and advanced automated workflows are future extensions unless explicitly implemented.

---

## 👥 User Roles

### Student

- View personal academic progress.
- Review attendance and subject-wise performance.
- Explore a target CGPA.
- Generate personalized study plans.
- Generate revision notes and practice quizzes.
- Track learning goals and recommended actions.

### Mentor / Faculty

- Review assigned students' relevant academic indicators.
- Examine explanations behind risk flags.
- Generate meeting briefs and supportive message drafts.
- Recommend and record academic interventions.
- Schedule follow-ups.
- Review subsequent progress.

### Department Administrator

- View authorized aggregate academic indicators.
- Monitor intervention completion.
- Review intervention outcome summaries.
- Examine appropriate fairness and model-performance reports.
- Identify areas where additional student support may be required.

Access to these views will be implemented according to the project's development stage and available time.

---


### Shared Responsibilities

Every team member is expected to:

- Use Git and GitHub for version control.
- Commit changes regularly.
- Communicate changes that affect shared interfaces.
- Test their module before integration.
- Review the overall project flow.
- Understand the problem statement and the complete architecture.
- Help prepare the demonstration and presentation.

**Collaboration rule:** Agree on database fields, API endpoints, and expected request/response formats before integrating separate modules.

---

## 📅 Project Roadmap

### Phase 1 — Working Prototype

**Target: Departmental Round — 23 October 2026**

Priorities:

- Implement the core database and fictional student records.
- Build the academic dashboard.
- Display attendance, assignments, marks and CGPA-related information.
- Implement explainable, rule-based risk indicators.
- Integrate at least one GenAI feature.
- Generate personalized study plans.
- Implement a basic mentor intervention record and follow-up status.
- Test the integrated application.

**Goal:** Demonstrate one complete journey from academic data to a risk explanation, personalized AI support, and a recorded intervention.

### Phase 2 — Enhanced Prototype

**Target: Final Round — 30 October 2026, if selected**

Potential improvements:

- Improve the GenAI assistant's grounding in verified academic data and approved course material.
- Add the Agentic AI follow-up workflow.
- Improve mentor summaries and supportive message generation.
- Add intervention outcome visualizations.
- Implement basic fairness checks using suitable demo data.
- Improve the weekly academic timeline.
- Add a simple what-if simulator.
- Strengthen role-based access and privacy controls.
- Improve testing, error handling and presentation quality.

The exact scope will depend on the stability of the initial prototype and feedback from the departmental round.

### Future Development

Longer-term possibilities include:

- Integration with an available LMS API.
- Integration with institutional ERP systems, subject to authorization.
- Predictive modelling trained on suitable historical data.
- More comprehensive fairness and model-performance evaluation.
- Additional academic planning tools.
- Expanded intervention analytics and institutional reporting.

---


## 🔐 Ethics, Privacy and Responsible AI

Lowkey is intended to support students, not label or punish them.

The project follows these design principles:

### Supportive Predictions

- Risk assessments are estimates, not certainties.
- Students should not be defined by a risk category.
- Predictions alone must not trigger punitive academic decisions.

### Human Oversight

- Mentors review sensitive intervention recommendations.
- Counseling referrals and escalations require appropriate human review.
- Generated communications can be reviewed before being sent.

### Data Privacy

- Use fictional records for the initial demonstration.
- Restrict access to authorized information.
- Avoid collecting unnecessary personal data.
- Protect API keys and other secrets.
- Provide clear information about data use and applicable consent requirements.

### Grounded Generative AI

- Generate recommendations from available and authorized information.
- Use verified institutional policies when discussing academic requirements.
- Make missing information explicit.
- Avoid inventing attendance rules, grades or academic records.
- Keep private student AI conversations separate from mentor views by default.

### Fairness and Accountability

- Evaluate potential differences in model performance across relevant groups.
- Document limitations of the data and methods.
- Investigate possible bias rather than assuming that excluding sensitive attributes eliminates it.
- Monitor whether interventions provide meaningful support.

---


## ⚠️ Current Limitations

The initial prototype has important limitations:

- It uses fictional data rather than verified institutional records.
- It may use rule-based indicators rather than a validated dropout-prediction model.
- It does not automatically connect to a real college LMS or ERP unless an authorized integration is implemented.
- GenAI-generated recommendations may contain errors and require validation.
- Demonstration intervention statistics do not establish real-world effectiveness.
- Fairness checks using synthetic data cannot establish fairness in actual student populations.

These limitations will be documented honestly during the project demonstration.

---

## 🔮 Future Scope

Potential future enhancements include:

- Authorized integration with institutional LMS and ERP platforms.
- Predictive models evaluated using appropriate historical academic outcomes.
- More comprehensive explainability and fairness monitoring.
- Grounded academic assistance using approved course materials.
- More advanced intervention scheduling and workflow automation.
- Expanded role-based dashboards and institutional reporting.
- Longitudinal evaluation of intervention outcomes.
- Improved student feedback and support mechanisms.

---
