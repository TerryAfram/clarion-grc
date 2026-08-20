# clarion-grc

ITGC Compliance & Evidence Tracker
An enterprise-ready, multi-framework ITGC compliance audit log, evidence collection, and automated reporting tool built with Python, Streamlit, and FastAPI. Designed for seamless human testing and programmatic system-to-system integrations.

Architecture & Components
 Streamlit Dashboard (⁠app.py⁠): An interactive user interface for human auditors to track compliance evidence, view dynamic metric cards, and generate/download CSV audit reports and framework analytics.
 FastAPI Backend (⁠api.py⁠): A programmatic REST API service allowing external enterprise platforms, SIEM tools, and local GRC pipelines to push and pull compliance data.
 Render Blueprint (⁠render.yaml⁠): Infrastructure-as-Code configuration enabling automated, simultaneous zero-downtime deployment of both the UI and API on Render.
