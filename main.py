from etl_job import run_etl
from agent import fix_etl_script, read_log
from utils import log_error
import traceback

def run_pipeline():
    try:
        print("Running ETL job...")
        run_etl()
        print("ETL job completed successfully.")
    except Exception as e:
        error_log = traceback.format_exc()
        print("Job failed! Logging error...")
        log_error(error_log)

        # Read current ETL code
        with open("etl_job.py", "r") as f:
            etl_code = f.read()

        print("Calling LLM agent to fix the issue...")
        fixed_code = fix_etl_script(error_log, etl_code)

        # Write fixed code back
        with open("etl_job.py", "w") as f:
            f.write(fixed_code)

        print("Re-running with fixed ETL code...")
        run_pipeline()  # Try again

if __name__ == "__main__":
    run_pipeline()
