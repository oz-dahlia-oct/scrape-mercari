#!/usr/bin/env python
# coding: utf-8


# Import built-in modules
import codecs
from datetime import datetime
import time


class Log:
    """
    ログ記録用のクラス
    静的クラス
    ※ 書き換えない
    """

    log = []
    force_logount_count = 0
    crash_count = 0
    count = None
    count_start_at = None
    start_at = None
    elapsed_time = None


    def start():
        Log.start_at = datetime.now()
        Log.log = []
        Log.force_logount_count = 0
        Log.crash_count = 0
        Log.count = 0
        Log.count_start_at = None
        Log.printlog()
        Log.printlog()
        Log.printlog('-------------------- start --------------------')
        Log.printlog(
            'start at:',
            Log.start_at
        )
        

    def set_countdown(count):
        Log.count = count
        Log.count_start_at = time.time()


    def countdown(show=True):
        if Log.count:
            Log.count -= 1
            Log.printlog(
                'Log countdown rest:',
                Log.count,
                show=show,
            )

            if Log.count == 0:
                msg = "Log countdown successfully finished !!! \ntotal elapsed time:"
            else:
                msg = "elapsed time:"

            Log.elapsed_time = time.time() - Log.count_start_at

            Log.printlog(
                msg,
                Log.elapsed_time,
                "[sec]",
                show=show
            )
        else:
            Log.printlog(
                'Check Log.count !!!',
                'You should use down method after using set_countdown.',
                'Your countdown may be finished.'
            )


    def printlog(*args, **kwargs):
        result = ''

        for arg in args:
            result += str(arg) + ' '
            
        Log.log.append(result)

        if len(kwargs) == 0:
            kwargs['show'] = True

        if kwargs['show']:
            print(result)


    def save_log():
        file_name = datetime.strftime(datetime.now(), 'log/%Y%m%d_%H%M%S_log.txt')
        with codecs.open(file_name, 'a', Conf.encoding) as f:
            for l in Log.log:
                f.write(l)
                f.write('\n')


    def print_length():
        Log.printlog(
            'Log length:', 
            len(Log.log)
        )


    def end():
        Log.printlog()
        Log.printlog('-------------------- end --------------------')
        Log.printlog()
        Log.printlog()
        Log.print_length()
        Log.save_log()
        Log.log = []
        Log.force_logount_count = 0
        Log.count = None
        Log.count_start_at = None
        Log.start_at = None


