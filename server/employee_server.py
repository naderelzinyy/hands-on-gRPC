from concurrent import futures
import logging

import grpc

import employees_pb2
import employees_pb2_grpc


class Employees(employees_pb2_grpc.EmployeesServicer):

    def GetEmployee(self, request, context):
        """Gets employee data."""
        return employees_pb2.GetEmployeeResponse(
            employee=request.employee
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
            employee=request.employee
        )

    def deleteEmployee(self, request, context):
        """Gets employee data."""
        return employees_pb2.DeleteEmployeeResponse(
            employee=request.employee
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
