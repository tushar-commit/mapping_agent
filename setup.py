from setuptools import setup, find_packages

setup(
    name="sfn-mapping-agent",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai",
        "pandas",
        "streamlit",
        "python-dotenv",
        "sfn-blueprint"
    ],
    author="StepFN AI",
    description="A mapping agent for data column categorization and mapping",
    python_requires=">=3.8",
) 