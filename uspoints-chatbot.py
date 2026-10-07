import streamlit as st

# Page configuration
st.set_page_config(
    page_title="NTU-USP USPoints Assistant",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 NTU-USP USPoints Assistant")
st.caption("Ask questions about NTU-USP guidelines, point requirements, and accumulation rules.")

# Knowledge base extracted directly from official NTU-USP Guidelines (as of June 2026)
KNOWLEDGE_BASE = {
    "what_are_uspoints": (
        "USPoints are a point system designed to reward NTU-USP students for involvement in "
        "relevant NTU-USP and NTU-USP Club events/activities. Note that USPoints ≠ NTU ECA points, "
        "and the system is subject to change. USPoints serve as consideration for priority in: "
        "enrichment programmes, overseas opportunities, NTU-USP electives, study abroad slots, "
        "recommendations, and CresPion Halls Priority Rec List."
    ),
    "annual_requirements": (
        "In Year 1 & 2: Accumulate at least 5 USPoints per year.\n"
        "By end of Year 2: Accumulate at least 4 Ambassador USPoints.\n"
        "Failing to meet these requirements subjects students to review by EC/USPO, "
        "which may include restricting Club privileges or deprioritising Study Abroad."
    ),
    "categories_and_points": (
        "- **NTU-USP Club Activities**: 1 to 8 points\n"
        "  • Top 4 Exco (Pres, VP, Gen Sec, Fin Sec): 8 pts\n"
        "  • Exco Director: 7 pts\n"
        "  • Subcommittee Member: Up to 4 pts (All Year 1s must join at least 1 subcomm)\n"
        "  • Band Manager: 2 pts / Band Member: Up to 1.5 pts\n\n"
        "- **Ad-hoc Events (FOP, USPresents, Ground Up, Elections)**:\n"
        "  • Top 4 / Chairperson: 3 pts per event\n"
        "  • Main Comm Member: 2 pts per event\n"
        "  • Subcomm Member: 1 pt per event\n\n"
        "- **Enrichment, Formal & Milestone Events**:\n"
        "  • Organising Committee (Formal): 2 pts per event\n"
        "  • Organising Committee (Milestone): 2 pts (Main) / 1 pt (Sub)\n"
        "  • Participation in Formal Events: 1 pt per event\n\n"
        "- **Ambassador USPoints** (Cap of 3 pts/year calculated towards total):\n"
        "  • Outreach Ambassador (Admissions Tea, Buddy Tea, Open House): 1 pt per event\n"
        "  • Interview / Campus Visit Ambassador: 0.25 pts per event\n"
        "  • JC Outreach Ambassador: $30 reimbursement (0 pts)"
    ),
    "crespion_rec_list": (
        "Accumulate ≥10 USPoints in the AY AND participate in ≥1 CresPion Hall Sub/Main Committee "
        "to be recommended for equal placement priority for CresPion hall stay (Category 2)."
    )
}

# Chat history initialization
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hello! I am your NTU-USP USPoints Assistant. Ask me anything about earning USPoints, requirements, or hall priority!"}
    ]

# Display chat history
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

# User query input
if prompt := st.chat_input("Ask a question about USPoints..."):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    prompt_lower = prompt.lower()
    response = ""

    if "requirement" in prompt_lower or "year" in prompt_lower or "minimum" in prompt_lower:
        response = f"**Annual Requirements:**\n\n{KNOWLEDGE_BASE['annual_requirements']}"
    elif "crespion" in prompt_lower or "hall" in prompt_lower or "rec list" in prompt_lower:
        response = f"**CresPion Hall Priority Rules:**\n\n{KNOWLEDGE_BASE['crespion_rec_list']}"
    elif "category" in prompt_lower or "point" in prompt_lower or "how many" in prompt_lower or "exco" in prompt_lower or "ambassador" in prompt_lower:
        response = f"**USPoints Categories & Earning Rates:**\n\n{KNOWLEDGE_BASE['categories_and_points']}"
    elif "what" in prompt_lower or "uspoints" in prompt_lower or "about" in prompt_lower:
        response = f"**Overview of USPoints:**\n\n{KNOWLEDGE_BASE['what_are_uspoints']}"
    else:
        response = (
            "I can answer questions regarding:\n"
            "- **Annual Requirements** (Year 1/2 points & ambassador caps)\n"
            "- **Earning Categories** (Exco, Subcommittees, Ad-hoc events, Ambassador roles)\n"
            "- **CresPion Hall Priority Rec List**\n\n"
            "Please try rephrasing your question or asking about one of these topics!"
        )

    st.session_state["messages"].append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
