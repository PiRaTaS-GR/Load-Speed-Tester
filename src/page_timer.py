from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from typing import Dict, List
import time

class PageLoadTimer:
    """Handles the timing of page load requests using Selenium."""
    
    def __init__(self, driver):
        self.driver = driver
        self.results: List[Dict] = []
        
    def measure_load_time(self, url: str) -> Dict:
        """Measure the load time for a single URL."""
        start_time = time.time()
        
        try:
            self.driver.get(url)
            
            WebDriverWait(self.driver, 30).until(
                lambda driver: driver.execute_script('return document.readyState') == 'complete'
            )
            
            end_time = time.time()
            load_time = end_time - start_time
            
            
            navigation_timing = self.driver.execute_script("""
                let timing = window.performance.timing;
                return {
                    'dns': timing.domainLookupEnd - timing.domainLookupStart,
                    'connection': timing.connectEnd - timing.connectStart,
                    'ttfb': timing.responseStart - timing.requestStart,
                    'dom_load': timing.domContentLoadedEventEnd - timing.navigationStart,
                    'full_load': timing.loadEventEnd - timing.navigationStart
                };
            """)
            
            return {
                'load_time': load_time,
                'metrics': navigation_timing
            }
            
        except Exception as e:
            raise Exception(f"Error loading {url}: {str(e)}")
    
    def analyze_url(self, url: str, attempts: int = 3) -> Dict:
        """Analyze a URL multiple times and collect statistics."""
        measurements = []
        
        for _ in range(attempts):
            measurement = self.measure_load_time(url)
            measurements.append(measurement)
            time.sleep(1)  
        
        
        avg_load_time = sum(m['load_time'] for m in measurements) / len(measurements)
        avg_metrics = {
            metric: sum(m['metrics'][metric] for m in measurements) / len(measurements)
            for metric in measurements[0]['metrics'].keys()
        }
        
        result = {
            'url': url,
            'timestamp': datetime.now().isoformat(),
            'average_load_time': avg_load_time,
            'min_load_time': min(m['load_time'] for m in measurements),
            'max_load_time': max(m['load_time'] for m in measurements),
            'average_metrics': avg_metrics,
            'samples': len(measurements)
        }
        
        self.results.append(result)
        return result