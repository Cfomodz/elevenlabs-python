# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.remove_none_from_dict import remove_none_from_dict
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.audio_native_create_project_response_model import AudioNativeCreateProjectResponseModel
from ..types.audio_native_get_embed_code_response_model import AudioNativeGetEmbedCodeResponseModel
from ..types.http_validation_error import HttpValidationError

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AudioNativeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self,
        *,
        name: str,
        image: str,
        author: str,
        small: bool,
        text_color: str,
        background_color: str,
        sessionization: int,
        voice_id: str,
        model_id: str,
        file: core.File,
        auto_convert: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AudioNativeCreateProjectResponseModel:
        """
        Creates AudioNative enabled project, optionally starts conversion and returns project id and embeddable html snippet.

        Parameters:
            - name: str. Project name.

            - image: str. Image URL used in the player. If not provided, default image set in the Player settings is used.

            - author: str. Author used in the player. If not provided, default author set in the Player settings is used.

            - small: bool. Whether to use small player or not. If not provided, default value set in the Player settings is used.

            - text_color: str. Text color used in the player. If not provided, default text color set in the Player settings is used.

            - background_color: str. Background color used in the player. If not provided, default background color set in the Player settings is used.

            - sessionization: int. Specifies for how many minutes to persist the session across page reloads. If not provided, default sessionization set in the Player settings is used.

            - voice_id: str. Voice ID used to voice the content. If not provided, default voice ID set in the Player settings is used.

            - model_id: str. TTS Model ID used in the player. If not provided, default model ID set in the Player settings is used.

            - file: core.File. See core.File for more documentation

            - auto_convert: bool. Whether to auto convert the project to audio or not.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/audio-native"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            data=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "name": name,
                        "image": image,
                        "author": author,
                        "small": small,
                        "text_color": text_color,
                        "background_color": background_color,
                        "sessionization": sessionization,
                        "voice_id": voice_id,
                        "model_id": model_id,
                        "auto_convert": auto_convert,
                    }
                )
            )
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "name": name,
                            "image": image,
                            "author": author,
                            "small": small,
                            "text_color": text_color,
                            "background_color": background_color,
                            "sessionization": sessionization,
                            "voice_id": voice_id,
                            "model_id": model_id,
                            "auto_convert": auto_convert,
                        }
                    )
                ),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            files=core.convert_file_dict_to_httpx_tuples(remove_none_from_dict({"file": file})),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AudioNativeCreateProjectResponseModel, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_embed_code(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AudioNativeGetEmbedCodeResponseModel:
        """
        Get the HTML snippet to embed the AudioNative player into a webpage.

        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from elevenlabs.client import ElevenLabs

        client = ElevenLabs(
            api_key="YOUR_API_KEY",
        )
        client.audio_native.get_embed_code()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/audio-native/get-embed-code"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AudioNativeGetEmbedCodeResponseModel, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_project_embed_code(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AudioNativeGetEmbedCodeResponseModel:
        """
        Get the HTML snippet to embed the AudioNative player into a webpage. The embedded player will not convert content from the webpage but instead play the specified project

        Parameters:
            - project_id: str. The project_id of the project, you can query GET https://api.elevenlabs.io/v1/projects to list all available projects.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from elevenlabs.client import ElevenLabs

        client = ElevenLabs(
            api_key="YOUR_API_KEY",
        )
        client.audio_native.get_project_embed_code(
            project_id="project_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"v1/audio-native/{jsonable_encoder(project_id)}/get-embed-code",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AudioNativeGetEmbedCodeResponseModel, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAudioNativeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self,
        *,
        name: str,
        image: str,
        author: str,
        small: bool,
        text_color: str,
        background_color: str,
        sessionization: int,
        voice_id: str,
        model_id: str,
        file: core.File,
        auto_convert: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AudioNativeCreateProjectResponseModel:
        """
        Creates AudioNative enabled project, optionally starts conversion and returns project id and embeddable html snippet.

        Parameters:
            - name: str. Project name.

            - image: str. Image URL used in the player. If not provided, default image set in the Player settings is used.

            - author: str. Author used in the player. If not provided, default author set in the Player settings is used.

            - small: bool. Whether to use small player or not. If not provided, default value set in the Player settings is used.

            - text_color: str. Text color used in the player. If not provided, default text color set in the Player settings is used.

            - background_color: str. Background color used in the player. If not provided, default background color set in the Player settings is used.

            - sessionization: int. Specifies for how many minutes to persist the session across page reloads. If not provided, default sessionization set in the Player settings is used.

            - voice_id: str. Voice ID used to voice the content. If not provided, default voice ID set in the Player settings is used.

            - model_id: str. TTS Model ID used in the player. If not provided, default model ID set in the Player settings is used.

            - file: core.File. See core.File for more documentation

            - auto_convert: bool. Whether to auto convert the project to audio or not.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/audio-native"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            data=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "name": name,
                        "image": image,
                        "author": author,
                        "small": small,
                        "text_color": text_color,
                        "background_color": background_color,
                        "sessionization": sessionization,
                        "voice_id": voice_id,
                        "model_id": model_id,
                        "auto_convert": auto_convert,
                    }
                )
            )
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "name": name,
                            "image": image,
                            "author": author,
                            "small": small,
                            "text_color": text_color,
                            "background_color": background_color,
                            "sessionization": sessionization,
                            "voice_id": voice_id,
                            "model_id": model_id,
                            "auto_convert": auto_convert,
                        }
                    )
                ),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            files=core.convert_file_dict_to_httpx_tuples(remove_none_from_dict({"file": file})),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AudioNativeCreateProjectResponseModel, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_embed_code(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AudioNativeGetEmbedCodeResponseModel:
        """
        Get the HTML snippet to embed the AudioNative player into a webpage.

        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from elevenlabs.client import AsyncElevenLabs

        client = AsyncElevenLabs(
            api_key="YOUR_API_KEY",
        )
        await client.audio_native.get_embed_code()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/audio-native/get-embed-code"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AudioNativeGetEmbedCodeResponseModel, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_project_embed_code(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AudioNativeGetEmbedCodeResponseModel:
        """
        Get the HTML snippet to embed the AudioNative player into a webpage. The embedded player will not convert content from the webpage but instead play the specified project

        Parameters:
            - project_id: str. The project_id of the project, you can query GET https://api.elevenlabs.io/v1/projects to list all available projects.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from elevenlabs.client import AsyncElevenLabs

        client = AsyncElevenLabs(
            api_key="YOUR_API_KEY",
        )
        await client.audio_native.get_project_embed_code(
            project_id="project_id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"v1/audio-native/{jsonable_encoder(project_id)}/get-embed-code",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AudioNativeGetEmbedCodeResponseModel, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
