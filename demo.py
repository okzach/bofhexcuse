from bofhexcuse import bofh_excuse


def main():
    for excuse in bofh_excuse(how_many=1):
        print 'ABORTING, LOG READS AS FOLLOWS:'
        print '> ERROR:'
        print '>  {0}'.format(excuse)
        print 'Please investigate!\n'


if __name__ == '__main__':
    main()
