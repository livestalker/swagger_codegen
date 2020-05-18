from __future__ import annotations

import pydantic
import datetime
import asyncio
import typing

from pydantic import BaseModel

from swagger_codegen.api.request import ApiRequest


class Order(BaseModel):
    id: typing.Optional[int] = None
    petId: typing.Optional[int] = None
    quantity: typing.Optional[int] = None
    shipDate: typing.Optional[datetime.datetime] = None
    status: typing.Optional[str] = None
    complete: typing.Optional[bool] = None


def make_request(self, __request__: Order,) -> Order:
    """Place an order for a pet"""
    m = ApiRequest(
        method="POST",
        path="/api/v3/store/order".format(),
        content_type="application/json",
        body=__request__.dict(),
        headers=self._only_provided({}, exclude_none=True),
        query_params=self._only_provided({}, exclude_none=True),
        cookies=self._only_provided({}, exclude_none=True),
    )
    return self.make_request({"200": {"application/json": Order,},}, m)
