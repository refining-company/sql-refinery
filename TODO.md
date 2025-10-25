Cleanup

1. Update `__str__` and `__repr__` in model to be aligned with src.code
2. Review variations to use model abstractions
3. `__str__` and `__repr__` in variations

Next steps

1. Make replacement in frontend comply with formatting
2. Make replacement in frontend comply with local column names
3. Make test snapshots configurable so there is a config file (e.g. `variations.config.json`) that tracks which
   snapshots are used in assert, and which are just captured (maybe using wildcards on filenames)
