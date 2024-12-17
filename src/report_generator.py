import json
from typing import List, Dict
from datetime import datetime

class ReportGenerator:
    """Handles the generation of load time reports."""
    
    @staticmethod
    def generate_text_report(results: List[Dict]) -> str:
        """Generate a human-readable text report."""
        report = []
        report.append("=== Page Load Speed Test Report ===")
        report.append(f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        for result in results:
            report.append(f"URL: {result['url']}")
            report.append(f"Timestamp: {result['timestamp']}")
            report.append(f"Average Load Time: {result['average_load_time']:.3f} seconds")
            report.append(f"Min Load Time: {result['min_load_time']:.3f} seconds")
            report.append(f"Max Load Time: {result['max_load_time']:.3f} seconds")
            report.append("\nDetailed Metrics (averages):")
            for metric, value in result['average_metrics'].items():
                report.append(f"  {metric}: {value:.3f} ms")
            report.append(f"Number of samples: {result['samples']}\n")
        
        return "\n".join(report)
    
    @staticmethod
    def save_json_report(results: List[Dict], filename: str):
        """Save results as JSON file."""
        with open(filename, 'w') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'results': results
            }, f, indent=2)