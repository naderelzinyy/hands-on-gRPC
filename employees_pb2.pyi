from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Employee(_message.Message):
    __slots__ = ["id", "name", "email"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    email: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class GetEmployeeRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetEmployeeResponse(_message.Message):
    __slots__ = ["employee"]
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    employee: _containers.RepeatedCompositeFieldContainer[Employee]
    def __init__(self, employee: _Optional[_Iterable[_Union[Employee, _Mapping]]] = ...) -> None: ...

class GetEmployeeByIdRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[_Iterable[str]] = ...) -> None: ...

class GetEmployeeByIdResponse(_message.Message):
    __slots__ = ["employee"]
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    employee: Employee
    def __init__(self, employee: _Optional[_Union[Employee, _Mapping]] = ...) -> None: ...

class CreateEmployeeRequest(_message.Message):
    __slots__ = ["employee"]
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    employee: Employee
    def __init__(self, employee: _Optional[_Union[Employee, _Mapping]] = ...) -> None: ...

class CreateEmployeeResponse(_message.Message):
    __slots__ = ["employee"]
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    employee: Employee
    def __init__(self, employee: _Optional[_Union[Employee, _Mapping]] = ...) -> None: ...

class UpdateEmployeeRequest(_message.Message):
    __slots__ = ["employee"]
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    employee: Employee
    def __init__(self, employee: _Optional[_Union[Employee, _Mapping]] = ...) -> None: ...

class UpdateEmployeeResponse(_message.Message):
    __slots__ = ["employee"]
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    employee: Employee
    def __init__(self, employee: _Optional[_Union[Employee, _Mapping]] = ...) -> None: ...

class DeleteEmployeeRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteEmployeeResponse(_message.Message):
    __slots__ = ["employee"]
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    employee: Employee
    def __init__(self, employee: _Optional[_Union[Employee, _Mapping]] = ...) -> None: ...
