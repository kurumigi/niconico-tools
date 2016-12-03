# coding: UTF-8
from typing import Tuple, Optional, List, Any, Dict, TypeVar, Union
import logging
import requests

from utility_func import LogIn

VideoId = TypeVar("VideoId", List[str, ...], Tuple[str, ...])
MylistId = TypeVar("MylistId", int, str)
LoggerType = TypeVar("LoggerType", bound=logging.Logger)


class NicoMyList(LogIn):
    WHY_DELETED = ...  # type: Dict[str, str]
    def __init__(self, auth: Tuple[Optional[str], Optional[str]],
                 logger: LoggerType=..., is_silent: bool = ...) -> None:
        super().__init__(auth, logger, is_silent)
        self.session = ...  # type: requests.Session
        self.logger = ...  # type: Union[LoggerType, "AltLogger"]
        self.is_silent = ...  # type: bool
        self.token = ...  # type: Optional[str]
        self.mylists = ...  # type: Dict[int, Dict[str, Union[str, int, bool]]]
        ...
    class AltLogger:
        def emitter(self, text: str, err: bool=..., en: str=...) -> None: ...
        def debug(self, text: str) -> None: ...
        def info(self, text: str) -> None: ...
        def error(self, text: str) -> None: ...
        def warning(self, text: str) -> None: ...
        def critical(self, text: str) -> None: ...

    def get_mylist_ids(self) -> Dict[int, Dict[str, Union[str, int, bool]]]:
        candidate = ...  # type: Dict[int, Dict[str, Union[str, int, bool]]]
        ...
    def get_item_ids(self, list_id: MylistId, *videoids: VideoId) -> Dict[str, str]: ...
    def get_id(self, search_for: str) -> Tuple[int, str]: ...
    def get_response(self, mode: str, is_def: bool, list_id_to: int, video_or_item_id: Optional[str],
                     list_id_from: Optional[int]=...) -> Dict: ...
    def get_jst_from_utime(self, timestamp: int) -> str: ...
    def get_title(self, video_id: str) -> str: ...
    def confirmation(self, mode: str, list_name: str, contents_to_be_deleted: Optional[List[str]]=...) -> bool: ...
    def should_continue(self, res: Dict, vd_id: str, list_name: str, count_now: int, count_whole: int) -> bool: ...
    def create_mylist(self, mylist_name: str, is_public: Optional[bool]=...,
                      desc: Optional[str]=...) -> bool: ...
    def purge_mylist(self, list_id: MylistId) -> bool: ...
    def add(self, list_id: MylistId, *videoids: VideoId) -> bool: ...
    def copy(self, list_id_from: MylistId, list_id_to: MylistId, *videoids: VideoId) -> bool: ...
    def move(self, list_id_from: MylistId, list_id_to: MylistId, *videoids: VideoId) -> bool: ...
    def _copy_or_move_item(self, is_copy: bool, list_id_from: MylistId, list_id_to: MylistId,
                           *videoids: VideoId) -> bool: ...
    def delete(self, list_id: MylistId, *videoids: VideoId) -> bool: ...
    def show_meta(self) -> List[List[str]]:
        container = ...  # type: List[List[str]]
        ...
    def show_one(self, list_id: MylistId, list_name: Optional[str]=...,
                 no_header: bool=...) -> List[List[str]]:
        container = ...  # type: List[List[str]]
        ...
    def show_through(self, simple: bool=...) -> List[List[str]]: ...
    def make_container(self, mode_all: bool=..., no_header: bool=...) -> List[List[str]]: ...
    def append_container_all(self, data: Dict, deflist=...) -> List[str]: ...
    def append_container_one(self, data: Dict, desc: str, name: str=...) -> List[str]: ...
    def export(self, list_id: MylistId, file_name: Optional[str]=...,
               table: Optional[bool]=..., tsv: Optional[bool]=...,
               mode_is_show: Optional[bool]=...) -> None: ...
    def _export_id_only(self, container: List[List[str]], file_name: str=...) -> None: ...
    def _export_tsv(self, container: List[List[str]], file_name: Optional[str]=...) -> None: ...
    def _export_table(self, container: List[List[str]], file_name: Optional[str]=...) -> None: ...
    def writer(self, text: str, file_name: str) -> None: ...


def main(args: Any) -> None: ...


if __name__ == "__main__":
    pass
