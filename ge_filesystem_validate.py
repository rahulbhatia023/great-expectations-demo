import sys

from great_expectations.core.batch import BatchRequest
from great_expectations.profile.user_configurable_profiler import (
    UserConfigurableProfiler,
)

from great_expectations import DataContext

if __name__ == "__main__":
    context = DataContext()

    # --- VALIDATE DATA --- #

    result = context.run_checkpoint(checkpoint_name="checkpoint_expectation_suite_demo")

    # --- CREATE DATA DOCS --- #

    context.build_data_docs()
    context.open_data_docs()

    if not result["success"]:
        print("Validation failed!")
        sys.exit(1)

    print("Validation succeeded!")
    sys.exit(0)
