import streamlit as st
from llama_cpp import Llama

# Initialize Llama with model path and configuration
llm = Llama(
    model_path="finance-llm.Q8_0.gguf",  # Path to your model file
    n_ctx=2048,        # Max sequence length to use
    n_threads=8,       # Number of CPU threads to use (adjust based on performance)
    n_gpu_layers=0    # Number of layers to offload to GPU (if available, adjust based on performance)
)
# Function for generating financial advice
def generate_advice(prompt, max_tokens=512, stop=["</s>"], echo=False):
    response = llm(
        prompt,
        max_tokens=max_tokens,
        stop=stop,
        echo=echo
    )
    output_text = response["choices"][0]["text"]
    return output_text.strip()
# Streamlit UI
def main():
    st.title("Financial Advice Generator")

    st.header("Get Financial Advice")
    user_input = st.text_area("Enter your financial query or concern:")
    if st.button("Get Advice"):
        if user_input:
            advice_output = generate_advice(user_input)
            st.subheader("Financial Advice:")
            st.write(advice_output)
        else:
            st.warning("Please enter your query.")

if __name__ == "__main__":
    main()
