import streamlit as st

# HTML + JavaScript to trigger vibration
vibration_script = """
<script>
function vibratePhone() {
    if ("vibrate" in navigator) {
        // Vibration pattern: vibrate for 500ms
        navigator.vibrate(500);
    } else {
        alert('Vibration not supported on this device');
    }
}
</script>
<button onclick="vibratePhone()" class="btn btn-primary">Vibrate Phone</button>
"""

def main():
    st.title('Streamlit Vibration App')
    
    # Display the custom HTML with the vibration button
    st.markdown(vibration_script, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
