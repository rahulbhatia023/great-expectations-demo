import sys

from great_expectations.core.batch import BatchRequest
from great_expectations.profile.user_configurable_profiler import (
    UserConfigurableProfiler,
)

from great_expectations import DataContext

if __name__ == "__main__":
    context = DataContext()

    batch_request_source = {
        "datasource_name": "filesystem_pandas_demo_datasource",
        "data_connector_name": "filesystem_pandas_demo_data_connector",
        "data_asset_name": "yellow_tripdata_sample_2019-01.csv",
    }

    validator = context.get_validator(
        batch_request=BatchRequest(**batch_request_source),
    )

    profiler = UserConfigurableProfiler(profile_dataset=validator)
    profiler.build_suite()

    # Review and save our Expectation Suite
    validator.save_expectation_suite()

    # Build Data Docs
    context.build_data_docs()

    # Set up and run a Simple Checkpoint for ad hoc validation of our data
    result = context.run_checkpoint(checkpoint_name="checkpoint_demo")

    # Open Data Docs
    context.open_data_docs()

    if not result["success"]:
        print("Validation failed!")
        sys.exit(1)

    print("Validation succeeded!")
    sys.exit(0)
