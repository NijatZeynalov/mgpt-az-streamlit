import streamlit as st
import time
from modeling.model_inference import generate_response
def main():
    st.title("mGPT - Azərbaycanca 🇦🇿")

    # Input text
    user_input = st.text_input("", placeholder="Davamının yazılmasını istədiyiniz mətni daxil edin...", key="input")

    if st.button("Tamamla"):
        with st.spinner("Mətniniz tamamlanır..."):
            if len(user_input) > 0:
                text = generate_response(user_input)
            st.markdown(f'<div id="animated-text">{text}</div>', unsafe_allow_html=True)
            st.markdown(
                """
                <style>
                    #animated-text {
                        white-space: pre-wrap;
                        overflow: hidden;
                        border-right: 1px solid;
                        font-size: 24px;
                        width: fit-content;
                        animation: typing 2s steps(40, end);
                    }

                    @keyframes typing {
                        from {
                            width: 0;
                        }
                        to {
                            width: 100%;
                        }
                    }
                </style>
                """,
                unsafe_allow_html=True,
            )


if __name__ == "__main__":
    main()










