#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

fpath = '/tmp/pysilhouette_job_failure.txt'

if __name__ == '__main__':
    fp= open(fpath, 'w')
    fp.write('Failure!!\n')
    fp.close()
    try:
        # os.unlink(fpath)
        raise Exception('Failure!!')
    except Exception as e:
        print('stderr : %s!!' % e.args, file=sys.stderr)
        sys.exit(1)
