# Clara AI Automation Pipeline

Assignment Objective

Build a zero-cost automation pipeline that converts demo call transcripts into structured account configuration and generates a Retell agent draft. 

The system must also update the configuration when onboarding information is received and maintain version history (v1 → v2).

## Overview

This project implements a simple automation pipeline that converts unstructured customer conversations (demo calls and onboarding calls) into structured operational configurations for an AI voice assistant.

The goal is to simulate how Clara Answers prepares and updates AI agents for service businesses based on information gathered during sales and onboarding calls.

The system processes transcripts, extracts key operational details, generates an initial agent configuration, and later updates the configuration when additional onboarding information becomes available.

---

## Problem Context

Service companies such as fire protection contractors, HVAC providers, or electrical service companies receive many incoming calls. These calls can include:

* Emergency requests (example: sprinkler leak)
* Non-emergency service requests
* Inspection scheduling
* After-hours support calls

Clara Answers automates this call handling using AI voice agents.
However, every business has slightly different operational rules such as:

* business hours
* emergency definitions
* routing rules
* escalation paths

This project demonstrates how those rules can be extracted from conversations and converted into structured AI agent configurations.

---

## System Architecture

The pipeline contains two main stages.

### Pipeline A — Demo Call → Initial Agent Configuration

Input:
Demo call transcript

Processing:

1. Extract operational information from transcript
2. Create structured account configuration (Account Memo JSON)
3. Generate a preliminary AI agent configuration
4. Store results as version **v1**

Output:

* Account memo (structured JSON)
* Retell agent draft specification

---

### Pipeline B — Onboarding Call → Configuration Update

Input:
Onboarding call transcript

Processing:

1. Load existing account configuration (v1)
2. Apply onboarding updates
3. Generate updated configuration (v2)
4. Record the changes between versions

Output:

* Updated account memo
* Version 2 agent configuration
* Change log documenting modifications

---

## Project Structure

```
clara-ai-assignment
│
├── dataset
│   ├── demo_call_1.txt
│   └── onboarding_call_1.txt
│
├── scripts
│   ├── extract_demo.py
│   ├── generate_agent.py
│   └── update_agent.py
│
├── outputs
│   └── accounts
│       └── account_001
│           ├── v1
│           │   ├── memo.json
│           │   └── agent_spec.json
│           │
│           └── v2
│               ├── memo.json
│               └── changes.md
│
└── README.md
```

---

## Data Model

### Account Memo

The account memo stores structured operational rules extracted from transcripts.

Key fields include:

* account_id
* company_name
* business_hours
* services_supported
* emergency_definition
* emergency_routing_rules
* questions_or_unknowns

This structure allows the system to translate conversational information into machine-readable configuration data.

---

### Agent Specification

The agent specification represents a draft configuration for a voice assistant.

The configuration includes:

* agent name
* voice style
* system prompt
* call handling flows

Two flows are defined:

1. **Business hours flow**
2. **After hours flow**

This ensures the agent behaves correctly depending on the time and call type.

---

## Versioning Strategy

The system maintains configuration history.

| Version | Source          | Purpose                                             |
| ------- | --------------- | --------------------------------------------------- |
| v1      | Demo call       | Initial assumptions based on exploratory discussion |
| v2      | Onboarding call | Finalized operational configuration                 |

A change log records all updates made between versions to ensure traceability.

---

## How to Run the Pipeline

### Step 1 — Generate Initial Configuration

Run:

```
python scripts/extract_demo.py
```

This extracts information from the demo transcript and creates the account memo.

---

### Step 2 — Generate Agent Draft

Run:

```
python scripts/generate_agent.py
```

This generates the initial AI agent configuration (v1).

---

### Step 3 — Apply Onboarding Updates

Run:

```
python scripts/update_agent.py
```

This updates the configuration using onboarding information and produces version v2.

---

## Outputs

All generated artifacts are stored under:

```
outputs/accounts/<account_id>/
```

Artifacts include:

* v1 memo
* v1 agent specification
* v2 memo
* change log

---

## Design Decisions

The system uses **simple rule-based extraction** rather than external LLM APIs.
This ensures the pipeline remains fully reproducible and complies with the zero-cost constraint.

JSON was chosen as the primary data format because it:

* is human readable
* is easy to version
* integrates easily with APIs and automation tools

---

## Limitations

This prototype focuses on demonstrating the automation concept rather than production-level NLP extraction.

Possible improvements include:

* more advanced transcript parsing
* automatic schema validation
* integration with workflow orchestrators like n8n
* automated diff visualization between versions

---

## Future Improvements

If extended further, this system could evolve into a production-ready onboarding automation platform by adding:

* database storage
* API endpoints
* integration with Retell agent creation APIs
* automated task tracking
* UI dashboard for account configuration management

---

## Author

A.Jaswanth
B.Tech CSE
VIT-AP University
