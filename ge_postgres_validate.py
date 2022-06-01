import sys

from great_expectations import DataContext

if __name__ == "__main__":
    context = DataContext()

    # --- VALIDATE DATA --- #

    result = context.run_checkpoint(checkpoint_name="checkpoint_postgres_demo")

    # --- CREATE DATA DOCS --- #

    context.build_data_docs()
    context.open_data_docs()

    if not result["success"]:
        print("Validation failed!")
        sys.exit(1)

    print("Validation succeeded!")
    sys.exit(0)
