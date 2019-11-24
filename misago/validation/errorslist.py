from typing import Any, Dict, List, Sequence, Union

from pydantic import PydanticTypeError, PydanticValueError


ROOT_LOCATION = "__root__"


class ErrorsList(List[Dict[str, Any]]):
    def __add__(self, other_list):
        errors_list = list(self)
        for error in other_list:
            if error not in errors_list:
                errors_list.append(error)
        return ErrorsList(errors_list)

    def add_root_error(self, error: Union[PydanticTypeError, PydanticValueError]):
        self.add_error(ROOT_LOCATION, error)

    def add_error(
        self,
        location: Union[str, Sequence[str]],
        error: Union[PydanticTypeError, PydanticValueError],
    ):
        error_dict = {
            "loc": (location,),
            "msg": error.msg_template,
            "type": error.code,
        }

        if error_dict not in self:  # pylint: disable=unsupported-membership-test
            super().append(error_dict)

    def get_errors_locations(self) -> List[str]:
        return [".".join(e["loc"]) for e in self]  # pylint: disable=not-an-iterable

    def get_errors_types(self) -> List[str]:
        return [e["type"] for e in self]  # pylint: disable=not-an-iterable
