from importlib.metadata import version, metadata

PROGRAM_NAME = "devator"
PACKAGE_NAME = "devator"
devator_metadata = metadata(PACKAGE_NAME)

PROGRAM_DESCRIPTION = devator_metadata["Summary"]
PROGRAM_LICENSE = devator_metadata["LICENSE"]
PROGRAM_VERSION = version(PACKAGE_NAME)
