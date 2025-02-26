import streamlit as st
import subprocess
import os

st.title("GPT‑Engineer Web Interface")

st.markdown("""
This app wraps GPT‑Engineer. Enter your prompt below and the app will run GPT‑Engineer to generate a codebase.
Make sure GPT‑Engineer is installed and accessible in your environment.
""")

# User input for the project prompt
prompt = st.text_area("Enter your project prompt", height=150)

if st.button("Generate Code"):
    if not prompt.strip():
        st.error("Please enter a prompt.")
    else:
        # Create a directory for the project (if it doesn't exist)
        project_dir = "generated_project"
        os.makedirs(project_dir, exist_ok=True)
        
        # Save the prompt into a file named "prompt" inside the project directory
        prompt_file = os.path.join(project_dir, "prompt")
        with open(prompt_file, "w") as f:
            f.write(prompt)
        
        st.info("Running GPT‑Engineer... This might take a while.")
        
        # Call GPT‑Engineer via its command-line interface.
        # Adjust the command 'gpte' if your installation uses a different command.
        try:
            result = subprocess.run(
                ["gpte", project_dir],
                capture_output=True,
                text=True,
                check=True,
            )
            st.success("Code generation complete!")
            st.subheader("GPT‑Engineer Output:")
            st.text_area("Output", value=result.stdout, height=300)
        except subprocess.CalledProcessError as e:
            st.error("An error occurred while generating the code.")
            st.text_area("Error Details", value=e.stderr, height=300)
