# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import employees_pb2 as employees__pb2


class EmployeesStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetEmployee = channel.unary_unary(
                '/employees.Employees/GetEmployee',
                request_serializer=employees__pb2.GetEmployeeRequest.SerializeToString,
                response_deserializer=employees__pb2.GetEmployeeResponse.FromString,
                )
        self.GetEmployeeById = channel.unary_unary(
                '/employees.Employees/GetEmployeeById',
                request_serializer=employees__pb2.GetEmployeeByIdRequest.SerializeToString,
                response_deserializer=employees__pb2.GetEmployeeByIdResponse.FromString,
                )
        self.CreateEmployee = channel.unary_unary(
                '/employees.Employees/CreateEmployee',
                request_serializer=employees__pb2.CreateEmployeeRequest.SerializeToString,
                response_deserializer=employees__pb2.CreateEmployeeResponse.FromString,
                )
        self.updateEmployee = channel.unary_unary(
                '/employees.Employees/updateEmployee',
                request_serializer=employees__pb2.UpdateEmployeeRequest.SerializeToString,
                response_deserializer=employees__pb2.UpdateEmployeeResponse.FromString,
                )
        self.deleteEmployee = channel.unary_unary(
                '/employees.Employees/deleteEmployee',
                request_serializer=employees__pb2.DeleteEmployeeRequest.SerializeToString,
                response_deserializer=employees__pb2.DeleteEmployeeResponse.FromString,
                )


class EmployeesServicer(object):
    """The greeting service definition.
    """

    def GetEmployee(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEmployeeById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateEmployee(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateEmployee(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteEmployee(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EmployeesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetEmployee': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEmployee,
                    request_deserializer=employees__pb2.GetEmployeeRequest.FromString,
                    response_serializer=employees__pb2.GetEmployeeResponse.SerializeToString,
            ),
            'GetEmployeeById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEmployeeById,
                    request_deserializer=employees__pb2.GetEmployeeByIdRequest.FromString,
                    response_serializer=employees__pb2.GetEmployeeByIdResponse.SerializeToString,
            ),
            'CreateEmployee': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateEmployee,
                    request_deserializer=employees__pb2.CreateEmployeeRequest.FromString,
                    response_serializer=employees__pb2.CreateEmployeeResponse.SerializeToString,
            ),
            'updateEmployee': grpc.unary_unary_rpc_method_handler(
                    servicer.updateEmployee,
                    request_deserializer=employees__pb2.UpdateEmployeeRequest.FromString,
                    response_serializer=employees__pb2.UpdateEmployeeResponse.SerializeToString,
            ),
            'deleteEmployee': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteEmployee,
                    request_deserializer=employees__pb2.DeleteEmployeeRequest.FromString,
                    response_serializer=employees__pb2.DeleteEmployeeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'employees.Employees', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Employees(object):
    """The greeting service definition.
    """

    @staticmethod
    def GetEmployee(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/employees.Employees/GetEmployee',
            employees__pb2.GetEmployeeRequest.SerializeToString,
            employees__pb2.GetEmployeeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEmployeeById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/employees.Employees/GetEmployeeById',
            employees__pb2.GetEmployeeByIdRequest.SerializeToString,
            employees__pb2.GetEmployeeByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateEmployee(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/employees.Employees/CreateEmployee',
            employees__pb2.CreateEmployeeRequest.SerializeToString,
            employees__pb2.CreateEmployeeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateEmployee(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/employees.Employees/updateEmployee',
            employees__pb2.UpdateEmployeeRequest.SerializeToString,
            employees__pb2.UpdateEmployeeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteEmployee(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/employees.Employees/deleteEmployee',
            employees__pb2.DeleteEmployeeRequest.SerializeToString,
            employees__pb2.DeleteEmployeeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)