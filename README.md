# Curl for windows

Curl is a command line tool for transferring data specified with URL
syntax. Find out how to use curl by reading the curl.1 man page or the
MANUAL document. Find out how to install Curl by reading the INSTALL
document.

libcurl is the library curl is using to do its job. It is readily
available to be used by your software. 

# About

This repository is a collection of submodules (dependencies)
that curl need to build successfully. Each submodule tracks
the latest known git release tag. In order to make 
this easy to maintain i converted the buildsystem to GYP. 
Please note that this is not a **_FORK_** and no patches has
been applied or sent upstream.

By following the tutorial below, you should be able build
a working, statically linked version of the latest libcurl.

**Both x86 and x64 builds are supported.**

Happy linking ;)

# Curl dependencies

- [Openssl](https://github.com/openssl/openssl)
- [Libssh2](http://libssh2.org)
- [nghttp2](https://nghttp2.org/)
- [Zlib](http://zlib.net)

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
  - zlib.lib
  - wsock32.lib
  - wldap32.lib
  - ws2_32.lib
  
By now you should have sweet, statically linked, CURL! ;)

# Contributing

## Upgrading libcurl

1. Download the zip archive from the latest tag from the curl official repo https://github.com/curl/curl
2. Compare the contents of the extracted sources with the ones at the curl folder on this repo. (I recommend bcompare for that or any other tool that can compare folder contents)
3. Make necessary changes to the curl.gyp file.
   > For example, if a lib source file was removed/added on the new version, it must be 
   > removed/added on the curl.gyp file at the specific target

## Upgrading OpenSSL

OpenSSL is based on Node.js version: https://github.com/nodejs/node/blob/v10.15.0/deps/openssl

At the time of writing this, the upgrade process was as easy as just copying the folder over.
