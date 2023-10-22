from concurrent import futures
import logging

import grpc

import employees_pb2
import employees_pb2_grpc


class Employees(employees_pb2_grpc.EmployeesServicer):

    def GetEmployee(self, request, context):
        """Gets employee data."""
        return employees_pb2.GetEmployeeResponse(
            employee=[employees_pb2.Employee(
                id="99212378623",
                name="Winston Churchill",
                email="churchill1945@uk.com"
            )]
        )

    def GetEmployeeById(self, request, context):
        """Gets employee data."""
        return employees_pb2.GetEmployeeByIdResponse()

    def CreateEmployee(self, request, context):
        """Gets employee data."""
        return employees_pb2.CreateEmployeeResponse(
            employee=request.employee
        )

    def updateEmployee(self, request, context):
        """Gets employee data."""
        return employees_pb2.UpdateEmployeeResponse(
            employee=employees_pb2.Employee(
                id="99212378623",
                name="Winston Churchill",
                email="churchill1949@uk.com"
            )
        )

    def deleteEmployee(self, request, context):
        """Gets employee data."""
        return employees_pb2.DeleteEmployeeResponse(
            employee=employees_pb2.Employee(
                id="99212378623",
                name="Winston Churchill",
                email="churchill1945@uk.com"
            )
        )


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    employees_pb2_grpc.add_EmployeesServicer_to_server(Employees(), server)
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    print(f"Server started, listening on {port}")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
