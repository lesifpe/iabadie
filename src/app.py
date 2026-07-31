import streamlit as st
from search import search

st.set_page_config(
    page_title="IAbadie - A IA para responder dúvidas sobre o curso de ADS",
    page_icon="🎓",
)

st.title("IAbadie - A IA para responder dúvidas sobre o curso de ADS")
st.caption("Tire suas dúvidas sobre o curso")

if "message_list" not in st.session_state:
    st.session_state["message_list"] = []

for message in st.session_state["message_list"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Digite sua pergunta...")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state["message_list"].append({
        "role": "user",
        "content": user_input
    })

    result_list = search(user_input)

    if not result_list:
        response = "Ainda não há resposta relevante para essa pergunta."

    else:
        best_result = result_list[0]
        confidence = int(best_result["score"] * 100)

        source_list = best_result.get("sourceList", [])

        sources_text = ""
        if source_list:
            source_line_list = [
                f"- [{source['title']}]({source['url']})"
                for source in source_list
            ]
            sources_text = "\n\n**Links úteis:**\n" + "\n".join(source_line_list)

        response = f"""
**Pergunta similar encontrada:**
_{best_result['question']}_

**Resposta:**
{best_result['answer']}

**Confiança:** {confidence}%
{sources_text}

        """

        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state["message_list"].append({
            "role": "assistant",
            "content": response
        })

