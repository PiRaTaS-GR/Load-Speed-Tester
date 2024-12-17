# Page Load Speed Tester

A Python-based tool for measuring and analyzing webpage load times using Selenium WebDriver. This tool provides accurate, real-world performance measurements and follows software engineering best practices.

## Features

- Accurate page load timing using Selenium WebDriver
- Detailed performance metrics including:
  - Time to First Byte (TTFB)
  - DNS lookup time
  - Connection establishment time
  - DOM load time
  - Full page load time
- Multiple measurement samples for statistical accuracy
- Both human-readable and JSON reports
- Headless browser testing
- Clean and modular code structure

## Project Structure

```
src/
├── webdriver_manager.py  # WebDriver configuration
├── page_timer.py         # Core timing functionality
├── report_generator.py   # Report generation utilities
└── main.py              # Main application entry point
```

## Components

1. **WebDriverManager**: Handles browser configuration
   - Creates and configures Chrome WebDriver
   - Sets up headless mode for automated testing

2. **PageLoadTimer**: Core timing functionality
   - Measures detailed page load metrics
   - Collects multiple samples
   - Uses JavaScript Performance API
   - Calculates statistical measures

3. **ReportGenerator**: Report generation
   - Creates detailed text reports
   - Generates JSON reports
   - Includes timestamps and metrics

## Requirements

- Python 3.x
- Selenium WebDriver
- Chrome/Chromium browser

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python src/main.py
```

The program will:
1. Initialize a headless Chrome browser
2. Test each URL multiple times
3. Display real-time progress
4. Generate detailed reports

## Output

Two types of output are generated:
1. Console-based text report with human-readable results
2. JSON file (`load_time_results.json`) containing detailed metrics

## Best Practices Implemented

1. **Modular Design**
   - Separate modules for distinct responsibilities
   - Clean interfaces between components
   - Easy to extend and maintain

2. **Error Handling**
   - Graceful error management
   - Resource cleanup (WebDriver)
   - Detailed error reporting

3. **Clean Code**
   - Type hints for better code understanding
   - Comprehensive documentation
   - Consistent coding style

4. **Performance Measurement**
   - Multiple samples for accuracy
   - Detailed timing metrics
   - Browser-based performance API usage

## Limitations

- Requires Chrome/Chromium browser
- Network-dependent results
- Single-threaded execution
- Basic authentication only

## Future Improvements

- Add support for multiple browsers
- Implement parallel testing
- Add custom HTTP headers support
- Create HTML report generation
- Add configuration file support
- Include visual metrics (Speed Index, First Contentful Paint)