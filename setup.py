from setuptools import setup

setup(
    name="openlimit_lite",
    description="Rate limiter for the OpenAI API",
    version="v0.3.0",
    packages=["openlimit_lite", "openlimit_lite.utilities", "openlimit_lite.buckets"],
    python_requires=">=3",
    url="https://github.com/dragoneyeAI/openlimit-lite",
    author="alexliao, shobrook",
    author_email="support@dragoneye.ai, shobrookj@gmail.com",
    install_requires=["tiktoken"],
    keywords=[
        "openai",
        "rate-limit",
        "limit",
        "api",
        "request",
        "token",
        "leaky-bucket",
        "gcra",
        "asyncio",
    ],
)
