import streamlit as st
import subprocess
import os

st.title("GPT‑Engineer Web Interface")
st.markdown("""
This app wraps GPT‑Engineer into a web interface.
Enter your project prompt below and click "Generate Code".
Make sure GPT‑Engineer is installed and available in your environment.
""")

# Input field for the project prompt
prompt = st.text_area("Enter your project prompt", height=150)

if st.button("Generate Code"):
    if not prompt.strip():
        st.error("Please enter a prompt.")
    else:
        # Create a directory for the generated project (if it doesn't already exist)
        project_dir = "generated_project"
        os.makedirs(project_dir, exist_ok=True)

        # Save the prompt into a file (as expected by GPT‑Engineer)
        prompt_file = os.path.join(project_dir, "prompt")
        with open(prompt_file, "w") as f:
            f.write(prompt)

        st.info("Running GPT‑Engineer... This may take a while.")

        # Call GPT‑Engineer via its CLI; adjust the command as needed
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
