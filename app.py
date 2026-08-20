import io
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="ITGC Compliance & Evidence Tracker", layout="wide"
)

st.title("🛡️ ITGC Compliance & Evidence Tracker")
st.markdown(
    "An interactive GRC audit log, evidence collection, and automated reporting tool for team testing."
)

# Initialize session state for persistent testing data
if "evidence_df" not in st.session_state:
    st.session_state.evidence_df = pd.DataFrame(
        [
            {
                "Request ID": "REQ-001",
                "Control ID": "AC-1",
                "Framework": "NIST SP 800-53",
                "Description": "Access Control Policy Review",
                "Status": "Open",
                "Due Date": "2026-09-30",
            },
            {
                "Request ID": "REQ-002",
                "Control ID": "CC6.1",
                "Framework": "SOX",
                "Description": "Logical Access Restrictions",
                "Status": "In Review",
                "Due Date": "2026-10-15",
            },
            {
                "Request ID": "REQ-003",
                "Control ID": "ISO-A.9",
                "Framework": "ISO 27001",
                "Description": "User Access Management Verification",
                "Status": "Approved",
                "Due Date": "2026-08-15",
            },
        ]
    )

# Sidebar for adding new test items
st.sidebar.header("➕ Create Evidence Request")
with st.sidebar.form("audit_form"):
    req_id = st.text_input("Request ID", value="REQ-004")
    control_id = st.text_input(
        "Control ID (e.g., AC-2, CC6.2)", value="AC-2"
    )
    framework = st.selectbox(
        "Framework", ["NIST SP 800-53", "ISO 27001", "SOX", "NIST AI RMF"]
    )
    desc = st.text_area("Evidence Description")
    status = st.selectbox("Status", ["Open", "In Review", "Approved", "Rejected"])
    due_date = st.date_input("Due Date")

    submit_button = st.form_submit_button(label="Add Request")

    if submit_button:
        new_row = {
            "Request ID": req_id,
            "Control ID": control_id,
            "Framework": framework,
            "Description": desc,
            "Status": status,
            "Due Date": str(due_date),
        }
        st.session_state.evidence_df = pd.concat(
            [st.session_state.evidence_df, pd.DataFrame([new_row])],
            ignore_index=True,
        )
        st.success(f"Added {req_id} successfully!")

# Main Dashboard Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Requests", len(st.session_state.evidence_df))
col2.metric(
    "Open Items",
    len(
        st.session_state.evidence_df[
            st.session_state.evidence_df["Status"] == "Open"
        ]
    ),
)
col3.metric(
    "In Review",
    len(
        st.session_state.evidence_df[
            st.session_state.evidence_df["Status"] == "In Review"
        ]
    ),
)
col4.metric(
    "Approved",
    len(
        st.session_state.evidence_df[
            st.session_state.evidence_df["Status"] == "Approved"
        ]
    ),
)

st.markdown("---")

# Active Audit Logs Data Grid
st.subheader("📋 Active Audit Logs & Evidence Registry")
st.dataframe(st.session_state.evidence_df, use_container_width=True)

st.markdown("---")

# Report Generation & Executive Export Section
st.subheader("📊 Executive Audit Report Generation")
st.markdown(
    "Export active audit logs for external SIEM/GRC ingestion or view framework analytics."
)

col_exp1, col_exp2 = st.columns(2)

with col_exp1:
    # CSV Report Export Button
    csv_data = st.session_state.evidence_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Full Audit Log (CSV)",
        data=csv_data,
        file_name="itgc_compliance_audit_report.csv",
        mime="text/csv",
    )

with col_exp2:
    show_summary = st.checkbox("Toggle Executive Analytics View")

if show_summary:
    st.markdown("### Framework Breakdown Analytics")
    framework_breakdown = (
        st.session_state.evidence_df["Framework"].value_counts().reset_index()
    )
    framework_breakdown.columns = ["Framework", "Total Requests"]
    st.bar_chart(framework_breakdown.set_index("Framework"))
    st.info(
        "Report metrics calculated dynamically from live session state registry."
    )
