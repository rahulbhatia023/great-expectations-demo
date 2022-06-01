from great_expectations import DataContext

if __name__ == "__main__":
    context = DataContext()

    # --- VALIDATE DATA --- #
    context.run_checkpoint(checkpoint_name="checkpoint_postgres_demo")

    # --- CREATE DATA DOCS --- #
    context.build_data_docs()
    context.open_data_docs()
