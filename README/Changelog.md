# 1.1
- fixed searching

# 1.2 
- I swear I just sleep before releasing a new version -_-

# 1.3
- updated to eaf base api v2

# 1.3-1
- switched to httpx
- removed requests from dependencies

# 1.3.4
- fixed downloading webp pins
- fixed downloading pins in general
- added http2 support
- added proxy support
- added brotli compression support
- better headers
- improved networking
- fixed tests

# v2.0
- Converted the entire project to an asynchronous structure using `curl_cffi`'s `AsyncSession`.
- All methods fetching data are now asynchronous and must be awaited (e.g. `client.get_pin(...)` -> `await client.get_pin(...)`).
- Collection fetching methods now return `AsyncGenerator`s instead of standard Generators, which requires the use of `async for` loops.
- Updated all test cases to support `pytest-asyncio`.
- browser impersonation
- dns over https
- proxies 
- and and and 