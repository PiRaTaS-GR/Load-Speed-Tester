from webdriver_manager import create_driver
from page_timer import PageLoadTimer
from report_generator import ReportGenerator

def main():
    
    driver = create_driver()
    
    try:
        
        timer = PageLoadTimer(driver)
        
       
        urls = [
            'https://www.example.com',
            'https://www.python.org',
            'https://www.github.com'
        ]
        
        print("Starting page load speed tests...\n")
        
        
        for url in urls:
            try:
                print(f"Testing {url}...")
                result = timer.analyze_url(url)
                print(f"Average load time: {result['average_load_time']:.3f} seconds")
                print(f"TTFB: {result['average_metrics']['ttfb']:.3f} ms")
                print(f"DOM Load: {result['average_metrics']['dom_load']:.3f} ms\n")
            except Exception as e:
                print(f"Error: {e}\n")
        

        report_generator = ReportGenerator()
        
        
        text_report = report_generator.generate_text_report(timer.results)
        print(text_report)
        
        
        report_generator.save_json_report(timer.results, 'load_time_results.json')
        print("\nJSON report has been saved to 'load_time_results.json'")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    main()