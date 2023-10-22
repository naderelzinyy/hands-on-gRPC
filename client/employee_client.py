
from __future__ import print_function

import logging

import grpc
import employees_pb2
import employees_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = employees_pb2_grpc.EmployeesStub(channel)
        response = stub.CreateEmployee(employees_pb2.CreateEmployeeRequest(employee=employees_pb2.Employee(
            id="99212378623",
            name="Winston Churchill",
            email="churchill1945@uk.com"
        )))
    print(f"Employee client received: {response.employee}")


if __name__ == "__main__":
    logging.basicConfig()
    run()
