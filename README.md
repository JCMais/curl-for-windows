# Curl for windows

Curl is a command line tool for transferring data specified with URL
syntax. Find out how to use curl by reading the curl.1 man page or the
MANUAL document. Find out how to install Curl by reading the INSTALL
document.

libcurl is the library curl is using to do its job. It is readily
available to be used by your software.

# About

This is repo is mostly being used by the Node.js native addon [`node-libcurl`](https://github.com/JCMais/node-libcurl)

This was originally a fork of the project https://github.com/peters/curl-for-windows

This repository is a collection of dependencies that curl need to build successfully.
Each submodule tries to track the latest known git release tag. When not using a git submodule
for the dependency, the direct source code was added to this repository, this is the case for
`nghttp2`, `openssl`, and `cares`, for these, their .gyp files were retrieved from the Node.js
source code.

**Both x86 and x64 builds are supported.**

# libcurl dependencies

- [Openssl](https://github.com/openssl/openssl)
- [Libssh2](http://libssh2.org)
- [nghttp2](https://nghttp2.org/)
- [Zlib](http://zlib.net)
- [cares](https://c-ares.haxx.se/)
- [brotli](https://github.com/google/brotli)

# Prerequisites

* [Python 2.7](python.org)
* [Visual Studio](https://visualstudio.microsoft.com/pt-br/vs/community/)
* [NASM](https://www.nasm.us/) (Required to use ASM version of openssl)

# Obtaining prerequisites 
	
    $ git clone https://github.com/JCMais/curl-for-windows.git
    $ git submodule update --init --recursive
      
# Configuration options
    
    $ python configure.py --help

```
Usage: configure.py [options]

Options:
  -h, --help            show this help message and exit
  --toolchain=TOOLCHAIN
                        msvs toolchain to build for. [default: auto]
  --target-arch=TARGET_ARCH
                        CPU architecture to build for. [default: x86]
```

# Generate project files

    $ python configure.py 

Open respective **curl.sln** found in **out** folder ;)

# Simple curl example

If you are new to curl you can checkout the example project
found in curl.sln or you can view additional the **[examples](https://github.com/bagder/curl/tree/master/docs/examples)**
in the official curl repository.

# Linking with libcurl (without gyp)

- Add preprocessor flag 
  - CURL_STATICLIB
 
- Add include directory
	- path/to/curl/include

- Add additional library search directory
	- path/to/out/Debug|Release/obj
	
- Link with the following libraries
  - libcurl.lib
  - openssl.lib
  - libssh2.lib
  - brotli.lib
  - cares.lib
  - zlib.lib
  - wsock32.lib
  - wldap32.lib
  - ws2_32.lib

The following libraries are available here, but not being used (yet):
- nghttp3
- ngtcp2
  
By now you should have sweet, statically linked, CURL! ;)

# Contributing

## Upgrading libcurl

1. Download the zip archive from the latest tag from the curl official repo https://github.com/curl/curl
2. Compare the contents of the extracted sources with the ones at the curl folder on this repo. (I recommend bcompare for that or any other tool that can compare folder contents)
3. Make necessary changes to the curl.gyp file.
   > For example, if a lib/src file was removed/added on the new version, it must be 
   > removed/added on the curl.gyp file at the specific target
4. After changes are made, cd into the `curl` directory and run:
    ```shell
    $ git fetch origin
    $ git checkout <curl-tag-version>
    ```

## Upgrading libssh2

Same than libcurl

# Upgrading nghttp2

nghttp2 is based on Node.js version: https://github.com/nodejs/node/blob/v12.16.1/deps/nghttp2

At the time of writing this, the upgrade process was as easy as:
1. copy the folder over.
2. on `nghttp2/nghttp2.gyp`:
   1. Comment:
      ```
          'msvs_settings': {
            'VCCLCompilerTool': {
              'CompileAs': '1'
            },
          },
      ```
3. done.

## Upgrading OpenSSL

OpenSSL is based on Node.js version: https://github.com/nodejs/node/blob/v10.15.0/deps/openssl

At the time of writing this, the upgrade process was as easy as:
1. copy the folder over.
2. on `openssl/openssl.gyp`:
   1. Add `'experimental_quic%': '0',` to the list of variables.
3. done.

## Upgrading c-ares

c-ares is based on Node.js version: https://github.com/nodejs/node/blob/v15.0.0/deps/cares

At the time of writing this, the upgrade process was as easy as:
1. copy the folder over.
2. done.

## Upgrading brotli

brotli is based on Node.js version: https://github.com/nodejs/node/blob/v15.0.0/deps/brotli

At the time of writing this, the upgrade process was as easy as:
1. copy the folder over.
2. done.

## Upgrading nghttp3

nghttp3 is based on Node.js version: https://github.com/nodejs/node/blob/v15.0.0/deps/nghttp3

At the time of writing this, the upgrade process was as easy as:
1. copy the folder over.
2. done.


## Upgrading ngtcp2

ngtcp2 is based on Node.js version: https://github.com/nodejs/node/blob/v15.0.0/deps/ngtcp2

At the time of writing this, the upgrade process was as easy as:
1. copy the folder over.
2. done.
