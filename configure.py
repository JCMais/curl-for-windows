from __future__ import print_function

import optparse
import os
import sys
import shutil
import platform

script_dir   = os.path.dirname( __file__ )
root_dir     = os.path.normpath( script_dir )
output_dir   = os.path.join( os.path.abspath( root_dir ), 'out' )
curl_root    = os.path.join( os.path.abspath( root_dir ), 'curl' )
libssh2_root = os.path.join( os.path.abspath( root_dir ), 'libssh2' )

sys.path.insert( 0, os.path.join( root_dir, 'build', 'gyp', 'pylib' ) )
import gyp

def host_arch():
    machine = platform.machine()
    if machine == 'i386':
        return 'ia32'
    return 'x64'

# parse our options
parser = optparse.OptionParser()

parser.add_option( '--toolchain',
                action='store',
                type='choice',
                dest='toolchain',
                choices=['2008', '2010', '2012', '2013', '2015', '2017', 'auto'],
                help='msvs toolchain to build for. [default: %default]',
                default='auto')

parser.add_option( '--target-arch',
                action='store',
                dest='target_arch',
                type='choice',
                choices=['ia32', 'x64'],
                help='CPU architecture to build for. [default: %default]',
                default=host_arch() )

( options, args ) = parser.parse_args()


def getoption( value, default ):
  if not value:
    return default
  return value


def configure_defines(o):
    """
    Configures libcurl
    """
    # we probably can make this a config option here...
    o.extend(['-D', 'experimental_quic=0'])
    o.extend(['-D', 'openssl_no_asm=0'])
    o.extend(['-D', 'debug_nghttp2=0'])
    # general options
    o.extend(['-D', 'target_arch=%s' % getoption(options.target_arch, host_arch())])
    o.extend(['-D', 'host_arch=%s' % getoption(options.target_arch, host_arch())])
    o.extend(['-D', 'library=static_library'])


def configure_buildsystem( o ):
    """
    Configures buildsystem
    """
    # gyp target
    o.append( os.path.join( root_dir, 'curl.gyp' ) )

    # includes
    o.extend( ['-I', os.path.join( root_dir, 'common.gypi' )] )

    # msvs
    o.extend( ['-f', 'msvs'] )

    # msvs toolchain
    if options.toolchain:
        o.extend( ['-G', 'msvs_version=' + options.toolchain] )

    # gyp
    o.append( '--depth=' + root_dir )
    o.extend( ['-G', 'output_dir=' + os.path.join( output_dir, options.target_arch )] )
    o.append( '--generator-output=' + os.path.join( output_dir, options.target_arch ) )
    # o.append( '--suffix=.' + options.target_arch )
    #o.append( '--help' )

    # copy tool_hugehelp.c
    # shutil.copy( os.path.join( root_dir, "build\\tool_hugehelp.c" ),
                # os.path.join( curl_root, "lib\\tool_hugehelp.c" ) )

    # copy libssh2_config.h
    shutil.copy( os.path.join( root_dir, "build\\libssh2_config.h" ),
                os.path.join( libssh2_root, "include\\libssh2_config.h" ) )

def run_gyp( args ):
    """
    Executes gyp
    """
    rc = gyp.main( args )
    if rc != 0:
        print('Error running GYP')
        sys.exit( rc )

# gyp arguments
args = []

# gyp configure
configure_buildsystem( args )
configure_defines( args )

gyp_args = list( args )

# build
if __name__ == '__main__':
    run_gyp( gyp_args )
