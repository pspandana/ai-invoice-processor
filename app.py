import streamlit as st
import os
import subprocess

st.title("🧾 AI Invoice Processor")

INVOICE_FOLDER = "sample_invoices/"
if os.path.exists(INVOICE_FOLDER):
    invoice_files = [f for f in os.listdir(INVOICE_FOLDER) if f.endswith('.pdf')]
else:
    st.error("Please create 'sample_invoices' folder")
    invoice_files = []

if invoice_files:
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("📋 Invoice List")
        selected = st.selectbox("Select Invoice:", invoice_files)
    
    with col2:
        if selected:
            st.subheader(f"📄 {selected}")
            
            if st.button("🤖 Analyze with Agent"):
                with st.spinner("Your agent is processing..."):
                    # Call your Python agent via subprocess
                    file_path = os.path.join(INVOICE_FOLDER, selected)
                    
                    try:
                        # Run your agent with the invoice file
                        import sys

                        result = subprocess.run([
                            sys.executable, 'main.py', 'analyze_invoice', file_path
                        ], capture_output=True, text=True, timeout=30)
                        
                        if result.returncode == 0:
                            st.success("✅ Analysis Complete!")
                            st.text_area("Agent Results:", result.stdout, height=250)
                        else:
                            st.error("❌ Agent Error:")
                            st.text(result.stderr)
                            
                    except subprocess.TimeoutExpired:
                        st.error("⏰ Agent timeout - processing took too long")
                    except Exception as e:
                        st.error(f"❌ Error running agent: {e}")