import streamlit as st
import requests

# ---------------- CONFIG ----------------
API_URL = "http://127.0.0.1:8000/support/query"

st.set_page_config(
    page_title="Agentic Support Orchestrator",
    page_icon="🤖",
    layout="centered"
)

# ---------------- HEADER ----------------
st.markdown("## 🤖 Agentic Support Orchestrator")
st.caption(
    "AI-powered support for **Technical** and **Billing** issues"
)

st.markdown("---")

# ---------------- INPUT ----------------
ticket = st.text_area(
    "Describe your issue",
    placeholder="Example: My password reset email is not arriving today.",
    height=100
)

submit = st.button("Submit")

# ---------------- API CALL ----------------
if submit:
    if not ticket.strip():
        st.warning("Please enter a support query.")
    else:
        with st.spinner("Analyzing your issue..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"ticket": ticket},
                    timeout=30
                )

                if response.status_code != 200:
                    st.error("Backend error. Please try again later.")
                else:
                    data = response.json()

                    # ---------------- RESPONSE ----------------
                    st.success("Resolution generated")

                    st.markdown("### 📄 Resolution")

                    answer = data.get("answer", "")

                    # ---- Format steps cleanly ----
                    steps = []
                    for line in answer.split("\n"):
                        line = line.strip()
                        if line.lower().startswith("step"):
                            steps.append(line)

                    if steps:
                        for step in steps:
                            st.markdown(f"- {step}")
                    else:
                        st.write(answer)

                    # ---------------- METRICS ----------------
                    st.markdown("")

                    col1, col2 = st.columns(2)

                    with col1:
                        st.metric(
                            "Confidence",
                            f"{data.get('confidence', 0):.2f}"
                            if data.get("confidence") is not None else "N/A"
                        )

                    with col2:
                        st.metric(
                            "Escalated",
                            "No" if not data.get("escalated") else "Yes"
                        )

            except requests.exceptions.RequestException:
                st.error("Unable to connect to the backend API.")
