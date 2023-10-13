from setuptools import setup, find_packages

setup(
    name="lnd-grpc-client",
    version="0.5.2",
    packages=find_packages(include=["lndgrpc*"], exclude=["lndgrpc/googleapis/*"])
)
