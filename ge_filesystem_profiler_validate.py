from great_expectations.core.batch import BatchRequest
from great_expectations.profile.user_configurable_profiler import (
    UserConfigurableProfiler,
)

from great_expectations import DataContext

context = DataContext()

# --- CREATE EXPECTATIONS --- #
context.create_expectation_suite(
    expectation_suite_name="expectation_suite_profiler_demo",
    overwrite_existing=True,
)

validator = context.get_validator(
    batch_request=BatchRequest(
        datasource_name="filesystem_pandas_datasource_demo",
        data_connector_name="filesystem_pandas_data_connector_demo",
        data_asset_name="yellow_tripdata_sample_2019-01.csv",
    ),
    expectation_suite_name="expectation_suite_profiler_demo",
)

profiler = UserConfigurableProfiler(profile_dataset=validator)
profiler.build_suite()

validator.save_expectation_suite()

# --- VALIDATE DATA --- #
context.run_checkpoint(checkpoint_name="checkpoint_filesystem_profiler_demo")

# --- CREATE DATA DOCS --- #
context.build_data_docs()
context.open_data_docs()
