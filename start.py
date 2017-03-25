
import sys
import struct
import platform


def parsing_cl_args():
    launch_broswer = True

    if len(sys.argv) == 1:
        print("No command line argments found.")
    else:
        try:
            

def main():
    print('Running Python %s (%s bit) on %s' % (platform.python_version(),
          (struct.calcsize('P') * 8), platform.platform()))

    print('\n\n======= Parsing Command line arguments =======\n')


if __name__ == '__main__':
    main()
