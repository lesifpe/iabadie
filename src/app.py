import streamlit as st
from search import search
from generate_response import generate_natural_response

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
        response = generate_natural_response(user_input, best_result["answer"])

        with st.chat_message("assistant"):
            st.markdown(response)
            if best_result.get("sourceList"):
                st.markdown("**Links úteis:**")
                for source in best_result["sourceList"]:
                    st.markdown(f"- [{source['title']}]({source['url']})")
            with st.expander("Ver fonte"):
                st.markdown(f"**Pergunta similar encontrada:** {best_result['question']}")
                st.markdown(f"**Resposta original:** {best_result['answer']}")
                st.markdown(f"**Confiança:** {int(best_result['score'] * 100)}%")

        st.session_state["message_list"].append({
            "role": "assistant",
            "content": response
        })