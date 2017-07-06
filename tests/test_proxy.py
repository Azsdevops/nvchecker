# MIT licensed
# Copyright (c) 2017 Felix Yan <felixonmars@archlinux.org>, et al.

import aiohttp
import pytest
pytestmark = pytest.mark.asyncio

async def test_proxy(get_version, monkeypatch):
    from nvchecker.source import session

    async def fake_request(*args, proxy, **kwargs):
        class fake_response():
            async def read():
                return proxy.encode("ascii")

            def release():
                pass

        return fake_response

    monkeypatch.setattr(session, "nv_config", {"proxy": "255.255.255.255:65535"}, raising=False)
    monkeypatch.setattr(aiohttp.ClientSession, "_request", fake_request)

    assert await get_version("example", {"regex": "(.+)", "url": "deadbeef"}) == "255.255.255.255:65535"
    assert await get_version("example", {"regex": "(.+)", "url": "deadbeef", "proxy": "0.0.0.0:0"}) == "0.0.0.0:0"
