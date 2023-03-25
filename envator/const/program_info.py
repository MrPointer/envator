from importlib.metadata import version, metadata

PROGRAM_NAME = "envator"
PACKAGE_NAME = "envator"
envator_metadata = metadata(PACKAGE_NAME)

PROGRAM_DESCRIPTION = envator_metadata["Summary"]
PROGRAM_LICENSE = envator_metadata["LICENSE"]
PROGRAM_VERSION = version(PACKAGE_NAME)
