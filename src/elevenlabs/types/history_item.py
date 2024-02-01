# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .feedback_item import FeedbackItem
from .history_item_state import HistoryItemState
from .voice_category import VoiceCategory

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class HistoryItem(pydantic.BaseModel):
    history_item_id: str
    voice_id: str
    voice_name: str
    text: str
    date_unix: int
    character_count_change_from: int
    character_count_change_to: int
    content_type: str
    state: HistoryItemState
    request_id: typing.Optional[str]
    model_id: typing.Optional[str]
    voice_category: typing.Optional[VoiceCategory]
    settings: typing.Optional[typing.Dict[str, typing.Any]]
    feedback: typing.Optional[FeedbackItem]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
