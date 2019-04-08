# 2013 (C) Peter Rekdal Sunde
# 2016 (C) Jonathan Cardoso Machado
{
  'includes': [
    'common.gypi',
  ],
  'targets':
  [
    {
      'target_name': 'libcurl',
      'type': '<(library)',
      'include_dirs': [
        '.',
        'curl',
        'curl/lib',
        'curl/include',
      ],
      'defines': [
        'USE_SSLEAY',
        'USE_OPENSSL',
        'USE_NGHTTP2',
        'USE_IPV6',
        'USE_LIBSSH2',
        'USE_ZLIB',
        'USE_WINDOWS_SSPI',
        'HAVE_SPNEGO',
        'HAVE_ZLIB_H',
        'HAVE_LIBSSH2_H',
        'HAVE_ZLIB',
        'HAVE_LIBZ',
        'BUILDING_LIBCURL',
      ],
      'dependencies': [
        'openssl/openssl.gyp:openssl',
        'libssh2.gyp:libssh2',
        'zlib.gyp:zlib',
        'nghttp2/nghttp2.gyp:nghttp2'
      ],
      'direct_dependent_settings': {
        'conditions': [
          ['_type=="static_library"',
            {
              'defines':[
                'CURL_STATICLIB'
              ]
            }
          ]
        ],
        'include_dirs': [
          'curl/include',
          'build'
        ],
      },
      'sources':[
        'build/tool_hugehelp.c',
        'curl/lib/altsvc.c',
        'curl/lib/amigaos.c',
        'curl/lib/asyn-ares.c',
        'curl/lib/asyn-thread.c',
        'curl/lib/base64.c',
        'curl/lib/conncache.c',
        'curl/lib/connect.c',
        'curl/lib/content_encoding.c',
        'curl/lib/cookie.c',
        'curl/lib/curl_addrinfo.c',
        'curl/lib/curl_ctype.c',
        'curl/lib/curl_des.c',
        'curl/lib/curl_endian.c',
        'curl/lib/curl_fnmatch.c',
        'curl/lib/curl_gethostname.c',
        'curl/lib/curl_gssapi.c',
        'curl/lib/curl_memrchr.c',
        'curl/lib/curl_multibyte.c',
        'curl/lib/curl_ntlm_core.c',
        'curl/lib/curl_ntlm_wb.c',
        'curl/lib/curl_path.c',
        'curl/lib/curl_range.c',
        'curl/lib/curl_rtmp.c',
        'curl/lib/curl_sasl.c',
        'curl/lib/curl_sspi.c',
        'curl/lib/curl_threads.c',
        'curl/lib/dict.c',
        'curl/lib/doh.c',
        'curl/lib/dotdot.c',
        'curl/lib/easy.c',
        'curl/lib/escape.c',
        'curl/lib/file.c',
        'curl/lib/fileinfo.c',
        'curl/lib/formdata.c',
        'curl/lib/ftp.c',
        'curl/lib/ftplistparser.c',
        'curl/lib/getenv.c',
        'curl/lib/getinfo.c',
        'curl/lib/gopher.c',
        'curl/lib/hash.c',
        'curl/lib/hmac.c',
        'curl/lib/hostasyn.c',
        'curl/lib/hostcheck.c',
        'curl/lib/hostip.c',
        'curl/lib/hostip4.c',
        'curl/lib/hostip6.c',
        'curl/lib/hostsyn.c',
        'curl/lib/http_chunks.c',
        'curl/lib/http_digest.c',
        'curl/lib/http_negotiate.c',
        'curl/lib/http_ntlm.c',
        'curl/lib/http_proxy.c',
        'curl/lib/http.c',
        'curl/lib/http2.c',
        'curl/lib/idn_win32.c',
        'curl/lib/if2ip.c',
        'curl/lib/imap.c',
        'curl/lib/inet_ntop.c',
        'curl/lib/inet_pton.c',
        'curl/lib/ldap.c',
        'curl/lib/llist.c',
        'curl/lib/md4.c',
        'curl/lib/md5.c',
        'curl/lib/memdebug.c',
        'curl/lib/mime.c',
        'curl/lib/mprintf.c',
        'curl/lib/multi.c',
        'curl/lib/netrc.c',
        'curl/lib/non-ascii.c',
        'curl/lib/nonblock.c',
        'curl/lib/openldap.c',
        'curl/lib/parsedate.c',
        'curl/lib/pingpong.c',
        'curl/lib/pipeline.c',
        'curl/lib/pop3.c',
        'curl/lib/progress.c',
        'curl/lib/psl.c',
        'curl/lib/rand.c',
        'curl/lib/rtsp.c',
        'curl/lib/security.c',
        'curl/lib/select.c',
        'curl/lib/sendf.c',
        'curl/lib/setopt.c',
        'curl/lib/sha256.c',
        'curl/lib/share.c',
        'curl/lib/slist.c',
        'curl/lib/smb.c',
        'curl/lib/smtp.c',
        'curl/lib/socks_gssapi.c',
        'curl/lib/socks_sspi.c',
        'curl/lib/socks.c',
        'curl/lib/speedcheck.c',
        'curl/lib/splay.c',
        'curl/lib/ssh-libssh.c',
        'curl/lib/ssh.c',
        'curl/lib/strcase.c',
        'curl/lib/strdup.c',
        'curl/lib/strerror.c',
        'curl/lib/strtok.c',
        'curl/lib/strtoofft.c',
        'curl/lib/system_win32.c',
        'curl/lib/telnet.c',
        'curl/lib/tftp.c',
        'curl/lib/timeval.c',
        'curl/lib/transfer.c',
        'curl/lib/url.c',
        'curl/lib/urlapi.c',
        'curl/lib/vauth/cleartext.c',
        'curl/lib/vauth/cram.c',
        'curl/lib/vauth/digest_sspi.c',
        'curl/lib/vauth/digest.c',
        'curl/lib/vauth/krb5_gssapi.c',
        'curl/lib/vauth/krb5_sspi.c',
        'curl/lib/vauth/ntlm_sspi.c',
        'curl/lib/vauth/ntlm.c',
        'curl/lib/vauth/oauth2.c',
        'curl/lib/vauth/spnego_gssapi.c',
        'curl/lib/vauth/spnego_sspi.c',
        'curl/lib/vauth/vauth.c',
        'curl/lib/version.c',
        'curl/lib/vtls/cyassl.c',
		    'curl/lib/vtls/gskit.c',
		    'curl/lib/vtls/gtls.c',
        'curl/lib/vtls/mbedtls.c',
		    'curl/lib/vtls/mesalink.c',
		    'curl/lib/vtls/nss.c',
		    'curl/lib/vtls/openssl.c',
		    'curl/lib/vtls/polarssl_threadlock.c',
		    'curl/lib/vtls/polarssl.c',
		    'curl/lib/vtls/schannel_verify.c',
		    'curl/lib/vtls/schannel.c',
		    'curl/lib/vtls/sectransp.c',
        'curl/lib/vtls/vtls.c',
        'curl/lib/warnless.c',
        'curl/lib/wildcard.c',
      ],
      'conditions':[
        ['OS=="win"',
          {
            'link_settings': {
              'libraries': [
                '-lws2_32.lib',
                '-lwldap32.lib',
                '-ladvapi32.lib',
              ],
            },
          }
        ],
        ['OS!="mac"',
          {
          # todo
          },
          {
          # linux
          }
        ],
        ['_type=="static_library"',
          {
            'defines':[
              'CURL_STATICLIB'
            ]
          }
        ]
      ],
    },
	{
	  'target_name': 'curl',
	  'type': 'executable',
	  'dependencies': [
      'libcurl',
	  ],
	  'include_dirs': [
      '.',
      'curl/lib',
      'curl/src',
	  ],
	  'defines': [],
	  'sources': [
      'curl/src/tool_binmode.c',
      'curl/src/tool_bname.c',
      'curl/src/tool_cb_dbg.c',
      'curl/src/tool_cb_hdr.c',
      'curl/src/tool_cb_prg.c',
      'curl/src/tool_cb_rea.c',
      'curl/src/tool_cb_see.c',
      'curl/src/tool_cb_wrt.c',
      'curl/src/tool_cfgable.c',
      'curl/src/tool_convert.c',
      'curl/src/tool_dirhie.c',
      'curl/src/tool_doswin.c',
      'curl/src/tool_easysrc.c',
      'curl/src/tool_filetime.c',
      'curl/src/tool_formparse.c',
      'curl/src/tool_getparam.c',
      'curl/src/tool_getpass.c',
      'curl/src/tool_help.c',
      'curl/src/tool_helpers.c',
      'curl/src/tool_homedir.c',
      'curl/src/tool_libinfo.c',
      'curl/src/tool_main.c',
      'curl/src/tool_metalink.c',
      'curl/src/tool_msgs.c',
      'curl/src/tool_operate.c',
      'curl/src/tool_operhlp.c',
      'curl/src/tool_panykey.c',
      'curl/src/tool_paramhlp.c',
      'curl/src/tool_parsecfg.c',
      'curl/src/tool_setopt.c',
      'curl/src/tool_sleep.c',
      'curl/src/tool_urlglob.c',
      'curl/src/tool_util.c',
      'curl/src/tool_vms.c',
      'curl/src/tool_writeout.c',
      'curl/src/tool_xattr.c',
      'curl/src/slist_wc.c'
	  ],
	},
    {
      'target_name': 'example',
      'type': 'executable',
      'dependencies': [
        'libcurl',
      ],
      'sources' : [
        'example.c'
      ],
    },
    #{
      # todo: tests
    #}
  ],
}
