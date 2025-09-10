# AI Invoice Processor

A web-based invoice management system that combines a clean Streamlit interface with a Python agent for document processing.

## Overview

This application demonstrates practical AI integration in business workflows by providing:
- Visual invoice selection and preview interface
- Automated data extraction from PDF documents
- Clean separation between UI layer and processing logic
- No external API dependencies for core functionality

## Architecture

### Components
- **Streamlit Frontend** (`app.py`): Web interface for invoice selection and results display
- **Python Agent** (`main.py`): Document processing engine with subprocess communication
- **Sample Data** (`sample_invoices/`): Demo invoice PDFs for testing

### Data Flow
1. User selects invoice from dropdown menu
2. Streamlit calls Python agent via subprocess
3. Agent processes file and returns structured data
4. Results displayed in web interface

## Features

### Invoice Management
- Upload and organize PDF invoices
- Visual file selection interface
- File size and metadata display

### Data Extraction
- Company name identification
- Invoice number parsing
- Amount and date extraction
- Structured output formatting

### User Interface
- Clean, professional layout
- Responsive two-column design
- Real-time processing feedback
- Error handling and validation

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-invoice-processor.git
   cd ai-invoice-processor
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add sample invoices**
   ```
   Create folder: sample_invoices/
   Add PDF files: sample_invoice_1.pdf, sample_invoice_2.pdf, etc.
   ```

### Running the Application

```bash
streamlit run app.py
```

Access the application at `http://localhost:8501`

## Usage

### Processing Invoices
1. Select an invoice from the dropdown menu
2. Click "Analyze with Agent" button
3. View extracted data in the results area

### Expected Output Format
```
Invoice Analysis Complete!
File: sample_invoice_1.pdf
Size: 28.0 KB
Company: TechCorp Solutions | Amount: $2,847.50 | Date: 2024-01-10
Analysis finished successfully!
```

## Project Structure

```
ai-invoice-processor/
├── app.py                 # Streamlit web interface
├── main.py               # Python agent with processing logic
├── requirements.txt      # Python dependencies
├── sample_invoices/      # Demo PDF files
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Dependencies

- `streamlit`: Web application framework
- Standard Python libraries for file processing and subprocess management

See `requirements.txt` for complete dependency list.

## Technical Implementation

### Subprocess Communication
The application uses subprocess calls to maintain clean separation between the web interface and processing logic:

```python
result = subprocess.run([
    'python', 'main.py', 'analyze_invoice', file_path
], capture_output=True, text=True, timeout=30)
```

### Error Handling
- File existence validation
- Subprocess timeout protection
- Unicode encoding management
- Graceful error messaging

### Performance Considerations
- Lightweight processing for demo purposes
- 30-second timeout protection
- Minimal memory footprint
- Fast response times

## Development Notes

### Current Implementation
- Mock data extraction based on filename patterns
- No external API dependencies
- Windows-compatible encoding handling
- Streamlined user workflow

### Future Enhancements
- Real PDF text extraction using PyPDF2 or similar libraries
- Integration with AI services for enhanced data extraction
- Database storage for processed invoices
- Batch processing capabilities
- Advanced data validation and formatting

## Troubleshooting

### Common Issues

**Unicode/Encoding Errors**
- Ensure all text output avoids special characters
- Use UTF-8 encoding where possible
- Test on target operating system

**File Path Issues**
- Verify `sample_invoices/` folder exists
- Check file permissions
- Ensure PDF files are accessible

**Subprocess Failures**
- Confirm `main.py` is in the same directory
- Test command line execution manually
- Check Python path configuration

### Testing

Test the basic functionality:
```bash
# Test agent directly
python main.py analyze_invoice sample_invoices/sample_invoice_1.pdf

# Test Streamlit interface
streamlit run app.py
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is available for educational and demonstration purposes.

## Contact

For questions or support, please open an issue in the repository.