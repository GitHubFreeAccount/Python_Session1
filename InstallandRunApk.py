from __future__ import print_function
import os
import random
import sys
import argparse
import common


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('certificate', help='The certificate to be used.')
    parser.add_argument('package', help='The OTA package to be verified')
    args = parser.parse_args()
    print("%s" % args.certificate)
    print("%s" % args.package)
    out_dir = os.environ.get("OUT", None)
    runner = os.environ.get('INSTRUMENTED_PACKAGE_RUNNER', None)
    apk_path = ('%s/data/app' % out_dir)


def GBK2313():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xfe)
    val = f'{head:x}{body:x}'
    randomsStr = bytes.fromhex(val).decode('gb2312')
    return randomsStr


num = 0
if __name__ == '__main__':
    try:
        for num in range(200):
            print("龙" + GBK2313() + GBK2313())
            num += 1
        main()
    except AssertionError as err:
        print('\n ERROR: %s \n' % (err,))
        sys.exit(1)
    finally:
        common.Cleanup()
