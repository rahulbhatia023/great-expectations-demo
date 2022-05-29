import sys

from great_expectations.core.batch import BatchRequest
from great_expectations.profile.user_configurable_profiler import (
    UserConfigurableProfiler,
)

from great_expectations import DataContext

if __name__ == "__main__":
    context = DataContext()

    # --- CREATE EXPECTATIONS --- #

    batch_request_source = BatchRequest(
        datasource_name="filesystem_pandas_datasource_demo",
        data_connector_name="filesystem_pandas_data_connector_demo",
        data_asset_name="yellow_tripdata_sample_2019-01.csv",
    )

    validator = context.get_validator(
        batch_request=batch_request_source,
        create_expectation_suite_with_name="expectation_suite_demo",
    )

    profiler = UserConfigurableProfiler(profile_dataset=validator)
    profiler.build_suite()

    validator.save_expectation_suite(
        "great_expectations/expectations/expectation_suite_demo.json"
    )

    # --- VALIDATE DATA --- #

    result = context.run_checkpoint(checkpoint_name="checkpoint_demo")

    # --- CREATE DATA DOCS --- #

    context.build_data_docs()
    context.open_data_docs()

    if not result["success"]:
        print("Validation failed!")
        sys.exit(1)

    print("Validation succeeded!")
    sys.exit(0)
