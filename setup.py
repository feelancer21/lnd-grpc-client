from setuptools import setup, find_packages

setup(
    name="fl21-lnd-grpc-client",
    version="0.6.0",
    packages=find_packages(include=["lndgrpc*"], exclude=["lndgrpc/googleapis/*"])
)
